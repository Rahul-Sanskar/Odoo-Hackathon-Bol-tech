from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db, get_current_admin
from app.models.user import User
from app.models.skill import Skill
from app.models.swap import Swap
from app.schemas.user import UserResponse, UserUpdate

router = APIRouter()

@router.post("/ban/{user_id}")
async def ban_user(user_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = False
    db.commit()
    return {"detail": "User banned"}

@router.post("/reject_skill/{skill_id}")
async def reject_skill(skill_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(skill)
    db.commit()
    return {"detail": "Skill rejected"}

@router.get("/report")
async def generate_report(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    swaps = db.query(Swap).all()
    return [{"id": swap.id, "status": swap.status, "created_at": swap.created_at} for swap in swaps]

@router.get("/users", response_model=List[UserResponse])
async def list_users(db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    return db.query(User).all()

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    # Delete associated swaps to avoid foreign key constraint violation
    db.query(Swap).filter((Swap.initiator_id == user_id) | (Swap.receiver_id == user_id)).delete()
    # Delete associated skills to avoid foreign key constraint violation
    db.query(Skill).filter(Skill.user_id == user_id).delete()
    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted"}