# app/routes/user.py

from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.post("/users/")
async def create_user(user: User):
    # Logic to save user to database
    return {"message": "User created successfully"}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    # Logic to retrieve user from database by ID
    return {"id": user_id, "username": "example_user"}
