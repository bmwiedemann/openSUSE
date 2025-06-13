#!/bin/bash
cmd=$(basename "$0")

/usr/sbin/$cmd "$@"
rc=$?

if [ "$rc" -eq 0 ]; then
  echo "Syncing user/group files"
  cp /etc/passwd /var/lib/samba/etc/passwd
  cp /etc/shadow /var/lib/samba/etc/shadow
  cp /etc/group /var/lib/samba/etc/group
fi

exit $rc
