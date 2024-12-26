from XpenseMeter.db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email: Column[str] = Column(String, unique=True, index=True)
    password = Column(String)
    preferences = Column(String)
    expenses = relationship("Expense", back_populates="user")