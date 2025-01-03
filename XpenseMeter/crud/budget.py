from sqlalchemy.orm import Session
from XpenseMeter.db.models import Budget


def add_budget(db: Session, user_id: int, category_id: int, monthly_limit: float):
    new_budget = Budget(
        category=category_id,
        user_id=user_id,
        monthly_limit=monthly_limit
    )
    db.add(new_budget)
    db.commit()
    return new_budget