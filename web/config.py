import os


class BaseConfig:
    """Base configuration"""
    DEBUG = True
    TESTING = False
    MONGODB_SETTINGS = {
        'db': 'rsframgia',
        'host': 'mongodb+srv://nhomanhemcututu:chubichthuy@cluster0.vnbw3.mongodb.net/rsframgia?authSource=admin&replicaSet=atlas-mi89bw-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true'
    }
    SECRET_KEY = os.environ.get("SECRET_KEY", "")


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
