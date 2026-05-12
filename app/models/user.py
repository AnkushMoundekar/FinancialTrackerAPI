from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from datetime import datetime, timezone

from app.db.base import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    role = Column(String, default="user")

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean,  default=False)
    is_deleted = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())

    deleted_at = Column(DateTime, nullable=True)
    last_login_at = Column(DateTime, nullable=True)