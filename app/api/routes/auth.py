from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import login_user, refresh_access_token, logout_user
from app.dependencies.db import get_db

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    access_token, refresh_token = login_user(db, data.email, data.password)

    return{
        "access_token": access_token,
        "refresh_token": refresh_token
    }
@router.post("/refresh")
def refresh_token(refresh_token: str, db: Session=Depends(get_db)):
    access_token = refresh_access_token(db, refresh_token)
    return{"access_token": access_token}

@router.post("/logout")
def logout(refresh_token: str, db: Session= Depends(get_db)):
    logout_user(db, refresh_token)
    return{"message": "user logout successfully "}