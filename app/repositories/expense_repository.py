from sqlalchemy.orm import Session

from app.models.expense import Expense

def create_expense(db: Session, expense: Expense):
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_user_expenses(
        db: Session, 
        user_id: int,
        limit: int,
        offset: int,
        type: str|None = None,
        start_date = None,
        end_date = None
        ):
    query = db.query(Expense).filter(
        Expense.user_id == user_id,
        Expense.is_deleted == False
    )

    if type:
        query = query.filter(Expense.type == type)
    if start_date:
        query = query.filter(Expense.transaction_date >= start_date)
    if end_date:
        query = query.filter(Expense.transaction_date <= end_date)

    return query.offset(offset).limit(limit).all()

