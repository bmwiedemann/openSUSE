#!/bin/bash
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
cat > /etc/rmt.conf <<EOF
database:
  host: ${MYSQL_HOST}
  database: ${MYSQL_DATABASE}
  username: ${MYSQL_USER}
  password: ${MYSQL_PASSWORD}
  adapter: mysql2
  encoding: utf8
  timeout: 5000
  pool: 5

scc:
  username: ${SCC_USERNAME}
  password:  ${SCC_PASSWORD}
  sync_systems: true
  scc_sync: ${SCC_SYNC}

log_level:
  rails: debug
EOF

if [ $# -eq 0 ]; then
	set -- /usr/share/rmt/bin/rails server -e production
fi

if [ "$1" = "/usr/share/rmt/bin/rails" ] && [ "$2" = "server" ]; then
  echo "Create/migrate SUSE RMT database"
  pushd /usr/share/rmt > /dev/null
	/usr/share/rmt/bin/rails db:create db:migrate RAILS_ENV=production
  popd > /dev/null
  if [ "${SCC_SYNC}" = "true" ]; then
    echo "Syncing product list"
    rmt-cli sync
    for PRODUCT in $SCC_PRODUCT_ENABLE
    do
      rmt-cli products enable "$PRODUCT"
    done
    for PRODUCT in $SCC_PRODUCT_DISABLE
    do
      rmt-cli products disable "$PRODUCT"
    done
    rmt-cli repos clean
  fi
  echo "Executing: catatonit -- $@"
  exec catatonit -- "$@"
else
	echo "Executing: $@"
	exec "$@"
fi
