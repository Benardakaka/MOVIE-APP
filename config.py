import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'bena'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:20302000b@localhost/moviez'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    MOVIE_URL = "https://api.themoviedb.org/3/movie/550?api_key=04319e158b74fc6aa9055b417b68d78c"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MOVIE_API_KEY='04319e158b74fc6aa9055b417b68d78c'


     #email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'moviez'
    SENDER_EMAIL = 'benardakaka484@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

   
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # TESTING = True

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:20302000b@localhost/moviez'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:20302000b@localhost/moviez'

    DEBUG = True
    ENV = 'development'
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
