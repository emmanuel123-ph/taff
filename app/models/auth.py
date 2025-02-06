from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum
from app.models.db.base_class import Base


class AuthStatus(str,Enum):
    ACTIVATED = "ACTIVATED"
    UNACTIVATED = "UNACTIVATED"
    DELETED ="DELETED"
    BLOCKED = "BLOCKED"

class Auth(Base):
     __tablename__ = "auth" # Nom de la table dans la base de données
     uuid= Column(String(36),primary_key=True)
     first_name= Column(String(255),nullable=False )
     last_name =Column(String(255),nullable=False)
     email= Column(String(255),unique=True,nullable=False)
     phone_number=Column(String(255),unique=True, nullable=False)
     status = Column(String(255),default=AuthStatus.ACTIVATED)
     is_deleted = Column(Boolean, default=False)
     created_at = Column(DateTime, default=datetime.utcnow) # Date de création
     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
     hashed_password = Column(String(255), nullable=False) # Mot de passe haché
     