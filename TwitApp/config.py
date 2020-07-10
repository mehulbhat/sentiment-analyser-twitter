import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = os.environ \
                   .get('SECRET_KEY',
                        'Z\xf0\xfb\xf0r\x8c\r\xa4\xc6Qf\xc2\x15\xcb\x12')
