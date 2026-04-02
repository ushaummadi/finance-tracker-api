from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.databases import SessionLocal
from app.models import Transaction
from app.dependencies import get_current_role, check_permission

router = APIRouter(tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/analytics/summary")
def summary(db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "analytics")

    income = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "income").scalar() or 0
    expense = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "expense").scalar() or 0

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }

@router.get("/analytics/category")
def category(db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "analytics")

    data = db.query(Transaction.category, func.sum(Transaction.amount)).group_by(Transaction.category).all()
    return {c: amt for c, amt in data}

@router.get("/analytics/monthly")
def monthly(db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "analytics")

    data = db.query(
        extract('month', Transaction.date),
        func.sum(Transaction.amount)
    ).group_by(extract('month', Transaction.date)).all()

    return {f"Month {int(m)}": total for m, total in data}