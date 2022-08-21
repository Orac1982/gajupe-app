from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = 'super-secret'

# DB Config
DB_FILE = 'app/app.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = 'upload'

SECURITY_PASSWORD_SALT = 'onetwothreefourfive'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CHANGEABLE = True

MAIL_SERVER = 'localhost'
MAIL_PORT = 8025
