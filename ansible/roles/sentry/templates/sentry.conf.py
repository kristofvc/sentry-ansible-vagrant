# This file is just Python, with a touch of Django which means you
# you can inherit and tweak settings to your hearts content.
from sentry.conf.server import *

import os.path

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        # You can swap out the engine for MySQL easily by changing this value
        # to ``django.db.backends.mysql`` or to PostgreSQL with
        # ``django.db.backends.postgresql_psycopg2``

        # If you change this, you'll also need to install the appropriate python
        # package: psycopg2 (Postgres) or mysql-python
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': '{{ pgsql.database }}',
        'USER': '{{ pgsql.user }}',
        'PASSWORD': '{{ pgsql.password }}',
        'HOST': 'localhost',
        'PORT': '',

        'OPTIONS': {
            'autocommit': True
        }
    }
}

# You should not change this setting after your database has been created
# unless you have altered all schemas first
SENTRY_USE_BIG_INTS = True

# If you're expecting any kind of real traffic on Sentry, we highly recommend
# configuring the CACHES and Redis settings

#############
## General ##
#############

# The administrative email for this installation.
# Note: This will be reported back to getsentry.com as the point of contact. See
# the beacon documentation for more information.

# SENTRY_ADMIN_EMAIL = 'your.name@example.com'
SENTRY_ADMIN_EMAIL = '{{ sentry.admin_email }}'

SENTRY_FEATURES['auth:register'] = False

###########
## Redis ##
###########

# Generic Redis configuration used as defaults for various things including:
# Buffers, Quotas, TSDB

SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': '127.0.0.1',
            'port': 6379,
        }
    }
}

###########
## Cache ##
###########

# If you wish to use memcached, install the dependencies and adjust the config
# as shown:
#
#   pip install python-memcached
#
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['127.0.0.1:11211'],
    }
}

SENTRY_CACHE = 'sentry.cache.django.DjangoCache'
ENTRY_CACHE = 'sentry.cache.redis.RedisCache'

###########
## Queue ##
###########

# See http://sentry.readthedocs.org/en/latest/queue/index.html for more
# information on configuring your queue broker and workers. Sentry relies
# on a Python framework called Celery to manage queues.

CELERY_ALWAYS_EAGER = False
BROKER_URL = 'redis://localhost:6379/0'

#################
## Rate Limits ##
#################

SENTRY_RATELIMITER = 'sentry.ratelimits.redis.RedisRateLimiter'

####################
## Update Buffers ##
####################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

############
## Quotas ##
############

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'

##########
## TSDB ##
##########

# The TSDB is used for building charts as well as making things like per-rate
# alerts possible.

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'

##################
## File storage ##
##################

# Any Django storage backend is compatible with Sentry. For more solutions see
# the django-storages package: https://django-storages.readthedocs.org/en/latest/

SENTRY_FILESTORE = 'django.core.files.storage.FileSystemStorage'
SENTRY_FILESTORE_OPTIONS = {
    'location': '/tmp/sentry-files',
}

################
## Web Server ##
################

# You MUST configure the absolute URI root for Sentry:
SENTRY_URL_PREFIX = 'http://{{ sentry.hostname }}'  # No trailing slash!

# If you're using a reverse proxy, you should enable the X-Forwarded-Proto
# header and uncomment the following settings
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = {{ sentry.port }}
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'limit_request_line': 0
    # 'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

#################
## Mail Server ##
#################

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

# The email address to send on behalf of
SERVER_EMAIL = '{{ sentry.server_email }}'

# If you're using mailgun for inbound mail, set your API key and configure a
# route to forward to /api/hooks/mailgun/inbound/
MAILGUN_API_KEY = '{{ sentry.mailgun_key }}'

###########
## etc. ##
###########

# If this file ever becomes compromised, it's important to regenerate your SECRET_KEY
# Changing this value will result in all current sessions being invalidated
SECRET_KEY = '{{ sentry.secret }}'

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = '{{ sentry.twitter_consumer_key }}'
TWITTER_CONSUMER_SECRET = '{{ sentry.twitter_consumer_secret }}'

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = '{{ sentry.facebook_app_id }}'
FACEBOOK_API_SECRET = '{{ sentry.facebook_api_secret }}'

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = '{{ sentry.google_oauth2_client_id }}'
GOOGLE_OAUTH2_CLIENT_SECRET = '{{ sentry.google_oauth2_client_secret }}'

# https://github.com/settings/applications/new
GITHUB_APP_ID = '{{ sentry.github_app_id }}'
GITHUB_API_SECRET = '{{ sentry.github_api_secret }}'

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = '{{ sentry.trello_api_key }}'
TRELLO_API_SECRET = '{{ sentry.trello_api_secret }}'

# https://confluence.atlassian.com/display/BITBUCKET/OAuth+Consumers
BITBUCKET_CONSUMER_KEY = '{{ sentry.bitbucket_consumer_key }}'
BITBUCKET_CONSUMER_SECRET = '{{ sentry.bitbucket_consumer_secret }}'
