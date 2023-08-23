# SPDX-License-Identifier: Apache-2.0
#!BuildTag: opensuse/grafana:%%grafana_version%%
#!BuildTag: opensuse/grafana:%%grafana_version%%-%RELEASE%
#!BuildTag: opensuse/grafana:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.grafana
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Grafana"
LABEL org.opencontainers.image.description="Grafana container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%grafana_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/grafana:%%grafana_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends grafana; zypper -n clean; rm -rf /var/log/*
ENV GF_PATHS_DATA="/var/lib/grafana"
ENV GF_PATHS_HOME="/usr/share/grafana"
ENV GF_PATHS_LOGS="/var/log/grafana"
ENV GF_PATHS_PLUGINS="/var/lib/grafana/plugins"
ENV GF_PATHS_PROVISIONING="/etc/grafana/provisioning"

ENTRYPOINT ["/run.sh"]
EXPOSE 3000
COPY run.sh /run.sh
RUN set -euo pipefail; chmod +x /run.sh
        
VOLUME /var/lib/grafana
