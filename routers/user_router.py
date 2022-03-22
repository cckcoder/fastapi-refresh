from typing import List, Optional
from fastapi import APIRouter, Depends

from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from auth.oauth2 import oauth2_scheme


router = APIRouter(prefix="/user", tags=["user"])

# Create user
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db_user.get_all_users(db)


@router.get("/{id}", response_model=UserDisplay)
def get_users(id: int, db: Session = Depends(get_db)):
    return db_user.get_users(db, id)


# Update user
@router.put("/{id}/update")
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_users(db, id, request)


# Delete user
@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
