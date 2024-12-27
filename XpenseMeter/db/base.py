from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from XpenseMeter.db.models.user import User
from XpenseMeter.db.models.expense import Expense
from XpenseMeter.db.models.category import Category
from XpenseMeter.db.models.budget import Budget