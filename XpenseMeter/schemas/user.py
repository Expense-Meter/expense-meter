from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    """
    Shared properties for reading and updating a user.
    """
    email: EmailStr
    preferences: Optional[str] = None

class UserCreate(UserBase):
    """
    Properties required to create a new user.
    """
    password: str

class UserUpdate(UserBase):
    """
    Properties that can be updated for a user.
    """
    password: Optional[str] = None

class UserInDBBase(UserBase):
    """
    Properties shared by models stored in DB.
    """
    id: int

    class Config:
        from_attributes = True

class User(UserInDBBase):
    """
    Properties to return to client.
    """
    pass

class UserInDB(UserInDBBase):
    """
    Properties stored in DB.
    """
    hashed_password: str

class UserSignIn(BaseModel):
    """
    Properties required to sign in a user.
    """
    email: EmailStr
    password: str

class Token(BaseModel):
    """
    Properties of a JWT token.
    """
    access_token: str
    token_type: str
    refresh_token: str

class TokenData(BaseModel):
    """
    Properties of a JWT token.
    """
    email: str | None = None