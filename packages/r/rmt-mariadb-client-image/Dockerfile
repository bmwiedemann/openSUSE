# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/rmt-mariadb-client:%%mariadb_version%%
#!BuildTag: opensuse/rmt-mariadb-client:%%mariadb_version%%-%RELEASE%
#!BuildTag: opensuse/rmt-mariadb-client:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.rmt-mariadb-client
LABEL org.opencontainers.image.title="openSUSE Tumbleweed MariaDB Client for SUSE RMT"
LABEL org.opencontainers.image.description="MariaDB Client for SUSE RMT container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%mariadb_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/rmt-mariadb-client:%%mariadb_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends mariadb-client; zypper -n clean; rm -rf /var/log/*
CMD ["mariadb"]
