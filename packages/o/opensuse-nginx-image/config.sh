#!/bin/sh

#--------------------------------------
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

# Log to stdout/stderr
ln -sf /dev/stdout /var/log/nginx/access.log
ln -sf /dev/stderr /var/log/nginx/error.log

# Create fallback backp of default config files and data
mkdir -p /usr/local/nginx/etc
cp -av /etc/nginx/* /usr/local/nginx/etc/
rm /etc/nginx/*
rm /usr/local/nginx/etc/*.default
mkdir -p /usr/local/nginx/htdocs
cp -av /srv/www/htdocs/* /usr/local/nginx/htdocs

exit 0
