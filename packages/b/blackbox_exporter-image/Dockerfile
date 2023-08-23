# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/blackbox_exporter:%%blackbox_exporter_version%%
#!BuildTag: opensuse/blackbox_exporter:%%blackbox_exporter_version%%-%RELEASE%
#!BuildTag: opensuse/blackbox_exporter:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.blackbox_exporter
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Blackbox Exporter"
LABEL org.opencontainers.image.description="Blackbox Exporter container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%blackbox_exporter_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/blackbox_exporter:%%blackbox_exporter_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends prometheus-blackbox_exporter; zypper -n clean; rm -rf /var/log/*
ENTRYPOINT ["/usr/bin/blackbox_exporter"]
EXPOSE 9115
