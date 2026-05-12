from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime, timezone

from app.db.base import Base

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    hashed_token = Column(String, nullable=False)

    is_revoked = Column(Boolean, default=False)

    expires_at = Column(DateTime)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))

