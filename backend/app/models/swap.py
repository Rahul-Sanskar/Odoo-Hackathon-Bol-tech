from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Swap(Base):
    __tablename__ = "swaps"
    id = Column(Integer, primary_key=True, index=True)
    initiator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    skill_offered_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    skill_wanted_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    status = Column(String, default="pending")  # pending, accepted, rejected, deleted
    created_at = Column(DateTime, default=datetime.utcnow)
    initiator = relationship("User", back_populates="swaps_initiated", foreign_keys=[initiator_id])
    receiver = relationship("User", back_populates="swaps_received", foreign_keys=[receiver_id])
    skill_offered = relationship("Skill", foreign_keys=[skill_offered_id])
    skill_wanted = relationship("Skill", foreign_keys=[skill_wanted_id])