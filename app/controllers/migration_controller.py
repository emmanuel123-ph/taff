import os
import shutil
import platform
from dataclasses import dataclass

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Column, String
from app import schemas
from app.core.config import Config
from app.core import dependencies
from app.models.db.base_class import Base
from app.utils import logger
import subprocess
import logging
import traceback

router = APIRouter(prefix="/migrations", tags=["migrations"])


def check_user_access_key(admin_key: schemas.AdminKey):
    logger.info(f"Check user access key: {admin_key.key}")
    if admin_key.key not in [Config.ADMIN_KEY]:
        raise HTTPException(status_code=400, detail="Clé d'accès incorrecte")


@router.post("/create-database-tables", response_model=schemas.Msg, status_code=201)
def create_database_tables(
    db: Session = Depends(dependencies.get_db),
    admin_key: schemas.AdminKey = Body(...)
) -> dict[str, str]:
    """
    Create database structure (tables)
    """
    check_user_access_key(admin_key)
    """ Try to remove previous alembic tags in database """
    try:
        @dataclass
        class AlembicVersion(Base):
            __tablename__ = "alembic_version"
            version_num: str = Column(String(32), primary_key=True, unique=True)

        db.query(AlembicVersion).delete()
        db.commit()
    except Exception as e:
        pass

    """ Try to remove previous alembic versions folder """
    migrations_folder = os.path.join(os.getcwd(), "alembic", "versions")
    try:
        shutil.rmtree(migrations_folder)
    except Exception as e:
        pass

    """ create alembic versions folder content """
    try:
        os.mkdir(migrations_folder)
    except OSError:
        logger.error("Creation of the directory %s failed" % migrations_folder)
    else:
        logger.info("Successfully created the directory %s " % migrations_folder)

    try:
        # Get the environment system
        if platform.system() == 'Windows':
            # Windows-specific command
            os.system('.\\venv\\Scripts\\python.exe .\\venv\\Scripts\\alembic.exe revision --autogenerate')
        else:
            # Unix-like system command
            os.system('PYTHONPATH=. alembic revision --autogenerate')

        # Get the environment system
        if platform.system() == 'Windows':
            # Windows-specific command
            os.system('.\\venv\\Scripts\\python.exe .\\venv\\Scripts\\alembic.exe upgrade head')
        else:
            # Unix-like system command
            os.system('PYTHONPATH=. alembic upgrade head')

        """ Try to remove previous alembic versions folder """
        try:
            shutil.rmtree(migrations_folder)
        except Exception as e:
            pass

        return {"message": "Les tables de base de données ont été créées avec succès"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
