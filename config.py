import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
   APP_NAME = os.environ.get('APP_NAME', 'Flask-Base')
   if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
   else:
        SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
        print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')
   #SECRET_KEY = os.environ.get("mlody")
   SQLALCHEMY_DATABASE_URI = ( 
           os.environ.get('DATABASE_URL') or
           'sqlite:///' + os.path.join(BASE_DIR, 'library.db')
   )
   SQLALCHEMY_TRACK_MODIFICATIONS = False