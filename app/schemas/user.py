from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username:str
    email:EmailStr
    phone_nunber:str
    hashed_password:str

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
    phone_nunber:str
    is_active:bool
    created_at:datetime
    updated_at:datetime