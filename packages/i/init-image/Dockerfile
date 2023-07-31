# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/bci/bci-init:%OS_VERSION_ID_SP%
#!BuildTag: opensuse/bci/bci-init:%OS_VERSION_ID_SP%.%RELEASE%
#!BuildTag: opensuse/bci/bci-init:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.init
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI openSUSE Tumbleweed Init"
LABEL org.opencontainers.image.description="Systemd environment for containers based on the openSUSE Tumbleweed Base Container Image. This container is only supported with podman."
LABEL org.opencontainers.image.version="%OS_VERSION_ID_SP%.%RELEASE%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/bci/bci-init:%OS_VERSION_ID_SP%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix
LABEL usage="This container should only be used to build containers for daemons. Add your packages and enable services using systemctl."

RUN set -euo pipefail; zypper -n in --no-recommends systemd gzip; zypper -n clean; rm -rf /var/log/*
CMD ["/usr/lib/systemd/systemd"]

RUN mkdir -p /etc/systemd/system.conf.d/ && \
    printf "[Manager]\nLogColor=no" > \
        /etc/systemd/system.conf.d/01-sle-bci-nocolor.conf
RUN systemctl disable getty@tty1.service
HEALTHCHECK --interval=5s --timeout=5s --retries=5 CMD ["/usr/bin/systemctl", "is-active", "multi-user.target"]
