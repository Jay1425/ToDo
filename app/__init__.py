# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Create the database object outside the function
db = SQLAlchemy()

# Define the application factory
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize the database
    db.init_app(app)
    
    # Import and register the blueprint
    from app import routes
    app.register_blueprint(routes.bp)
    
    # Create database tables (if they don’t exist)
    with app.app_context():
        db.create_all()
    
    # Return the app
    return app