from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional


class AuthBase(BaseModel):
    uuid:str
    email:EmailStr
    phone_number:str

class AuthCreate (AuthBase):
    pass

class AuthUpdate(BaseModel):
    uuid:Optional[str]
    email:Optional[EmailStr]
    phone_number:Optional[str]

#pour supprimer plusieur utilisateurs au choix
class AuthDeleteList(BaseModel):
    uuid:list[str]
class AuthResponse (BaseModel):
    uuid:str
    email:EmailStr
    phone_number:str
    created_at:datetime
    updated_at:datetime