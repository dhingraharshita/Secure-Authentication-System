from flask import Blueprint, render_template, request, redirect, url_for

from services.auth_service import AuthService
from utils.jwt_handler import generate_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        result = AuthService.register_user(
            username,
            email,
            password
        )

        if result["success"]:
            return redirect("/login")

        return result["message"]

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        result = AuthService.login_user(
            email,
            password
        )

        if not result["success"]:
            return result["message"]

        token = generate_token(result["user"])

        return render_template(
            "dashboard.html",
            token=token
        )

    return render_template("login.html")
