from flask import Flask
from flask_cors import CORS
from .auth import auth  # Import auth blueprint for authentication-related routes
from .api import api_bp  # Import api blueprint for API-related routes
from .report import report  # Import report blueprint (if applicable)
from .trend_analysis import trend_analysis  # Import trend analysis blueprint (if applicable)

def create_app():
    app = Flask(__name__)
    
    # Enable CORS (for frontend-backend communication)
    CORS(app)
    
    # Load configuration from config.py
    app.config.from_object('config.Config')
    
    # Register Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(api_bp, url_prefix='/api')  # Register API with '/api' prefix
    app.register_blueprint(report)  # If you have a report blueprint
    app.register_blueprint(trend_analysis)  # If you have a trend analysis blueprint
    
    return app
