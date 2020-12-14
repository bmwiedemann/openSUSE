#!/bin/sh
LOG_DIR="/var/log/postorius"
LIB_DIR="/var/lib/postorius"
DATA_DIR="$LIB_DIR/data/"

setfacl -R    --no-mask -m u:postorius-admin:rwX  ${DATA_DIR}
setfacl -R -d --no-mask -m u:postorius-admin:rwX  ${DATA_DIR}

chown   postorius-admin:postorius-admin           ${LIB_DIR}
chmod   u=rwX,g=rwX,o=                            ${LIB_DIR}

chown   -R postorius:postorius                    ${DATA_DIR}
chmod   -R u=rwX,g=rwX,o=                         ${DATA_DIR}

chown   postorius:postorius                       ${DATA_DIR}/postorius.db 2>/dev/null
chmod   u=rwX,g=rwX,o=                            ${DATA_DIR}/postorius.db 2>/dev/null

setfacl -R    --no-mask -m u:postorius:rwX        ${DATA_DIR}
setfacl -R -d --no-mask -m u:postorius:rwX        ${DATA_DIR}
setfacl -R    --no-mask -m u:postorius-admin:rwX  ${DATA_DIR}
setfacl -R -d --no-mask -m u:postorius-admin:rwX  ${DATA_DIR}

chown   postorius-admin:postorius-admin           ${LOG_DIR}
chmod   u=rwX,g=rwX,o=                            ${LOG_DIR}
chown   postorius-admin:postorius-admin           ${LOG_DIR}/postorius.log 2>/dev/null
chmod   u=rwX,g=rwX,o=                            ${LOG_DIR}/postorius.log 2>/dev/null

setfacl -R    --no-mask -m u:postorius:rwX        ${LOG_DIR}
setfacl -R -d --no-mask -m u:postorius:rwX        ${LOG_DIR}
setfacl -R    --no-mask -m u:postorius-admin:rwX  ${LOG_DIR}
setfacl -R -d --no-mask -m u:postorius-admin:rwX  ${LOG_DIR}
