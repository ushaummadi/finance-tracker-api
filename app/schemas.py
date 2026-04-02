from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: Optional[str] = None

class TransactionOut(TransactionCreate):
    id: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    role: str