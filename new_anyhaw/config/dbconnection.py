import mysql.connector
from mysql.connector import Error
from config import settings  # Import settings to use environment variables

# Function to create database connection using settings from settings.py
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=settings.DB_CONFIG["host"],
            user=settings.DB_CONFIG["user"],
            password=settings.DB_CONFIG["password"],
            database=settings.DB_CONFIG["database"],
            port=settings.DB_CONFIG["port"]
        )
        if connection.is_connected():
            print("✅ Connected to 'anyhaw' database using hardcoded settings")
            return connection
    except Error as err:
        print(f"❌ Connection error: {err}")
    return None

# Function to get a database connection using environment variables (from settings.py)
def get_db_connection():
    try:
        print(f"Connecting to DB with host={settings.DB_CONFIG['host']}, "
              f"user={settings.DB_CONFIG['user']}, "
              f"database={settings.DB_CONFIG['database']}, "
              f"port={settings.DB_CONFIG['port']}")
              
        connection = mysql.connector.connect(
            host=settings.DB_CONFIG["host"],
            user=settings.DB_CONFIG["user"],
            password=settings.DB_CONFIG["password"],
            database=settings.DB_CONFIG["database"],
            port=settings.DB_CONFIG["port"]
        )
        if connection.is_connected():
            print("✅ Successfully connected to the database.")
            return connection
    except Error as err:
        print(f"❌ Database connection failed: {err}")
        return None
