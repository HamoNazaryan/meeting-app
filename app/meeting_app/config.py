import os

class Config:
  SECRET_KEY = "e77f61e2d38595229ce88ddf91b34b00"
  # SECRET_KEY = os.environ.get('SECRET_KEY')
  TEMPLATES_AUTO_RELOAD  = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
  # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
  # MAIL_SERVER = 'smtp.googlemail.com'
  # MAIL_PORT = 587
  # MAIL_USE_TLS = True
  # MAIL_USERNAME = os.environ.get('EMAIL_USER')
  # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
  # MAIL_DEFAULT_SENDER = ("Meeting",'EMAIL_USER')

  MAIL_SERVER = 'smtp.beget.com'
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  # MAIL_DEBUG = True 
  MAIL_USERNAME = 'meeting@travelinarmenia.am'
  MAIL_PASSWORD = 'Meeting555'
  MAIL_DEFAULT_SENDER = ("Meeting app",'meeting@travelinarmenia.am')
  MAIL_MAX_EMAILS = None
  # MAIL_SUPPRESS_SEND = False
  MAIL_ASCII_ATTACHMENTS = False  
