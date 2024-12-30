from sqlalchemy.orm import Session
from datetime import datetime
from XpenseMeter.db.models import Expense
from XpenseMeter.schemas import ExpenseCreate


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

def add_expense(db: Session, expense_in: ExpenseCreate, user_id: str):
    """
    Add a new expense to the database.

    Args:
        db (Session): SQLAlchemy database session.
        expense_in (ExpenseCreate): Pydantic model with expense creation data.
        user_id (str): User ID of the user adding the expense.
    
    Returns:
        Expense: The created Expense object.
    """
    new_expense = Expense(
        user_id=user_id,
        amount=expense_in.amount,
        category=expense_in.category,
        description=expense_in.description,
        date=datetime.now()
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense