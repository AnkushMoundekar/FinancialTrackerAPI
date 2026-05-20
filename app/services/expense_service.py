from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import timedelta

from app.models.expense import Expense
from app.repositories.expense_repository import create_expense, get_user_expenses, get_expense_summary, get_category_summary, get_monthly_summary
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

def get_monthly_summary_service(db, user_id, from_date = None, to_date = None):
    result = get_monthly_summary(db, user_id, from_date, to_date)
    data_map = {
        row.month.date(): float(row.total or 0)
    for row in result}

    start_date = from_date.date() if from_date else min(data_map.keys())
    end_date = to_date.date() if to_date else max(data_map.keys())

    # Normalize dates to the 1st day of the month to match database format
    current_month = start_date.replace(day=1)
    target_end = end_date.replace(day=1)

    
    final_summary = []
    while current_month <= target_end:
        # Fetch the total if it exists, otherwise fall back to 0.0
        total_amount = data_map.get(current_month, 0.0)
        
        final_summary.append({
            "month": current_month.strftime("%Y-%m"),
            "total": total_amount
        })
        
        next_month_somewhere = current_month + timedelta(days=32)
        current_month = next_month_somewhere.replace(day=1)

    return final_summary

    