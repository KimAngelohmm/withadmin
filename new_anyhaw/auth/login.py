from flask import request, jsonify
from config.dbconnection import create_connection
import bcrypt

def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = create_connection()
    if not conn:
        return jsonify({"message": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
        return jsonify({"message": "Login successful", "user": {"email": user["email"], "role": user["role"]}}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401
