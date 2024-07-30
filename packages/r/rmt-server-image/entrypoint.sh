#!/bin/sh
set -e

# PV could be empty, make sure the directories exist
mkdir -p /var/lib/rmt/public/repo
mkdir -p /var/lib/rmt/public/suma
mkdir -p /var/lib/rmt/regsharing
mkdir -p /var/lib/rmt/tmp
# Set permissions
chown -R _rmt:nginx /var/lib/rmt

if [ -z "${MYSQL_HOST}" ]; then
	echo "MYSQL_HOST not set!"
	exit 1
fi
if [ -z "${MYSQL_PASSWORD}" ]; then
        echo "MYSQL_PASSWORD not set!"
        exit 1
fi

MYSQL_DATABASE="${MYSQL_DATABASE:-rmt}"
MYSQL_USER="${MYSQL_USER:-rmt}"
SCC_SYNC="${SCC_SYNC:-true}"

# Create adjusted /etc/rmt.conf
echo -e "database:\n  host: ${MYSQL_HOST}\n  database: ${MYSQL_DATABASE}\n  username: ${MYSQL_USER}\n  password: ${MYSQL_PASSWORD}" > /etc/rmt.conf
echo -e "  adapter: mysql2\n  encoding: utf8\n  timeout: 5000\n  pool: 5\n" >> /etc/rmt.conf
echo -e "scc:\n  username: ${SCC_USERNAME}\n  password:  ${SCC_PASSWORD}\n  sync_systems: ${SCC_SYNC}\n" >> /etc/rmt.conf
echo -e "log_level:\n  rails: debug" >> /etc/rmt.conf

if [ $# -eq 0 ]; then
	set -- /usr/share/rmt/bin/rails server -e production
fi

if [ "$1" == "/usr/share/rmt/bin/rails" -a "$2" == "server" ]; then
  echo "Create/migrate SUSE RMT database"
  pushd /usr/share/rmt > /dev/null
	/usr/share/rmt/bin/rails db:create db:migrate RAILS_ENV=production
  popd > /dev/null
  if [ ${SCC_SYNC} != "false" ]; then
    echo "Syncing product list"
    rmt-cli sync
    for PRODUCT in $SCC_PRODUCT_ENABLE
    do
      rmt-cli products enable $PRODUCT
    done
    for PRODUCT in $SCC_PRODUCT_DISABLE
    do
      rmt-cli products disable $PRODUCT
    done
    rmt-cli repos clean
  fi
  echo "Executing: catatonit -- $@"
  exec catatonit -- "$@"
else
	echo "Executing: $@"
	exec "$@"
fi
