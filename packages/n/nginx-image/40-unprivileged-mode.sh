#!/bin/sh

echo "$0: Creating temporary folder at /tmp/nginx"

install -d /tmp/nginx/client_temp \
           /tmp/nginx/proxy_temp \
           /tmp/nginx/fastcgi_temp \
           /tmp/nginx/uwsgi_temp \
           /tmp/nginx/scgi_temp
