class Config:
    """
    Common configuration settings.
    """
    SECRET_KEY = 'your_secret_key'  # Change this to a secure random key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # SQLite database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable Flask-SQLAlchemy modification tracking
    DEBUG = True  # Enable debug mode for development
    STRIPE_PUBLIC_KEY = 'your_stripe_public_key'  # Stripe public key for payment processing
    STRIPE_SECRET_KEY = 'your_stripe_secret_key'  # Stripe secret key for payment processing

class ProductionConfig(Config):
    """
    Configuration settings for the production environment.
    """
    DEBUG = False  # Disable debug mode for production
