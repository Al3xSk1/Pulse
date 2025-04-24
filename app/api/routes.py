# app/api/routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.client import Client

router = APIRouter()

@router.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()
