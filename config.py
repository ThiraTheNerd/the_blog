import os

class Config:
  QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thirathenerd:admin2021@localhost/blog'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}