HyperKitty
==========

## Configuration

The web application is configured in `/etc/hyperkitty/settings_local.py` which
is included by the default configuration in
/srv/www/webapps/mailman/hyperkitty/settings.py.

1. Optional: Change the default secret for the application:
   We already created one, but feel free to replace with a stronger
   alternative.

   `/etc/hyperkitty/settings_local.py`:

      SECRET_KEY = 'something-very-secret'

2. Make sure to disable debugging when running in production:

   `/etc/hyperkitty/settings_local.py`:

       DEBUG = False

3. The valid hosts or domain names for the application need to be defined:

   `/etc/hyperkitty/settings_local.py`:

        ALLOWED_HOSTS = [
            'localhost',
            'lists.example.com'
        ]

4. Add a valid email configuration

   `/etc/hyperkitty/settings_local.py`:

        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'localhost'
        EMAIL_PORT = 25
        EMAIL_HOST_USER = <username>
        EMAIL_HOST_PASSWORD = <password>

5. To connect with a running mailman instance's REST API, configuration options
   have to be added to hyperkitty's configuration.

   `/etc/hyperkitty/settings_local.py`:

        MAILMAN_REST_API_URL = 'http://localhost:8001'
        MAILMAN_REST_API_USER = 'rest_admin'
        MAILMAN_REST_API_PASS = 'rest_admin_password'

6. To configure the archive integration with a mailman instance first setup the
   integration with hyperkitty on mailman's side and then configure hyperkitty
   to accept those connections:

    `/etc/hyperkitty/settings_local.py`:

        MAILMAN_ARCHIVER_KEY = 'SecretArchiverAPIKey'
        MAILMAN_ARCHIVER_FROM = ('127.0.0.1', '::1')

7. Optional: Configure postgres or another database (default: sqlite3)

8. Create and setup the database

        hyperkitty-manage migrate

9. Populate the database with default data (when setting up for the first time):

        hyperkitty-manage loaddata first_start

10. Create admin user

       hyperkitty-manage createsuperuser

11. Enable HyperKitty async tasks runner

       systemctl enable --now hyperkitty-qcluster.service

12. Enable HyperKitty runjob timers

       systemctl enable hyperkitty-runjob-minutely.timer
       systemctl enable hyperkitty-runjob-quarter-hourly.timer
       systemctl enable hyperkitty-runjob-hourly.timer
       systemctl enable hyperkitty-runjob-daily.timer
       systemctl enable hyperkitty-runjob-weekly.timer
       systemctl enable hyperkitty-runjob-monthly.timer
       systemctl enable hyperkitty-runjob-yearly.timer

## Apache2

To configure hyperkitty with Apache and uwsgi, just add the follwing lines to a vhost:

    ProxyPassMatch ^/static !
    ProxyPass / unix:/run/uwsgi/uwsgi-hyperkitty.sock|uwsgi://localhost/
    <Directory /srv/www/webapps/mailman/hyperkitty>
        Require all granted
    </Directory>

## Xapian search backend

Hyperkitty can make use of a Xapian based search backend.

`/etc/hyperkitty/settings_local.py`:

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'xapian_backend.XapianEngine',
            'PATH': "/var/lib/hyperkitty/data/xapian_index",
        },
    }

Make sure to create the search index for all lists afterwards.

    hyperkitty-manage update_index
