import os

class constants:
    DATABASE_FILE = 'penguicontrax.db'
    SESSION_SECRET_KEY = 'DEVELOPMENT_SECRET_KEY_CHANGE_ME_PLEASE' 
    DATABASE_URL = 'sqlite:///' + DATABASE_FILE if not 'DATABASE_URL' in os.environ else os.environ['DATABASE_URL']
    OPENID_STORE = 'openid_store'
    TWITTER_KEY = 'ECRuL6d9pjHX4ahB4NG5w'
    TWITTER_SECRET_KEY = 'nvstgAnRcnEXvEzZvchZCDXiYjBOWprNDMfLhz0HVQ'
    FACEBOOK_APP_ID = '522574207859497'
    FACEBOOK_SECRET = '06d93a085622870248f9b0c2a2e13c49' 
    PUBLIC_URL = 'http://gentle-tor-1515.herokuapp.com/'
    MODELER_PATH = '../modeler/runmodeler.sh'
    CLP_PATH = '../modeler/Clp-1.15.6/build/bin/clp'
    REDIS_URL = 'redis://localhost:6379' if not 'REDISTOGO_URL' in os.environ else os.environ['REDISTOGO_URL']
