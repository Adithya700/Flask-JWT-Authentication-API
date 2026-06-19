from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import logging

db = SQLAlchemy()
jwt = JWTManager()

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_app():

    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    @app.errorhandler(404)
    def not_found(error):
        return {
            "error": "Resource Not Found"
        }, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {
            "error": "Internal Server Error"
        }, 500

    return app