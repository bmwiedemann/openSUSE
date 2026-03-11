#!/bin/bash
CONFDIR="/etc/matrix-synapse"
DATADIR="/var/lib/matrix-synapse"
/usr/bin/python3 \
    -m synapse.app.homeserver \
    --config-path ${CONFDIR}/homeserver.yaml \
    --config-directory="${CONFDIR}/conf.d/" \
    --data-directory="${DATADIR}" \
    --generate-config \
    --report-stats=no \
    --server-name "$@" && \
/usr/bin/python3 \
    -m synapse.app.homeserver \
    --config-path ${CONFDIR}/homeserver.yaml \
    --config-directory="${CONFDIR}/conf.d/" \
    --data-directory="${DATADIR}" \
    --generate-missing-configs --generate-keys \
    --report-stats=no \
    --server-name "$@"
chown -R root:synapse "${CONFDIR}"
chmod -R u=rwX,g=rX,o= "${CONFDIR}"
