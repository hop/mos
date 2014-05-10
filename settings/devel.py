# Django settings for a local development instance of MOS
from common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mos.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = PROJECT_DIR.child("media")

HOS_SEPA_CREDITOR_ID = 'AT29HXR00000037632'
