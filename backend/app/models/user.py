from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    location = Column(String, nullable=True)
    profile_photo = Column(String, nullable=True)
    is_public = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    skills = relationship("Skill", back_populates="user")
    swaps_initiated = relationship("Swap", back_populates="initiator", foreign_keys="[Swap.initiator_id]")
    swaps_received = relationship("Swap", back_populates="receiver", foreign_keys="[Swap.receiver_id]")
    feedback = relationship("Feedback", back_populates="user")