#!/bin/sh

#--------------------------------------
#test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

mkdir -p /usr/local/nginx/etc
cp -av /etc/nginx/* /usr/local/nginx/etc/
rm /etc/nginx/*.default
rm /usr/local/nginx/etc/*.default
mkdir -p /usr/local/nginx/htdocs
cp -av /srv/www/htdocs/* /usr/local/nginx/htdocs

exit 0
