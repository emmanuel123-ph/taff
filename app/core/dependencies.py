from typing import Generator, Optional

from fastapi import Depends, Query
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, BackgroundTasks

from app import schemas, models, crud
from app.core.i18n import __
from app.core.security import decode_access_token
from app.models.db.session import SessionLocal

# def get_db(request: Request) -> Generator:
#     return request.state.db
def get_db():
    db = SessionLocal()  # Crée une session de base de données
    try:
        yield db  # Utilise la session et permet sa gestion automatique
    finally:
        db.close()  # Ferme la session après utilisation


# class TokenRequired(HTTPBearer):

#     def __init__(self, token: Optional[str] = Query(None), roles=None, auto_error: bool = True):
#         if roles is None:
#             roles = []
#         self.roles = roles
#         self.token = token
#         super(TokenRequired, self).__init__(auto_error=auto_error)

#     async def __call__(self, request: Request, db: Session = Depends(get_db)):
#         required_roles = self.roles
#         credentials: HTTPAuthorizationCredentials = await super(TokenRequired, self).__call__(request)

#         if not credentials and self.token:
#             credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=self.token)

#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code=403, detail=__("dependencies-token-invalid"))
#             token_data = decode_access_token(credentials.credentials)
#             if not token_data:
#                 raise HTTPException(status_code=403, detail=__("dependencies-token-invalid"))

#             if models.BlacklistToken.check_blacklist(db, credentials.credentials):
#                 raise HTTPException(status_code=403, detail=__("dependencies-token-invalid"))

#             current_user = crud.user.get_by_uuid(db=db, uuid=token_data["sub"])
#             if not current_user:
#                 raise HTTPException(status_code=403, detail=__("dependencies-token-invalid"))

#             """
#             if required_roles:
#                 if current_user.role_uuid not in required_roles:
#                     raise HTTPException(status_code=403, detail=__("dependencies-access-unauthorized"))
#             """

#             return current_user
#         else:
#             raise HTTPException(status_code=403, detail=__("dependencies-access-unauthorized"))
#         db.close()
