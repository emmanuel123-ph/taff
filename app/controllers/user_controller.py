from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core.dependencies import get_db

router = APIRouter(prefix="", tags=["users"])

@router.post("/register", response_model=schemas.UserResponse)
def register(
    obj_in: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    user=crud.create_user(db=db,obj_in=obj_in)
    return user

@router.delete("/delete_by_uuid", response_model=schemas.Msg)
def delete_by_uuid(
    obj_in: schemas.UserDelete,
    db: Session = Depends(get_db)
):
    crud.delete_user(db=db,uuid=obj_in.uuid)
    return schemas.Msg(message="User deleted successfully")

@router.put("/deactivate_by_uuid", response_model=schemas.Msg)
def deactivate_by_uuid(
    uuid: str,
    db: Session = Depends(get_db)
):
    crud.deactivate_user(db=db,uuid=uuid)
    return schemas.Msg(message="User deactivated successfully")

@router.put("/activate_by_uuid", response_model=schemas.Msg)
def activate_by_uuid(
    uuid: str,
    db: Session = Depends(get_db)
):
    crud.activate_user(db=db,uuid=uuid)
    return schemas.Msg(message="User activated successfully")