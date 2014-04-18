
class ProductionConfig(object):
    DEBUG = True
    TESTING = False
    MONGODB_SETTINGS = {'DB': 'flaskstarter_production'}
    SECRET_KEY = 'flask+mongoengine=<3'
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class ProductionConfigHome(object):
    DEBUG = True
    TESTING = False
    MONGODB_SETTINGS = {'HOST': 'mongodb://demo:demo@update.vobi.ge:27017/vobismart', 'DB': 'vobismart'}
    SECRET_KEY = 'flask+mongoengine=<3'
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SMTP = ''
    SMTP_USER= ''
    SMTP_PASSWORD = ''


class TestConfig(object):
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {'DB': 'flaskstarter_test'}
    SECRET_KEY = 'flask+mongoengine=<3'
    DEBUG_TB_INTERCEPT_REDIRECTS = False