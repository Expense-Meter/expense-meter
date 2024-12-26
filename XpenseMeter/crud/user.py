from fastapi import Depends
from sqlalchemy.orm import Session
from XpenseMeter.db.models import User
from XpenseMeter.schemas import UserCreate
from XpenseMeter.core.security import get_password_hash


def get_users(db: Session):
    """
    Retrieve all users.

    Args:
        db (Session): SQLAlchemy session object.
    
    Returns:
        List[User]: List of User objects
    """
    expenses = db.query(User).all()
    return expenses

def get_user_by_email(db: Session, email: str):
    """
    Retrieve user by email.

    Args:
        db (Session): SQLAlchemy session object.
        email (str): Email of the user to retrieve.
    
    Returns:
        User: User object with the specified email.
    """
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_in: UserCreate) -> User:
    """
    Create a new user in the database.

    Args:
        db (Session): SQLAlchemy database session.
        user_in (UserCreate): Pydantic model with user creation data.

    Returns:
        User: The created User object.
    """
    hashed_password = get_password_hash(user_in.password)
    db_user = User(
        email=user_in.email,
        hashed_password=hashed_password,
        preferences=user_in.preferences
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user