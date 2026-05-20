from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.expense import Expense
from app.repositories.expense_repository import create_expense, get_user_expenses, get_expense_summary, get_category_summary
from app.repositories.category_repository import get_category_by_id

def create_user_expense(db: Session, user_id: int, data):

    if data.category_id:
        category = get_category_by_id(db, data.category_id)
        
        if not category:
            raise HTTPException(status_code=401, detail="category not exist")
        
        if category.user_id is not None and category.user_id != user_id:
            raise HTTPException(status_code=401, detail="Not allowed to use this category")

    expense = Expense(
        user_id = user_id,
        amount = data.amount,
        type = data.type,
        description = data.description,
        transaction_date = data.transaction_date,
        category_id = data.category_id
    )

    return create_expense(db, expense)

def list_user_expense(
        db: Session, 
        user_id: int,
        limit: int,
        offset: int,
        type = None,
        category_id = None,
        start_date = None,
        end_date = None
        ):
    return get_user_expenses(db, user_id, limit, offset, type, start_date, end_date, category_id)

def get_expense_summary_service(db, user_id):
    return get_expense_summary(db, user_id)

def get_category_summary_service(db, user_id):
    result = get_category_summary(db, user_id)
    return [
        {
            "category": r.category,
            "total": float(r.total or 0)
        }
        for r in result
    ]