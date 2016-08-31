import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'not-today-piggly-not-today.'
DEBUG = True
TESTING = False

class BaseConfiguration(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'not-today-piggly-not-today.'
    HASH_ROUNDS = 100000
    WTF_CSRF_ENABLED = True

class TestConfiguration(BaseConfiguration):
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/test_db'
    HASH_ROUNDS = 1


# class Config(object):

# class ProductionConfig(Config):
#     DEBUG = False
#
# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#
# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#
# class TestingConfig(Config):
#     TESTING = True
