from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum
from sqlalchemy.orm import relationship
from app.models.db.base_class import Base

class StatutsConges(str,Enum):
    PENDING = "PENDING"
    CANCELLED ="CANCELLED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"

class Conges(Base):
    uuid= Column(String,primary_key=True)
    start_date=Column(DateTime)
    total_duration = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)
    end_date = Column(DateTime,nullable=False)
    status = Column(String,default=StatutsConges.PENDING)
    is_deleted = Column(Boolean, default=False)
    user_uuid =Column(String,ForeignKey("users.uuid",ondelete="CASCADE"),nullable=False)
    user=relationship("User",foreign_keys=[user_uuid])
    created_at = Column(DateTime, default=datetime.utcnow) # Date de création
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)