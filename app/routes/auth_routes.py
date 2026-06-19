from flask import (
    Blueprint,
    request,
    jsonify
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

import logging
from app.exceptions import UserNotFoundError
from app import db
from app.models.user import User


auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/register", methods=["POST"])
def register():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data provided"
            }), 400

        if not data.get("username"):
            return jsonify({
                "error": "Username required"
            }), 400

        if not data.get("email"):
            return jsonify({
                "error": "Email required"
            }), 400

        if not data.get("password"):
            return jsonify({
                "error": "Password required"
            }), 400

        existing_user = User.query.filter_by(
            email=data["email"]
        ).first()

        if existing_user:
            return jsonify({
                "error": "Email already exists"
            }), 409

        hashed_password = generate_password_hash(
            data["password"]
        )

        user = User(
            username=data["username"],
            email=data["email"],
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        logging.info(
            f"New user registered: {data['email']}"
        )

        return jsonify({
            "message": "User Registered Successfully"
        }), 201

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": "Registration Failed"
        }), 500


@auth_bp.route("/login", methods=["POST"])
def login():

    try:

        data = request.get_json()

        user = User.query.filter_by(
            email=data["email"]
        ).first()

        if not user:

            logging.warning(
                f"Login attempt with unknown email: {data['email']}"
            )

            return jsonify({
                "error": "Invalid Credentials"
            }), 401

        if not check_password_hash(
            user.password,
            data["password"]
        ):

            logging.warning(
                f"Invalid password attempt: {data['email']}"
            )

            return jsonify({
                "error": "Invalid Credentials"
            }), 401

        token = create_access_token(
            identity=str(user.id)
        )

        logging.info(
            f"User logged in: {user.email}"
        )

        return jsonify({
            "access_token": token
        })

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": "Login Failed"
        }), 500


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    try:
        user_id = get_jwt_identity()

        user = User.query.get(user_id)

        if not user:
            raise UserNotFoundError()

        return jsonify({
            "message": "Authorized User",
            "user": user.to_dict()
        })

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "error": "Profile Fetch Failed"
        }), 500