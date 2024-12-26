from XpenseMeter.db.base import Base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship


class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    category = Column(String)
    date = Column(Date)
    description = Column(String)
    user = relationship("User", back_populates="expenses")