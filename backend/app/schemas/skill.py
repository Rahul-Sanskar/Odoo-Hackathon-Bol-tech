from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SkillBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_offered: bool = True
    availability: Optional[str] = None

class SkillCreate(BaseModel):
    name: str
    description: Optional[str] = None
    is_offered: bool
    availability: Optional[str] = None

    class Config:
        from_attributes = True

class SkillResponse(SkillBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True