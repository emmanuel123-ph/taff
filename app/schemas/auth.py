from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import datetime
from typing import Optional

class AuthBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    hashed_password:str

class AuthCreate(AuthBase):
    pass



class AuthUpdate(BaseModel):
    uuid: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None


class AuthDelete(BaseModel):
    uuid: str

class AuthResponse(BaseModel):
    uuid: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    status: str
    is_deleted: bool
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str  # Assurez-vous que ce soit une chaîne de caractères non optionnelle
    token_type: str    # Assurez-vous que ce soit une chaîne de caractères non optionnelle
    model_config = ConfigDict(from_attributes=True)

class AuthAuthentification(BaseModel):
    auth: AuthResponse
    token: Token  # Assurez-vous que ce soit de type `Token`
    model_config = ConfigDict(from_attributes=True)


class AuthLogin(BaseModel):
    email:str
    password:str

