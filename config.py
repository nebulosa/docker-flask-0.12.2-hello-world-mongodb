import os
import urllib.parse

class Config(object):
    #per environment settings
    APP_ENVIRONMENT = os.environ.get('APP_ENVIRONMENT') or 'development'

    if   APP_ENVIRONMENT == 'development':
        DEBUG   = True
        TESTING = True #disable recaptcha
    elif APP_ENVIRONMENT == 'production' :
        DEBUG  = False

    #flask-mongoengine
    MONGODB_HOST     = os.environ.get('MONGODB_HOST')     or 'mongodb'
    MONGODB_TCP_PORT = os.environ.get('MONGODB_TCP_PORT') or 27017
    MONGODB_TCP_PORT = int(MONGODB_TCP_PORT)
    MONGODB_DB       = os.environ.get('MONGODB_DB')       or 'app'
    MONGODB_USER     = os.environ.get('MONGODB_USER')     or 'app'
    MONGODB_PASSWD   = os.environ.get('MONGODB_PASSWD')   or 'app'

    MONGODB_USER     = urllib.parse.quote_plus(MONGODB_USER)
    MONGODB_PASSWD   = urllib.parse.quote_plus(MONGODB_PASSWD)

    MONGODB_SETTINGS = {
        'db':       MONGODB_DB,
        'host':     MONGODB_HOST,
        'port':     MONGODB_TCP_PORT,
        'username': MONGODB_USER,
        'password': MONGODB_PASSWD,
    }
