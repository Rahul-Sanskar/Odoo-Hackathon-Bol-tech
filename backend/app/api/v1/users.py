from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.core.security import get_password_hash
from app.schemas.user import UserResponse, UserUpdate
from app.models.user import User
router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def read_user_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_public and current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Private profile")
    return UserResponse.from_orm(user)

@router.put("/me", response_model=UserResponse)
async def update_user(user: UserUpdate, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    db_user = db.query(User).filter(User.id == current_user.id).first()
    update_data = user.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return UserResponse.from_orm(db_user)