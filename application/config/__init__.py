from os.path import dirname, realpath

app_path = dirname(dirname(realpath(__file__)))

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

SECRET_KEY = 'Super Secret Key'

DATABASE_TABLE_PREFIX = 'ACT_'

SQLALCHEMY_DATABASE_URI = 'sqlite://%s/test.db' % app_path

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = 'Super_Secret_Key'
#     DATABASE_URI = 'sqlite://'


# class ProductionConfig(Config):
#     DEBUG = False
#     DATABASE_URI = 'mysql://user@localhost/foo'


# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class TestingConfig(Config):
#     TESTING = True

