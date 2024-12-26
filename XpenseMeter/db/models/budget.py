from XpenseMeter.db.base import Base
from sqlalchemy import Column, Integer, Float, ForeignKey


class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(Integer, ForeignKey('categories.id'))
    monthly_limit = Column(Float)