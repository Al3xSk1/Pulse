# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import config

# --------------------------------------------
# Database URL Format
# --------------------------------------------
DATABASE_URL = (
    f"postgresql://{config.DB_CONFIG['user']}:"
    f"{config.DB_CONFIG['password']}@"
    f"{config.DB_CONFIG['host']}:"
    f"{config.DB_CONFIG['port']}/"
    f"{config.DB_CONFIG['database']}"
)

# --------------------------------------------
# SQLAlchemy Engine, Session, and Base
# --------------------------------------------
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# --------------------------------------------
# Dependency to Get a DB Session in FastAPI
# --------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
