#!/bin/sh

#======================================
# Functions...
#--------------------------------------
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

mv /srv/www/htdocs/index.html /srv/www/htdocs/nginx.html
mv /etc/php8/fpm/php-fpm.conf.default /etc/php8/fpm/php-fpm.conf
mv /etc/php8/fpm/php-fpm.d/www.conf.default /etc/php8/fpm/php-fpm.d/www.conf

# Enable ping URL for healthcheck
sed -i -e 's|;ping.path = /ping|ping.path = /fpm-ping|g' /etc/php8/fpm/php-fpm.d/www.conf
