import bcrypt
from models.user import User, db


class AuthService:

    @staticmethod
    def register_user(username, email, password):

        existing_user = User.query.filter(
            (User.username == username) |
            (User.email == email)
        ).first()

        if existing_user:
            return {
                "success": False,
                "message": "User already exists"
            }

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        new_user = User(
            username=username,
            email=email,
            password_hash=hashed_password.decode("utf-8")
        )

        db.session.add(new_user)
        db.session.commit()

        return {
            "success": True,
            "message": "Registration successful"
        }

    @staticmethod
    def login_user(email, password):

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:
            return {
                "success": False,
                "message": "User not found"
            }

        password_match = bcrypt.checkpw(
            password.encode("utf-8"),
            user.password_hash.encode("utf-8")
        )

        if not password_match:
            return {
                "success": False,
                "message": "Invalid password"
            }

        return {
            "success": True,
            "message": "Login successful",
            "user": user
        }
