from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    location: Optional[str]
    profile_photo: Optional[str]
    is_public: bool
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True