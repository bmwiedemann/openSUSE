#!/bin/bash

/usr/bin/mysqladmin --user=root --socket=${MYSQL_UNIX_PORT} shutdown 2>&1 || \
[ ! -s "${MYSQL_PIDFILE}" ] || /bin/kill `cat "${MYSQL_PIDFILE}"` || true
rm -rf ${MYSQL_DIR}
