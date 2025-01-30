from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from app.models.db.base_class import Base
class User(Base):
    __tablename__ = "users" # Nom de la table dans la base de données
    uuid = Column(String(255), primary_key=True, index=True) # Clé primaire
    username = Column(String(255),index=True, nullable=False) # Nom d'utilisateur unique
    email = Column(String(255), unique=True, index=True, nullable=False) # Email unique
    phone_number=Column(String(255),unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False) # Mot de passe haché
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True) # Statut actif ou non
    created_at = Column(DateTime, default=datetime.utcnow) # Date de création
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # added_by = Column(String ,ForeignKey("auth.uuid"),nullable=True )
# auth =relationship("Auth",foreign_keys=[added_by])

    # Dernière mise à jour
