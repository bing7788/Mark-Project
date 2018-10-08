class Config(object):
    """Base config class"""
    pass

class ProdConfig(Config):
    """Production config class"""
    pass

class DevConfig(Config):
    """Development config class"""
    #Open the DEBUG
    DEBUG = True
    # MySQL connection
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = 'localhost'
    PORT = '3306'
    DATABASE = 'pymysql'
 
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
        DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
       