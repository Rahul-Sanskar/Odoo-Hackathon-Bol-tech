from pydantic import BaseModel
from datetime import datetime

class SwapBase(BaseModel):
    skill_offered_id: int
    skill_wanted_id: int

class SwapCreate(SwapBase):
    receiver_id: int

class SwapResponse(SwapBase):
    id: int
    initiator_id: int
    receiver_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True