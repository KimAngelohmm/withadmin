import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_cors import CORS

# Existing auth routes
from auth.login import login
from auth.register import register_bp
from auth.forgotpassword import forgot_password
from auth.guest_login import guest_login

# Admin auth routes (procedural-style initialization)
from auth.admin_login import init_admin_login_routes
from auth.admin_register import init_admin_register_routes

app = Flask(__name__)
CORS(app)

# Register Blueprint
app.register_blueprint(register_bp, url_prefix="/auth")

# Procedural route registrations
app.add_url_rule('/login', view_func=login, methods=["POST"])
app.add_url_rule('/forgot-password', view_func=forgot_password, methods=["POST"])
app.add_url_rule('/guest-login', view_func=guest_login, methods=["POST"])

# Initialize admin routes
init_admin_login_routes(app)
init_admin_register_routes(app)

@app.route("/")
def home():
    return "Welcome to Anyhaw API"

if __name__ == "__main__":
    app.run(debug=True)
