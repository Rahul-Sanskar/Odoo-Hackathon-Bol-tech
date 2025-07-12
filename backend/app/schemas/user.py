from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    location: Optional[str] = None
    profile_photo: Optional[str] = None
    is_public: bool = True

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True