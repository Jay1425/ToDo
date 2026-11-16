import os
class Config:
    if os.environ.get('FLASK_ENV') == 'production' and not os.environ.get('SECRET_KEY'):
        raise RuntimeError('SECRET_KEY must be configured in production')
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

