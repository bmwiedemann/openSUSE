#!/bin/bash

# Wrapper that makes sure /etc/vnc/tls.{key,cert} exist before executing given command.


TLSKEY=/etc/vnc/tls.key
TLSCERT=/etc/vnc/tls.cert


if test -s $TLSKEY -a -s $TLSCERT; then
    # Execute the command we were given.
    exec "$@"
fi

(
    # Wait for lock on the key file. We must not proceed while someone else is creating it.
    flock 200

    # If the key file doesn't exist or has zero size (because it doubles as lock), generate it.
    if ! test -s $TLSKEY ; then
        (umask 077 && openssl genrsa -out $TLSKEY 2048) >&200
        chown vnc:vnc $TLSKEY
    fi

    # If the cert file doesn't exist, generate it.
    if ! test -e $TLSCERT ; then
        # Keeping it short, because hostname could be long and max CN is 64 characters
        CN="`hostname`"
        CN=${CN:0:64}
        openssl req -new -x509 -extensions usr_cert -key $TLSKEY -out $TLSCERT -days 7305 -subj "/CN=$CN/"
        chown vnc:vnc $TLSCERT
    fi

) 200>>$TLSKEY 2>/dev/null

# Execute the command we were given.
exec "$@"
