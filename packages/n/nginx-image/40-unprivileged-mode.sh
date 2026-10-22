#!/bin/sh

set -e

ME=$(basename "$0")

entrypoint_log() {
    if [ -z "${NGINX_ENTRYPOINT_QUIET_LOGS:-}" ]; then
        echo "$@"
    fi
}

entrypoint_log "$ME: Creating temporary folder at /tmp/nginx"

install -d /tmp/nginx/client_temp \
           /tmp/nginx/proxy_temp \
           /tmp/nginx/fastcgi_temp \
           /tmp/nginx/uwsgi_temp \
           /tmp/nginx/scgi_temp
