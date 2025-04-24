import os
from dotenv import load_dotenv
from pathlib import Path

# Load from .env
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# Required Vars (will raise if missing)
QBO_CLIENT_ID = os.getenv("QBO_CLIENT_ID")
QBO_CLIENT_SECRET = os.getenv("QBO_CLIENT_SECRET")
QBO_REDIRECT_URI = os.getenv("QBO_REDIRECT_URI")
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

# Optional or Defaulted Vars
QBO_REALM_ID = os.getenv("QBO_REALM_ID", "000000000000000")
TOKEN_STORAGE_PATH = os.getenv("TOKEN_STORAGE_PATH", "./tokens")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "user": os.getenv("DB_USER", "pulseuser"),
    "password": os.getenv("DB_PASS", "changeme"),
    "database": os.getenv("DB_NAME", "pulsedb"),
}

# Risk thresholds (configurable per install or client)
RISK_LATE_INVOICE_DAYS = int(os.getenv("RISK_LATE_INVOICE_DAYS", 30))
RISK_VENDOR_ALERT_AMOUNT = float(os.getenv("RISK_VENDOR_ALERT_AMOUNT", 5000.00))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

# Cron
SYNC_INTERVAL_CRON = os.getenv("SYNC_INTERVAL_CRON", "0 3 * * 1")  # Every Monday at 3am

# Safety check
REQUIRED_ENV_VARS = [QBO_CLIENT_ID, QBO_CLIENT_SECRET, QBO_REDIRECT_URI, APP_SECRET_KEY]
if any(v is None for v in REQUIRED_ENV_VARS):
    raise EnvironmentError("Missing required environment variables in .env file.")
