import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

# ------------------------------
# ENVIRONMENT SETUP
# ------------------------------
ENV = os.environ.get("FLASK_ENV", "development")  # "production" or "development"
DEBUG = ENV == "development"

# ------------------------------
# SECRET KEY & SECURITY
# ------------------------------
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "your-super-secret-key")
BCRYPT_LOG_ROUNDS = 12  # For password hashing

# ------------------------------
# DATABASE CONFIGURATION
# ------------------------------
DB_CONFIG = {
    "host": os.environ.get("MYSQL_HOST", "localhost"),
    "user": os.environ.get("MYSQL_USER", "your_mysql_user"),
    "password": os.environ.get("MYSQL_PASSWORD", "your_mysql_password"),
    "database": os.environ.get("MYSQL_DATABASE", "anyhaw"),
    "port": int(os.environ.get("MYSQL_PORT", 3306))
}

# ------------------------------
# CORS CONFIGURATION
# ------------------------------
CORS_ORIGINS = [
    "http://localhost:3000",     # Local frontend
    "http://127.0.0.1:3000"
]
CORS_SUPPORTS_CREDENTIALS = True

# ------------------------------
# SESSION SETTINGS (optional)
# ------------------------------
SESSION_TYPE = "filesystem"
PERMANENT_SESSION_LIFETIME = timedelta(hours=5)

# ------------------------------
# FILE UPLOADS / IMAGE STORAGE
# ------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'assets', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# ------------------------------
# APPLICATION CONSTANTS
# ------------------------------
ACCOUNT_TYPES = ['Admin', 'Staff', 'Cashier', 'Kitchen', 'Delivery']
AVAILABILITY_STATUSES = ['Available', 'On Break', 'Not Available']

# ------------------------------
# EMAIL SETTINGS (optional)
# ------------------------------
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USERNAME = os.environ.get("EMAIL_USER", "your_email@example.com")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS", "your_email_password")
DEFAULT_FROM_EMAIL = EMAIL_USERNAME
