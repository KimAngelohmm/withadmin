from flask import jsonify
from config.dbconnection import create_connection
import uuid

def guest_login():
    guest_id = str(uuid.uuid4())
    guest_email = f"guest_{guest_id}@anyhaw.com"

    conn = create_connection()
    if not conn:
        return jsonify({"message": "Database connection failed"}), 500

    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password, role) VALUES (%s, %s, %s)", 
                   (guest_email, "", "guest"))
    conn.commit()
    conn.close()
    return jsonify({"message": "Guest account created", "guest_email": guest_email}), 201
