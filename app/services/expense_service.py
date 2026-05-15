from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.repositories.expense_repository import create_expense, get_user_expenses

def create_user_expense(db: Session, user_id: int, data):
    expense = Expense(
        user_id = user_id,
        amount = data.amount,
        type = data.type,
        description = data.description,
        transaction_date = data.transaction_date
    )

    return create_expense(db, expense)

def list_user_expense(
        db: Session, 
        user_id: int,
        limit: int,
        offset: int,
        type = None,
        start_date = None,
        end_date = None
        ):
    return get_user_expenses(db, user_id, limit, offset, type, start_date, end_date)