"""
Configuration Module
"""

import os


class Config:
    """Configuration for all envs"""

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = [os.getenv("JWT_TOKEN_LOCATION")]


class DevelopmentConfig(Config):
    """Dev config"""

    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")


class TestingConfig(Config):
    """Test config"""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TESTING_DATABASE_URL")


class StagingConfig(Config):
    """Staging config"""

    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("STAGING_DATABASE_URL")


class ProductionConfig(Config):
    """Prod config"""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}
