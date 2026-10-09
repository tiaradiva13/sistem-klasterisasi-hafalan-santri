
from fastapi import APIRouter

router=APIRouter(prefix="/hafalan")
items=[]

@router.get("/")
def get_all():
    return items

@router.post("/")
def create(data:dict):
    items.append(data)
    return data
