# app/models/client.py

from sqlalchemy import Column, Integer, String
from app.db import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    realm_id = Column(String, unique=True, nullable=False)
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=False)

    # Optional extras
    contact_email = Column(String, nullable=True)
    notes = Column(String, nullable=True)
