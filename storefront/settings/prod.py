import os
from .common import *

DEBUG = False

# with ALLOWED_HOSTS we specified the server or the servers that can run this applications
ALLOWED_HOSTS = []


SECRET_KEY = os.environ['SECRET_KEY']
