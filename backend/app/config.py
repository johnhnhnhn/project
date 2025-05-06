class Config:
    SECRET_KEY = 'your_secret_key'  # Secret key for sessions or JWT tokens
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/site.db'  # Database URI (use PostgreSQL in production)
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Turn off unnecessary modification tracking
    DEBUG = True  # Set to False in production
