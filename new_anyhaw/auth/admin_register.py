from flask import request, jsonify
from config.dbconnection import get_db_connection
import bcrypt

def init_admin_register_routes(app):
    @app.route('/admin/register', methods=['POST'])
    def admin_register():
        data = request.get_json()

        first_name = data.get('first_name')
        middle_name = data.get('middle_name', '')
        last_name = data.get('last_name')
        contact_number = data.get('contact_number')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        position_id = data.get('position_id')

        if not all([first_name, last_name, contact_number, email, username, password, position_id]):
            return jsonify({"error": "Missing required fields."}), 400

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor(dictionary=True)

        try:
            # Check if position ID exists
            cursor.execute("SELECT * FROM Position_List WHERE Position_ID = %s", (position_id,))
            if not cursor.fetchone():
                return jsonify({"error": "Invalid position_id"}), 400

            # Check if email or username already exists
            cursor.execute("SELECT * FROM main_accounts WHERE email = %s OR username = %s", (email, username))
            if cursor.fetchone():
                return jsonify({"error": "Email or username already exists"}), 409

            # Insert into main_accounts
            cursor.execute("""
                INSERT INTO main_accounts (
                    account_type, position_id, first_name, middle_name, last_name,
                    contact_number, email, username, password
                )
                VALUES ('Admin', %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                position_id, first_name, middle_name, last_name,
                contact_number, email, username, hashed_pw
            ))

            conn.commit()
            return jsonify({"message": "Admin registered successfully."}), 201

        except Exception as e:
            conn.rollback()
            return jsonify({"error": f"Registration failed: {str(e)}"}), 500

        finally:
            cursor.close()
            conn.close()
