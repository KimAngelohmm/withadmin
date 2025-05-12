from flask import Blueprint, request, jsonify
from config.dbconnection import get_db_connection
import bcrypt

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    customer_username = data.get("customer_username")
    first_name = data.get("Fname")
    middle_name = data.get("Mname")
    last_name = data.get("Lname")
    email = data.get("email")
    password = data.get("password")
    contact_number = data.get("contact_number")

    # Basic validation
    if not customer_username or not first_name or not last_name or not email or not password or not contact_number:
        return jsonify({
            "success": False,
            "message": "Username, first name, last name, email, password, and contact number are required."
        }), 400

    # Establish database connection
    conn = get_db_connection()
    if not conn:
        return jsonify({
            "success": False,
            "message": "Database connection failed."
        }), 500

    try:
        cursor = conn.cursor(dictionary=True)

        # Check if the email or contact number already exists
        cursor.execute("SELECT * FROM customer_accounts WHERE email = %s OR contact_number = %s", (email, contact_number))
        existing_user = cursor.fetchone()

        # Debugging: Log the query result
        print("Existing user check:", existing_user)

        if existing_user:
            return jsonify({
                "success": False,
                "message": "Email or contact number already registered."
            }), 409

        # Hash the password
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Debugging: Print the hashed password
        print("Hashed password:", hashed_pw.decode("utf-8"))

        # Insert into customer_accounts table
        cursor.execute(
            "INSERT INTO customer_accounts (customer_username, Fname, Mname, Lname, email, password, contact_number) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (customer_username, first_name, middle_name, last_name, email, hashed_pw.decode("utf-8"), contact_number)
        )
        conn.commit()

        return jsonify({
            "success": True,
            "message": "Registered successfully."
        }), 201

    except Exception as e:
        # Log the error message
        print(f"Error occurred during registration: {str(e)}")
        return jsonify({
            "success": False,
            "message": f"Registration failed: {str(e)}"
        }), 500

    finally:
        conn.close()
