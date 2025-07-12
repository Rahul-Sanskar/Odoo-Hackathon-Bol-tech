from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FeedbackBase(BaseModel):
    rating: int
    comment: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    swap_id: int

class FeedbackResponse(FeedbackBase):
    id: int
    user_id: int
    swap_id: int
    created_at: datetime

    class Config:
        orm_mode = True