from sqlalchemy.orm import Session
from datetime import datetime
from XpenseMeter.db.models import Expense


def get_current_month_expenses(db: Session, user_id: str):
    """
    Retrieve all expenses for a user.

    Args:
        db (Session): SQLAlchemy session object.
        user_id (str): User ID of the user to retrieve expenses for.
    
    Returns:
        List[Expense]: List of Expense objects
    """
    current_date = datetime.now().date()
    first_date = datetime(current_date.year, current_date.month, 1).date()
    return db.query(Expense).filter(Expense.user_id == user_id, Expense.date >= first_date, Expense.date <= current_date).all()