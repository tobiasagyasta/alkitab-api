# wsgi.py (root)
from app import create_app

# Export both names so gunicorn can use either wsgi:app or wsgi:application
application = create_app()
app = application
