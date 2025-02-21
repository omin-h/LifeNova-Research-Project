import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    # Add other configurations as needed, e.g., database URI
    # DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///your_database.db'
