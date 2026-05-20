from sqlalchemy.orm import Session
from sqlalchemy import func, case

from app.models.expense import Expense
from app.models.category import Category

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
        end_date = None,
        category_id = None
        ):
    query = db.query(Expense).filter(
        Expense.user_id == user_id,
        Expense.is_deleted == False
    )
    if category_id:
        query = query.filter(Expense.category_id == category_id)
    if type:
        query = query.filter(Expense.type == type)
    if start_date:
        query = query.filter(Expense.transaction_date >= start_date)
    if end_date:
        query = query.filter(Expense.transaction_date <= end_date)

    return query.offset(offset).limit(limit).all()

def get_expense_summary(db, user_id):
    # SELECT 
    #     SUM(CASE WHEN expense.type = 'expense' THEN expense.amount ELSE 0 END) AS total_expense,
    #     SUM(CASE WHEN expense.type = 'income' THEN expense.amount ELSE 0 END) AS total_income
    # FROM expense
    # WHERE expense.user_id = :user_id 
    # AND expense.is_deleted = false
    # LIMIT 1;
    result = db.query(
        func.sum(
            case((Expense.type == "expense", Expense.amount), else_=0)
        ).label("total_expense"),
        
        func.sum(
            case((Expense.type == "income", Expense.amount), else_= 0)
        ).label("total_income")
    ).filter(
        Expense.user_id == user_id,
        Expense.is_deleted == False
    ).first()
    return {"total_expense": result.total_expense,
            "total_income": result.total_income}



def get_category_summary(db, user_id):
    # SELECT 
    #     COALESCE(category.name, 'Uncategorized') AS category,
    #     SUM(expense.amount) AS total
    # FROM expense
    # LEFT OUTER JOIN category ON expense.category_id = category.id
    # WHERE expense.user_id = :user_id 
    # AND expense.is_deleted = false
    # GROUP BY COALESCE(category.name, 'Uncategorized');
    result = db.query(
        func.coalesce(Category.name, "Uncategorized").label("category"),
        func.sum(Expense.amount).label("total")
    ).outerjoin(
        Category, Expense.category_id == Category.id
    ).filter(
        Expense.user_id == user_id,
        Expense.is_deleted == False
    ).group_by(
        func.coalesce(Category.name, "Uncategorized")
    ).all()

    return result



