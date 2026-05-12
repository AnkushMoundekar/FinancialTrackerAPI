from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import register_user
from app.dependencies.db import get_db

router = APIRouter()

@router.post("/register", response_model= UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user.email, user.password)