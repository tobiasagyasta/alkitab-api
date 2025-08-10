from flask import Flask
from .routes import bible_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(bible_bp, url_prefix="/api")

    @app.route("/", methods=["GET"])
    def welcome():
        return {"message": "Welcome to my Alkitab API!"}, 200


    return app
