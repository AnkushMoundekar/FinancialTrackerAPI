from sqlalchemy import Column, Integer, Boolean, DateTime, String, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func

from app.db.base import Base

class Category(Base):
    __tablename__="categories"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    is_deleted = Column(Boolean, default=False)

    __table_args__ = (
        UniqueConstraint("user_id", "name", "is_deleted", name="unique_user_category_name"),
    )