from typing import Generator, Optional

from fastapi import Depends, Query
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, BackgroundTasks

from app import schemas, models, crud
from app.core.i18n import __
from app.core.security import decode_access_token


def get_db(request: Request) -> Generator:
    return request.state.db

