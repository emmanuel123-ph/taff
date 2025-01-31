from datetime import timedelta, datetime
from typing import Any, List

from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app import schemas, crud, models
from app.core.i18n import __
from app.core.security import create_access_token, get_password_hash
from app.core.config import Config

router = APIRouter(prefix="", tags=["users"])

@router.post("/register", response_model=schemas.UserResponse)
async def register(
    obj_in: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    user = crud.create_user(db=db, obj_in=obj_in)
    return user  # FastAPI convertira automatiquement l'objet SQLAlchemy en UserResponse

@router.put("/update", response_model=schemas.UserResponse)
def update(
    obj_in: schemas.UserUpdate, 
    db: Session = Depends(get_db),
):
    user = crud.update_user(db=db, obj_in=obj_in)
    return user

@router.delete("/delete_by_uuid/{uuid}", response_model=schemas.Msg)
def delete_by_uuid(
    uuid: str,
    db: Session = Depends(get_db),
):
    # Appel de la fonction de suppression par UUID
    crud.delete_user(db=db, uuid=uuid)
    return schemas.Msg(message="User deleted successfully")

@router.delete("/delete_by_list", response_model=schemas.Msg)
def delete_by_list(
    uuids: List[str],  # Liste d'UUID des utilisateurs à supprimer
    db: Session = Depends(get_db),
):
    deleted_count = crud.delete_user_by_list(db=db, uuids=uuids)  # Appel à la fonction pour marquer comme supprimé
    return {"message": f"{deleted_count} users marked as deleted successfully"}  # Retour avec un message


@router.put("/actived_by_uuid/{uuid}", response_model=schemas.Msg)
def actived_by_uuid(
    uuid: str,
    db: Session = Depends(get_db),
):
    # Appel de la fonction d'activation par UUID
    crud.activate_user(db=db, uuid=uuid)
    return {"message": "User activated successfully"}

@router.put("/deactivated_by_uuid/{uuid}", response_model=schemas.Msg)
def deactivate_by_uuid(
    uuid: str,
    db: Session = Depends(get_db),
):
    # Appel de la fonction de désactivation par UUID
    crud.deactivate_user(db=db, uuid=uuid)
    return {"message": "User deactivated successfully"}


@router.put("/deactivate_by_list", response_model=schemas.Msg)
def deactivate_by_list(
    uuids: List[str],  # Le nom de l'argument ici doit être 'uuids' pour correspondre à la fonction
    db: Session = Depends(get_db),
):
    deactivated_count = crud.deactivate_user_by_list(db=db, uuids=uuids)  # Utilisation du bon argument 'uuids'
    return {"message": f"{deactivated_count} users deactivated successfully"}

@router.put("/activate_by_list", response_model=schemas.Msg)
def activate_by_list(
    uuids: List[str],  # Liste d'UUID des utilisateurs à activer
    db: Session = Depends(get_db),
):
    activated_count = crud.activate_user_by_list(db=db, uuids=uuids)  # Appel à la fonction pour activer les utilisateurs
    return {"message": f"{activated_count} users activated successfully"}  # Retour avec un message

