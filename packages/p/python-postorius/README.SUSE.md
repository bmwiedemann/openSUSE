Postorius
=========

## Configuration

The web application is configured in `/etc/postorius/settings_local.py` which
is included by the default configuration in
/srv/www/webapps/postorius/settings.py. 

1. Optional: Change the default secret for the application:
   We already created one, but feel free to replace with a stronger
   alternative.

   `/etc/postorius/settings_local.py`:

       SECRET_KEY = 'something-very-secret'

2. Make sure to disable debugging when running in production:

   `/etc/postorius/settings_local.py`:

       DEBUG = False

3. The valid hosts or domain names for the application need to be defined:

   `/etc/postorius/settings_local.py`:

        ALLOWED_HOSTS = [
            'localhost',
            'lists.example.com'
        ]

4. To be able to configure a running mailman instance configuration options for
   its REST API have to be added to postorius' configuration.

   `/etc/postorius/settings_local.py`

       MAILMAN_REST_API_URL = 'http://localhost:8001'
       MAILMAN_REST_API_USER = 'rest_admin'
       MAILMAN_REST_API_PASS = 'rest_admin_password'


5. Add a valid email configuration

   `/etc/postorius/settings_local.py`:

        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'localhost'
        EMAIL_PORT = 25
        EMAIL_HOST_USER = <username>
        EMAIL_HOST_PASSWORD = <password>

7. Optional: Configure postgres or another database (default: sqlite3)

6. Create and setup the database

    postorius-manage migrate

7. Create admin user

    postorius-manage createsuperuser

## Apache2

To configure postorius with Apache and uwsgi, just add the follwing lines to a vhost:

    ProxyPass /.well-known/acme-challenge !
    ProxyPassMatch ^/static !
    ProxyPass / unix:/run/uwsgi/uwsgi-postorius.sock|uwsgi://localhost/
    <Directory /srv/www/webapps/mailman/postorius>
        Require all granted
    </Directory>
