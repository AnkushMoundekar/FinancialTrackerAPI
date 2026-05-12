from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.user_repository import create_user, get_user_by_email
from app.core.security import hash_password

def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)
    hash = hash_password(password)
    if existing_user:
        raise HTTPException(status_code= 400, detail="email already exist")
    
    user = create_user(db, email, hash)
    return user