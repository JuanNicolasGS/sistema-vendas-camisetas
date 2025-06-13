import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    """Configuration class for the Flask application"""
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SESSION_SECRET') or 'dev-secret-key-change-in-production'
    
    # Google Sheets configuration
    GOOGLE_CREDENTIALS = os.environ.get('GOOGLE_CREDENTIALS')
    GOOGLE_SHEET_NAME = os.environ.get('GOOGLE_SHEET_NAME', 'T-Shirt Sales')
    
    # Form password
    FORM_PASSWORD = os.environ.get('FORM_PASSWORD', 'admin123')
    
    # Application settings
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    PORT = int(os.environ.get('FLASK_PORT', 5000))

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
