from pickle import TRUE

class Config:
    SECRET_KEY="OJOTA!#@"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST ='localhost'
    MYSQL_USER ='root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'rrhh_avisos'


config={
    'development':DevelopmentConfig
}
