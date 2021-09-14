from faker import Faker
fake = Faker()

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
INSTALLED_APPS=(
    'django_seed',
)
SECRET_KEY=fake.sha1()

