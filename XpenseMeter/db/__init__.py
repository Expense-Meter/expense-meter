from XpenseMeter.db.session import engine
from XpenseMeter.db.base import Base
from .models import *

Base.metadata.create_all(bind=engine)