import dj_database_url


SECRET_KEY = 'django-action-framework'
# Install the tests as an app so that we can make test models
INSTALLED_APPS = [
    'daf',
    'daf.tests',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]
# Database url comes from the DATABASE_URL env var
DATABASES = {'default': dj_database_url.config()}

# For integration testing with the test app
ROOT_URLCONF = 'daf.tests.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ]
        },
    }
]
DEBUG = True
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
