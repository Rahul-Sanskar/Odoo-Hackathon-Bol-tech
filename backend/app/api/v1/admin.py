from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db, get_current_admin
from app.models.user import User
from app.models.skill import Skill
from app.models.swap import Swap
from app.api.v1.models import UserResponse

router = APIRouter()

@router.post("/ban/{user_id}")
async def ban_user(user_id: int, db: Session = Depends(get_db), current_admin: UserResponse = Depends(get_current_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = False
    db.commit()
    return {"detail": "User banned"}

@router.post("/reject_skill/{skill_id}")
async def reject_skill(skill_id: int, db: Session = Depends(get_db), current_admin: UserResponse = Depends(get_current_admin)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(skill)
    db.commit()
    return {"detail": "Skill rejected"}

@router.get("/report")
async def generate_report(db: Session = Depends(get_db), current_admin: UserResponse = Depends(get_current_admin)):
    swaps = db.query(Swap).all()
    return [{"id": swap.id, "status": swap.status, "created_at": swap.created_at} for swap in swaps]