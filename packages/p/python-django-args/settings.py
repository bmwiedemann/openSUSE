import dj_database_url


SECRET_KEY = 'django-args'
# Install the tests as an app so that we can make test models
INSTALLED_APPS = [
    'djarg',
    'djarg.tests',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
]
# Database url comes from the DATABASE_URL env var
DATABASES = {'default': dj_database_url.config()}

# Settings for integration tests
DEBUG = True
ROOT_URLCONF = 'djarg.tests.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# For testing session-based form wizards
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
