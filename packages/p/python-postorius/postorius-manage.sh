#!/bin/bash

sudo -u postorius-admin /usr/bin/python3 /srv/www/webapps/mailman/postorius/manage.py "$@"
