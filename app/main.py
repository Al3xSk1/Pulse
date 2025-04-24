# app/main.py

from fastapi import FastAPI
from app.db import Base, engine
from app.api.routes import router as api_router

# --------------------------------------
# Initialize FastAPI app
# --------------------------------------
app = FastAPI(
    title="Pulse API",
    description="Financial analytics and risk detection system for QBO data",
    version="0.1.0",
)

# --------------------------------------
# Create all tables (in dev, not for prod)
# --------------------------------------
Base.metadata.create_all(bind=engine)

# --------------------------------------
# Include route modules
# --------------------------------------
app.include_router(api_router)
