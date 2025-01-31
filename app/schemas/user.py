from pydantic import BaseModel, ConfigDict,EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone_number: str  # Assure-toi que le champ est bien présent
    hashed_password: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    uuid:str
    username:Optional[str]
    email:Optional[EmailStr]
    phone_number:Optional[str]
    hashed_password:Optional[str]
#pour la modification des donnees de l'utilisateur
class UserDelete(BaseModel):
    uuid:str
#pour supprimer un seule utilisateur uniquement
class UserDeleteList(BaseModel):
    uuid:list[str]
#pour supprimer plusieur utilisateur au choix

class UserResponse(BaseModel):
    uuid:str
    username:str
    email:EmailStr
    phone_number:str
    is_active:bool
    created_at:datetime
    updated_at:datetime
    model_config = ConfigDict(from_attributes=True)
