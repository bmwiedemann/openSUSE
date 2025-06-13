#!/bin/bash
set -euo pipefail

if [[ ! -z "${LDAP_ADMIN_PASSWORD:-}" ]]; then
  echo "Setting LDAP password..."
  smbpasswd -w "$LDAP_ADMIN_PASSWORD"
fi

SMBD_OPTIONS=${SMBD_OPTIONS:-"--debuglevel=3"}

mkdir -p /var/lib/samba/etc /var/lib/samba/private

USER_FILES="passwd shadow group"

for f in $USER_FILES; do
  if [ -f /var/lib/samba/etc/$f ]; then
    cp /var/lib/samba/etc/$f /etc/$f
  else
    cp /etc/$f /var/lib/samba/etc/$f
  fi
done

exec catatonit -- /usr/sbin/smbd --foreground --no-process-group --debug-stdout $SMBD_OPTIONS
