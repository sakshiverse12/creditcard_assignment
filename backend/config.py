"""
Configuration file for Credit Card Statement Parser
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration"""
    
    # Flask settings
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # File upload settings
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16 * 1024 * 1024))  # 16MB default
    ALLOWED_EXTENSIONS = {'pdf'}
    DELETE_AFTER_PARSE = os.getenv('DELETE_AFTER_PARSE', 'True').lower() == 'true'
    
    # Parser settings
    SUPPORTED_ISSUERS = [
        'Chase',
        'American Express',
        'Citibank',
        'Capital One',
        'Discover'
    ]
    
    # Data points to extract
    DATA_POINTS = [
        'card_issuer',
        'card_last_4_digits',
        'billing_cycle',
        'payment_due_date',
        'total_balance',
        'minimum_payment',
        'statement_date',
        'account_holder'
    ]


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    DELETE_AFTER_PARSE = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
