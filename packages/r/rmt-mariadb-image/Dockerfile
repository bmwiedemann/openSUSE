# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/rmt-mariadb:%%mariadb_version%%
#!BuildTag: opensuse/rmt-mariadb:%%mariadb_version%%-%RELEASE%
#!BuildTag: opensuse/rmt-mariadb:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.rmt-mariadb
LABEL org.opencontainers.image.title="openSUSE Tumbleweed MariaDB Server for SUSE RMT"
LABEL org.opencontainers.image.description="MariaDB Server for SUSE RMT container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%mariadb_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/rmt-mariadb:%%mariadb_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends mariadb mariadb-tools gawk timezone util-linux; zypper -n clean; rm -rf /var/log/*
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["mariadbd"]
EXPOSE 3306
RUN set -euo pipefail; mkdir /docker-entrypoint-initdb.d

# docker-entrypoint from https://github.com/MariaDB/mariadb-docker.git
COPY docker-entrypoint.sh /usr/local/bin/
RUN set -euo pipefail; chmod 755 /usr/local/bin/docker-entrypoint.sh
RUN set -euo pipefail; ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat

RUN set -euo pipefail; sed -i 's#gosu mysql#su mysql -s /bin/bash -m#g' /usr/local/bin/docker-entrypoint.sh

# Ensure all logs goes to stdout
RUN set -euo pipefail; sed -i 's/^log/#log/g' /etc/my.cnf

# Disable binding to localhost only, doesn't make sense in a container
RUN set -euo pipefail; sed -i -e 's|^\(bind-address.*\)|#\1|g' /etc/my.cnf

RUN set -euo pipefail; mkdir /run/mysql

VOLUME /var/lib/mysql
