#!/bin/sh

DIR=$(dirname $0)
CACHE_DIR=$($DIR/cache_dir.sed < /etc/squid/squid.conf)
if [ 'x'$CACHE_DIR = 'x' ]; then
    exit 0
fi

if ! test -d $CACHE_DIR; then
    echo "Initializing cache directories..."
    exec /usr/sbin/squid -z -F --foreground -S
fi

