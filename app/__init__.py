from flask import Flask
from .routes import bible_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bible_bp, url_prefix="/api")

    @app.route("/", methods=["GET"])
    def welcome():
        return {"message": "Welcome to my Alkitab API!"}, 200

    return app

# --- Defensive fallback: expose a module-level app object ---
# This allows gunicorn to load `app:app` if something in CI/host references the package directly.
try:
    _created = create_app()
    app = _created
except Exception:
    # If creation fails at import time we still define `app` so Gunicorn error becomes visible
    # but we don't crash import in case of other issues.
    app = None
