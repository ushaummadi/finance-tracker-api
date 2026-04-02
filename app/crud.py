from sqlalchemy.orm import Session
from app import models

def create_transaction(db: Session, data):
    txn = models.Transaction(**data.dict())
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn

def get_all_transactions(db: Session):
    return db.query(models.Transaction).all()

def get_transaction(db: Session, id: int):
    return db.query(models.Transaction).filter(models.Transaction.id == id).first()

def delete_transaction(db: Session, id: int):
    txn = get_transaction(db, id)
    if txn:
        db.delete(txn)
        db.commit()
    return txn