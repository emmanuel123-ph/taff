

from datetime import timedelta, datetime
from typing import Any, List

from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app import schemas, crud, models
from app.core.i18n import __
from app.core.security import create_access_token, get_password_hash
from app.core.config import Config

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("", response_model=schemas.AuthResponse)
def create(
    obj_in: schemas.AuthCreate,
    db: Session = Depends(get_db),
):
   return crud.create_auth(db=db, obj_in=obj_in)

@router.get("/{uuid}", response_model=schemas.AuthResponse)
def read(
    uuid: str,
    db: Session = Depends(get_db),
):
    return crud.get_auth_by_uuid(db=db, uuid=uuid)


@router.delete("/delete_by_uuid/{uuid}",response_model=schemas.Msg)
def delete(
    uuid: str,
    db: Session = Depends(get_db),
):
    crud.delete_auth(db=db,uuid=uuid)
    return {"message" : __("Auth deleted successfully")}

@router.put("/deactivate_by_uuid/{uuid}",response_model=schemas.Msg)
def deactivate(
    uuid: str,
    db: Session = Depends(get_db),
):
    crud.deactivate_auth(db=db,uuid=uuid)
    return {"message" : __("Auth deactived successfully")}

@router.put("/activated_by_uuid/{uuid}",response_model=schemas.Msg)
def activate(
    uuid: str,
    db: Session = Depends(get_db),
):
    crud.activated_auth(db=db,uuid=uuid)
    return{"message" : __("Auth actived successfully")}

@router.put("/blocked_by_uuid/{uuid}",response_model=schemas.Msg)
def blocked(
    uuid:str,
    db: Session = Depends(get_db),
    
):
    crud.blocked_auth(db=db,uuid=uuid)
    return{"message" : __("Auth blocked successfully")}



