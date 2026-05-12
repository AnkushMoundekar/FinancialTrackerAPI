from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.jwt import decode_access_token
from app.dependencies.db import get_db
from app.models.user import User

security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session= Depends(get_db)
):
    token = credentials.credentials

    user_id = decode_access_token(token)

    user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()

    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="user not found")
    
    return user