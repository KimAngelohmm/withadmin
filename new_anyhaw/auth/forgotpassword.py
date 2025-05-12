from flask import request, jsonify
from config.dbconnection import create_connection
import bcrypt

def forgot_password():
    data = request.json
    email = data.get("email")
    new_password = data.get("new_password")

    conn = create_connection()
    if not conn:
        return jsonify({"message": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"message": "Email not found"}), 404

    hashed = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())
    cursor.execute("UPDATE users SET password = %s WHERE email = %s", (hashed.decode("utf-8"), email))
    conn.commit()
    conn.close()
    return jsonify({"message": "Password updated successfully"}), 200
