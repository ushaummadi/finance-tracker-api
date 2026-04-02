from fastapi import APIRouter
from app.auth import create_token
from app.schemas import UserLogin

router = APIRouter(tags=["Auth"])

@router.post("/login")
def login(user: UserLogin):
    return {
        "access_token": create_token({
            "username": user.username,
            "role": user.role
        })
    }