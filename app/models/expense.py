from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Numeric
from sqlalchemy.sql import func

from app.db.base import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    user_id =  Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, nullable=True)

    amount = Column(Numeric(10,2), nullable=False)
    type = Column(String, nullable=False) #income/expense

    description = Column(String, nullable=True)

    transaction_date = Column(DateTime, nullable=False)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)

