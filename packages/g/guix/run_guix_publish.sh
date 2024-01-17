#!/bin/sh

# if there is newer Guix compiled by `guix pull`, use it
if [ -x /var/guix/profiles/per-user/root/guix-profile/bin/guix-publish ]; then
    BINARY=/var/guix/profiles/per-user/root/guix-profile/bin/guix
else
    # otherwise use the one installed with our package
    BINARY=/usr/bin/guix
fi

exec "$BINARY" publish --user=nobody --port=8181
