import uuid
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate,UserDelete,UserUpdate,UserResponse
from fastapi import HTTPException,status


def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(User.email==email,User.is_deleted==False).first()

def get_user_by_phone_number(db:Session,phone_number:str):
    return db.query(User).filter(User.phone_number==phone_number,User.is_deleted==False).first()

def create_user(db:Session,obj_in:UserCreate):
    exist_email = get_user_by_email(db,email=obj_in.email)
    if exist_email is not None: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,message="This email is already exist")
    exist_phone_number = get_user_by_phone_number(db,phone_number=obj_in.phone_number)
    if exist_phone_number is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, message="This phone number is already exist")
    new_user = User(
        uuid = str(uuid.uuid4()),
        username = obj_in.username,
        email = obj_in.email,
        phone_number = obj_in.phone_number,
        hashed_password = obj_in.hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
