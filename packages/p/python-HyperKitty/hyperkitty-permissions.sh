#!/bin/sh
LOG_DIR="/var/log/hyperkitty"
LIB_DIR="/var/lib/hyperkitty"
DATA_DIR="${LIB_DIR}/data"
WEBAPPS_DIR="/srv/www/webapps/mailman/hyperkitty"
CACHE_DIR="${WEBAPPS_DIR}/static/CACHE"

setfacl -R    --no-mask -m u:hyperkitty-admin:rwX  ${DATA_DIR}
setfacl -R -d --no-mask -m u:hyperkitty-admin:rwX  ${DATA_DIR}

chown   hyperkitty-admin:hyperkitty-admin          ${LIB_DIR}
chmod   u=rwX,g=rwX,o=                             ${LIB_DIR}

chown   -R hyperkitty:hyperkitty                   ${DATA_DIR}
chmod   -R u=rwX,g=rwX,o=                          ${DATA_DIR}

chown   hyperkitty:hyperkitty                      ${DATA_DIR}/hyperkitty.db 2>/dev/null
chmod   u=rwX,g=rwX,o=                             ${DATA_DIR}/hyperkitty.db 2>/dev/null

setfacl -R    --no-mask -m u:hyperkitty:rwX        ${DATA_DIR}
setfacl -R -d --no-mask -m u:hyperkitty:rwX        ${DATA_DIR}
setfacl -R    --no-mask -m u:hyperkitty-admin:rwX  ${DATA_DIR}
setfacl -R -d --no-mask -m u:hyperkitty-admin:rwX  ${DATA_DIR}

chown   hyperkitty-admin:hyperkitty-admin          ${LOG_DIR}
chmod   u=rwX,g=rwX,o=                             ${LOG_DIR}
chown   hyperkitty-admin:hyperkitty-admin          ${LOG_DIR}/hyperkitty.log 2>/dev/null
chmod   u=rwX,g=rwX,o=                             ${LOG_DIR}/hyperkitty.log 2>/dev/null

setfacl -R    --no-mask -m u:hyperkitty:rwX        ${LOG_DIR}
setfacl -R -d --no-mask -m u:hyperkitty:rwX        ${LOG_DIR}
setfacl -R    --no-mask -m u:hyperkitty-admin:rwX  ${LOG_DIR}
setfacl -R -d --no-mask -m u:hyperkitty-admin:rwX  ${LOG_DIR}

# The wsgi needs to write to static/CACHE
chown   -R hyperkitty:hyperkitty                   ${CACHE_DIR}
chmod   -R u=rwX,g=rwX,o=rX                        ${CACHE_DIR}

setfacl -R    --no-mask -m u:hyperkitty:rwX        ${CACHE_DIR}
setfacl -R -d --no-mask -m u:hyperkitty:rwX        ${CACHE_DIR}
setfacl -R    --no-mask -m u:hyperkitty-admin:rwX  ${CACHE_DIR}
setfacl -R -d --no-mask -m u:hyperkitty-admin:rwX  ${CACHE_DIR}
