# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/alertmanager:%%alertmanager_version%%
#!BuildTag: opensuse/alertmanager:%%alertmanager_version%%-%RELEASE%
#!BuildTag: opensuse/alertmanager:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.alertmanager
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Alertmanager"
LABEL org.opencontainers.image.description="Alertmanager container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%alertmanager_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/alertmanager:%%alertmanager_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends golang-github-prometheus-alertmanager; zypper -n clean; rm -rf /var/log/*
ENTRYPOINT ["/usr/bin/prometheus-alertmanager"]
EXPOSE 9093

VOLUME /var/lib/prometheus/alertmanager
