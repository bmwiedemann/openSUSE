# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/postgres:14
#!BuildTag: opensuse/postgres:14-%RELEASE%
#!BuildTag: opensuse/postgres:%%pg_version%%
#!BuildTag: opensuse/postgres:%%pg_version%%-%RELEASE%

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.postgres
LABEL org.opencontainers.image.title="openSUSE Tumbleweed PostgreSQL 14"
LABEL org.opencontainers.image.description="PostgreSQL 14 container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="14"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/postgres:14-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends postgresql14-server; zypper -n clean; rm -rf /var/log/*
ENV LANG="en_US.utf8"
ENV PG_MAJOR="14"
ENV PG_VERSION="%%pg_version%%"
ENV PGDATA="/var/lib/pgsql/data"

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["postgres"]
EXPOSE 5432
COPY docker-entrypoint.sh /usr/local/bin/
RUN set -euo pipefail; chmod +x /usr/local/bin/docker-entrypoint.sh; \
    sed -i -e 's/exec gosu postgres "/exec setpriv --reuid=postgres --regid=postgres --clear-groups -- "/g' /usr/local/bin/docker-entrypoint.sh; \
    mkdir /docker-entrypoint-initdb.d; \
    install -d -m 0700 -o postgres -g postgres $PGDATA; \
    sed -ri "s|^#?(listen_addresses)\s*=\s*\S+.*|\1 = '*'|" /usr/share/postgresql14/postgresql.conf.sample

STOPSIGNAL SIGINT
HEALTHCHECK --interval=10s --start-period=10s --timeout=5s \
    CMD pg_isready -U ${POSTGRES_USER:-postgres} -h localhost -p 5432

VOLUME $PGDATA
