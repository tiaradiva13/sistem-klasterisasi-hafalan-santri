
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import hash_password,create_token

router=APIRouter(prefix="/auth")

class Auth(BaseModel):
    email:str
    password:str

@router.post("/register")
def register(data:Auth):
    return {"email":data.email,"password_hash":hash_password(data.password)}

@router.post("/login")
def login(data:Auth):
    return {"access_token":create_token({"sub":data.email})}
