from fastapi import FastAPI
from app import config

print(config.DB_CONFIG["host"])
print(config.QBO_CLIENT_ID)

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Pulse backend is live (WIP)"}
