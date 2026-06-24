import os

class Config:

    SECRET_KEY = "super_secret_key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///auth.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "jwt_secret_key"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = "your_email@gmail.com"
    MAIL_PASSWORD = "your_app_password"