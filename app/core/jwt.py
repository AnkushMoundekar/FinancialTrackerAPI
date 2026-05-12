from datetime import datetime, timedelta
from jose import jwt, JWTError
import secrets
from fastapi import HTTPException

from app.core.config import settings

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def generate_refresh_token():
    return secrets.token_urlsafe(32)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")