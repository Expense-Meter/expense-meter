from XpenseMeter.db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))