import uuid 
from sqlalchemy.orm import Session 
from app.models import Auth
from app.schemas import AuthUpdate,AuthCreate,AuthDelete
from fastapi import HTTPException,status



def get_auth_by_uuid(db:Session,uuid:str):
    return db.query(Auth).filter(Auth.uuid==uuid, Auth.is_deleted==False).first()


def get_auth_by_email(db:Session,email:str):
    return db.query(Auth).filter(Auth.email==email, Auth.is_deleted==False).first()

def get_auth_by_phone_number(db:Session,phone_number:str):
    return db.query(Auth).filter(Auth.phone_number==phone_number, Auth.is_deleted==False).first()


def create_auth(db:Session, obj_in:AuthCreate):
    exist_email= get_auth_by_email(db=db,email=obj_in.email)
    if exist_email is not None:
        raise HTTPException(status_code=409,detail="this email is already exist")
    exist_phone_number= get_auth_by_phone_number(db=db, phone_number=obj_in.phone_number)
    if exist_phone_number is not None:
        raise HTTPException(status_code=409,detail="this phone number is already exist")
    new_auth = Auth(
        uuid=str(uuid.uuid4()),
        first_name=obj_in.first_name,
        last_name=obj_in.last_name,
        email=obj_in.email,
        phone_number=obj_in.phone_number
    )

    db.add(new_auth)
    db.commit()
    db.refresh(new_auth)
    return new_auth