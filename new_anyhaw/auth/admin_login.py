from flask import request, jsonify
from config.dbconnection import get_db_connection
import bcrypt

def init_admin_login_routes(app):
    @app.route('/admin/login', methods=['POST'])
    def admin_login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password are required."}), 400

        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor(dictionary=True)

        try:
            query = "SELECT * FROM main_accounts WHERE email = %s AND account_type = 'Admin'"
            cursor.execute(query, (email,))
            admin = cursor.fetchone()

            if not admin:
                return jsonify({"error": "Admin account not found."}), 404

            if bcrypt.checkpw(password.encode('utf-8'), admin['password'].encode('utf-8')):
                return jsonify({
                    "message": "Admin login successful.",
                    "admin_id": admin['account_id'],
                    "email": admin['email'],
                    "username": admin['username']
                }), 200
            else:
                return jsonify({"error": "Incorrect password."}), 401

        except Exception as e:
            return jsonify({"error": f"Login failed: {str(e)}"}), 500

        finally:
            cursor.close()
            conn.close()
