#!/bin/bash -e

if [ -n "${ADMIN_PASSWORD}" ]; then
  echo -e "${ADMIN_PASSWORD}\n${ADMIN_PASSWORD}" | passwd admin
fi

if [ ! -f /etc/cups/cupsd.conf ]; then
  cp -rpn /etc/cups-skel/* /etc/cups/
fi

exec "$@"

