from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta, timezone

from app.repositories.user_repository import get_user_by_email
from app.repositories.token_repository import get_refresh_token, revoke_refresh_token, create_refresh_token as create_refresh_token_record

from app.core.security import verify_password, hash_token
from app.core.jwt import create_access_token, generate_refresh_token

def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=400, detail=f"user with email {email} does not exist")
    
    if not verify_password(password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentails")
    
    #access token
    access_token = create_access_token({"sub":str(user.id)})

    #refresh token
    raw_refresh_token = generate_refresh_token()
    
    hashed_token = hash_token(raw_refresh_token)

    expires_at = datetime.now() + timedelta(days=7)

    create_refresh_token_record(db, user.id, hashed_token, expires_at)

    return access_token, raw_refresh_token


def refresh_access_token(db: Session, refresh_token: str):

    hashed_token = hash_token(refresh_token)

    token_record = get_refresh_token(db, hashed_token)

    if not token_record:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    if token_record.expires_at < datetime.now():
        raise HTTPException(status_code=401, detail="Refresh token expired")
    
    user_id = token_record.user_id

    access_token = create_access_token({"sub": str(user_id)})

    return access_token

def logout_user(db: Session, refresh_token: str):

    hashed_token = hash_token(refresh_token)
    revoke_refresh_token(db, hashed_token)
    