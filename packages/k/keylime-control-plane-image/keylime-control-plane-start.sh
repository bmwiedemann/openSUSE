#!/bin/sh

set -e

# Start the verifier and the registar in the correct order
/usr/bin/keylime_verifier &
# TODO fix the race condition
sleep 2
exec /usr/bin/keylime_registrar
