import os
import dj_database_url
from .common import *

DEBUG = False

# with ALLOWED_HOSTS we specified the server or the servers that can run this applications
ALLOWED_HOSTS = ['smkbuy-prod.herokuapp.com']


SECRET_KEY = os.environ['SECRET_KEY']


DATABASES = {
    'default': dj_database_url.config()
}

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
