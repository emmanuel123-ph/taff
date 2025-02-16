from typing import List
import uuid
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate,UserDelete,UserUpdate,UserResponse
from fastapi import HTTPException,status
from app.core.security import get_password_hash,verify_password

# Fonction pour récupérer un utilisateur par email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email, User.is_deleted == False).first()

# Fonction pour récupérer un utilisateur par numéro de téléphone
def get_user_by_phone_number(db: Session, phone_number: str):
    return db.query(User).filter(User.phone_number == phone_number, User.is_deleted == False).first()

# Fonction pour récupérer un utilisateur par UUID
def get_user_by_uuid(db: Session, uuid: str):
    return db.query(User).filter(User.uuid == uuid, User.is_deleted == False).first()

# Fonction pour récupérer une liste d'utilisateurs à partir d'une liste de UUIDs
def get_user_by_list_uuids(db: Session, uuids: List[str]):
    return db.query(User).filter(User.uuid.in_(uuids), User.is_deleted == False).all()

# Fonction pour créer un utilisateur
def create_user(db: Session, obj_in: UserCreate):
    # Vérifier si l'email existe déjà
    exist_email = get_user_by_email(db, email=obj_in.email)
    if exist_email is not None: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This email already exists")

    # Vérifier si le numéro de téléphone existe déjà
    exist_phone_number = get_user_by_phone_number(db, phone_number=obj_in.phone_number)
    if exist_phone_number is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This phone number already exists")
    
    # Hasher le mot de passe
    hashed_password = get_password_hash(obj_in.hashed_password)

    # Créer un nouvel utilisateur
    new_user = User(
        uuid=str(uuid.uuid4()),  # Générer un UUID unique
        username=obj_in.username,
        email=obj_in.email,
        phone_number=obj_in.phone_number,
        hashed_password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Rafraîchir pour obtenir l'objet mis à jour
    return new_user


def update_user(db:Session,obj_in:UserUpdate):
    user = get_user_by_uuid(db, uuid=obj_in.uuid)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    user.username = obj_in.username if obj_in.username else user.username
    user.email = obj_in.email if obj_in.email else user.email
    user.phone_number = obj_in.phone_number if obj_in.phone_number else user.phone_number
    db.commit()
    db.refresh(user)
    return user

# Fonction pour supprimer un utilisateur (soft delete)
def delete_user(db: Session, uuid: str):
    user = get_user_by_uuid(db, uuid=uuid)
    if user is None:  # Correction de la condition
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user.is_deleted = True  # Marquer comme supprimé au lieu de supprimer physiquement
    db.commit()
    
# Activer un utilisateur
def activate_user(db: Session, uuid: str):
    user = get_user_by_uuid(db, uuid=uuid)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.is_active = True
    db.commit()
    return {"message": "User activated successfully"}

# Désactiver un utilisateur
def deactivate_user(db: Session, uuid: str):
    user = get_user_by_uuid(db, uuid=uuid)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.is_active = False
    db.commit()
    return {"message": "User deactivated successfully"}

# Supprimer une liste d'utilisateurs (soft delete)
def delete_user_by_list(db: Session, uuids: List[str]):
    users = get_user_by_list_uuids(db, uuids)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
    for user in users:
        user.is_deleted = True
    db.commit()
    return len(users)

# Activer une liste d'utilisateurs
def activate_user_by_list(db: Session, uuids: List[str]):
    users = get_user_by_list_uuids(db, uuids)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
    for user in users:
        user.is_active = True
    db.commit()
    return len(users)

# Désactiver une liste d'utilisateurs
def deactivate_user_by_list(db: Session, uuids: List[str]):
    users = get_user_by_list_uuids(db, uuids)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
    for user in users:
        user.is_active = False
    db.commit()
    return len(users)

def authenticate(db:Session,email:str,password:str):
    db_obj = db.query(User).filter(User.email==email,User.is_deleted==False).first()
    if not db_obj:
        return None
    if not verify_password(password,db_obj.hashed_password):
        return None
    return db_obj