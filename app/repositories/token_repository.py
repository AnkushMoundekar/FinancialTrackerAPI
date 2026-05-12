from sqlalchemy.orm import Session

from app.models.refresh_token import RefreshToken

def create_refresh_token(db: Session, user_id: int, hashed_token: str, expires_at):
    token = RefreshToken(
        user_id=user_id,
        hashed_token=hashed_token,
        expires_at=expires_at
    )
    db.add(token)
    db.commit()
    db.refresh(token)

    return token

def get_refresh_token(db:Session, hashed_token: str):
    return db.query(RefreshToken).filter(
        RefreshToken.hashed_token == hashed_token,
        RefreshToken.is_revoked == False
    ).first()

def revoke_refresh_token(db: Session, hashed_token: str):
    token = db.query(RefreshToken).filter(
        RefreshToken.hashed_token == hashed_token,
        RefreshToken.is_revoked == False
    ).first()

    if token:
        token.is_revoked = True
        db.commit()
    
