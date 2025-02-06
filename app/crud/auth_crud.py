import uuid
from sqlalchemy.orm import Session
from app import models
from app.models import Auth
from app.schemas import AuthCreate, AuthUpdate, AuthDelete, AuthResponse
from fastapi import HTTPException  , status


def get_auth_by_uuid(db: Session, uuid: str):
    return db.query(Auth).filter(Auth.uuid == uuid,Auth.is_deleted==False).first()

def get_auth_by_email(db: Session, email: str):
    return db.query(Auth).filter(Auth.email == email,Auth.is_deleted==False).first()

def get_auth_by_phone_number(db: Session, phone_number: str):
    return db.query(Auth).filter(Auth.phone_number == phone_number,Auth.is_deleted==False).first()


def create_auth(db:Session,obj_in:AuthCreate):

    exit_email=get_auth_by_email(db=db,email=obj_in.email)
    if exit_email is not None:
        raise HTTPException(status_code=409,detail="Email already exist")
    exist_phone_number=get_auth_by_phone_number(db=db,phone_number=obj_in.phone_number)
    if exist_phone_number is not None:
        raise HTTPException(status_code=409,detail="Phone number already exist")
    new_auth = Auth(
        uuid=str(uuid.uuid4()),
        first_name=obj_in.first_name,
        last_name=obj_in.last_name,
        email=obj_in.email,
        phone_number=obj_in.phone_number,
    )

    db.add(new_auth)
    db.commit()
    db.refresh(new_auth)
    return new_auth

def delete_auth(db:Session,uuid:str):
    auth=get_auth_by_uuid(db=db,uuid=uuid)
    if auth is None:
        raise HTTPException(status_code=404,detail="auth not found")
    auth.is_deleted=True
    db.commit()

def deactivate_auth(db:Session,uuid:str):
    auth = get_auth_by_uuid(db=db,uuid=uuid)
    if auth is None:
        raise HTTPException(status_code=404,detail="Auth not found")
    auth.status = models.AuthStatus.UNACTIVATED
    db.commit()


def activated_auth(db:Session,uuid:str):
    auth=get_auth_by_uuid(db=db,uuid=uuid)
    if auth is None :
        raise HTTPException(status_code=404,detail="auth not found")
    auth.status =models.AuthStatus.ACTIVATED
    db.commit()


def blocked_auth(db:Session,uuid:str):
    auth=get_auth_by_uuid(db=db,uuid=uuid)
    if auth is None :
        raise HTTPException(status_code=404,detail="auth not found")
    auth.status=models.AuthStatus.BLOCKED
    db.commit()

