from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from XpenseMeter import schemas, crud
from XpenseMeter.db.session import get_db
from XpenseMeter.core.security import verify_password, create_access_token, create_refresh_token
from XpenseMeter.decorators.jwt import token_authentication_required

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
@token_authentication_required
def read_users(db: Session = Depends(get_db)):
    """
    Retrieve all users.
    """
    users = crud.get_users(db)
    return users

@router.post("/sign-up", response_model=schemas.User)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    user = crud.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    user = crud.create_user(db=db, user_in=user_in)
    return user

@router.post("/sign-in", response_model=schemas.Token)
def sign_in(user_data: schemas.UserSignIn, db: Session = Depends(get_db)):
    """
    Sign in a user.
    """
    user = crud.get_user_by_email(db, email=user_data.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    access_token = create_access_token(data={"email": user.email})
    refresh_token = create_refresh_token(data={"email": user.email})
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}