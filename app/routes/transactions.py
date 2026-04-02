from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.databases import SessionLocal
from app import schemas, crud, models
from app.dependencies import get_current_role, check_permission

router = APIRouter(tags=["Transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transactions")
def create_txn(txn: schemas.TransactionCreate, db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "write")
    return crud.create_transaction(db, txn)

@router.get("/transactions")
def get_txns(db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "read")
    return crud.get_all_transactions(db)

@router.put("/transactions/{id}")
def update_txn(id: int, txn: schemas.TransactionCreate, db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "write")

    db_txn = crud.get_transaction(db, id)
    if not db_txn:
        raise HTTPException(status_code=404, detail="Not found")

    for key, value in txn.dict().items():
        setattr(db_txn, key, value)

    db.commit()
    db.refresh(db_txn)
    return db_txn

@router.delete("/transactions/{id}")
def delete_txn(id: int, db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "write")
    txn = crud.delete_transaction(db, id)
    if not txn:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Deleted"}

@router.get("/transactions/filter")
def filter_txn(type: str = None, category: str = None, db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "read")

    query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)
    if category:
        query = query.filter(models.Transaction.category == category)

    return query.all()

@router.get("/transactions/paginated")
def paginate(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), role: str = Depends(get_current_role)):
    check_permission(role, "read")
    return db.query(models.Transaction).offset(skip).limit(limit).all()