#!/bin/sh

# if there is newer Guix daemon compiled by `guix pull`, use it
if [ -x /var/guix/profiles/per-user/root/guix-profile/bin/guix-daemon ]; then
    BINARY=/var/guix/profiles/per-user/root/guix-profile/bin/guix-daemon
else
    # otherwise use the one installed with our package
    BINARY=/usr/bin/guix-daemon
fi

exec "$BINARY" --build-users-group=guixbuild
