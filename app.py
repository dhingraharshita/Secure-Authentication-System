from flask import Flask
from flask import render_template
from config import Config

from models.user import db

from flask_jwt_extended import JWTManager

from routes.auth import auth_bp


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(
    auth_bp,
    url_prefix="/auth"
)


with app.app_context():
    db.create_all()

@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")


@app.route("/forgot-password")
def forgot_password_page():
    return render_template("forgot_password.html")


@app.route("/verify-otp")
def verify_otp_page():
    return render_template("verify_otp.html")
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/security")
def security():
    return render_template("security.html")

@app.route("/login-history")
def login_history():
    return render_template("login_history.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/")
def home():

    return {
        "message": "Secure Authentication System Running"
    }


if __name__ == "__main__":
    app.run(
        debug=True
    )