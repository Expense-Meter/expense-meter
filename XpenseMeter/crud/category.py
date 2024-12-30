from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
from typing import Tuple
from XpenseMeter.db.models import Category, Budget, Expense


def get_category(db: Session, category_name: str, user_id: str):
    return db.query(Category).filter(Category.name == category_name, Category.user_id == user_id).first()

def add_category(db: Session, category_name: str, user_id: str):
    new_category = Category(name=category_name, user_id=user_id)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_category_limit_status(db: Session, user_id: int, category_id: int, category_name: str) -> Tuple[float, float]:
    budget_obj = db.query(Budget).filter(Budget.user_id == user_id, Budget.category == category_id).first()
    category_monthly_limit = budget_obj.monthly_limit

    current_date = datetime.now().date()
    first_date = datetime(current_date.year, current_date.month, 1).date()

    category_total_amount_spent = db.query(func.sum(Expense.amount)).filter(
        Expense.user_id == user_id,
        Expense.category == category_name,
        Expense.date >= first_date,
        Expense.date <= current_date
    ).scalar()
    return (category_monthly_limit, category_total_amount_spent)