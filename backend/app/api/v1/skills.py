from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List
from app.dependencies import get_db, get_current_user
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillResponse
from app.api.v1.models import UserResponse

router = APIRouter()

@router.post("/", response_model=SkillResponse)
async def create_skill(skill: SkillCreate, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    db_skill = Skill(**skill.dict(), user_id=current_user.id)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return SkillResponse.from_orm(db_skill)

@router.get("/", response_model=List[SkillResponse])
async def list_skills(db: Session = Depends(get_db)):
    skills = db.query(Skill).all()
    return [SkillResponse.from_orm(skill) for skill in skills]

@router.get("/search", response_model=List[SkillResponse])
async def search_skills(query: str, db: Session = Depends(get_db)):
    skills = db.query(Skill).filter(
        or_(Skill.name.ilike(f"%{query}%"), Skill.description.ilike(f"%{query}%"))
    ).all()
    return [SkillResponse.from_orm(skill) for skill in skills]