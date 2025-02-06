from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import datetime
from typing import Optional

class AuthBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str

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

class AuthResponse(AuthBase):
    uuid: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    status: str
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

