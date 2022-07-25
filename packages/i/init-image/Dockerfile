# SPDX-License-Identifier: MIT
#!BuildTag: bci/bci-init:%OS_VERSION_ID_SP%
#!BuildTag: bci/bci-init:%OS_VERSION_ID_SP%.%RELEASE%
#!BuildTag: bci/bci-init:latest
FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.init
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI %OS_VERSION% Init Container Image"
LABEL org.opencontainers.image.description="Systemd environment for containers based on the SLE Base Container Image. This container is not supported when using container runtime other than podman."
LABEL org.opencontainers.image.version="%OS_VERSION_ID_SP%.%RELEASE%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opensuse.reference="registry.opensuse.org/bci/bci-init:%OS_VERSION_ID_SP%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"

LABEL com.suse.release-stage="released"
# endlabelprefix
LABEL usage="This container should only be used to build containers for daemons. Add your packages and enable services using systemctl."

RUN set -euo pipefail; zypper -n in --no-recommends systemd gzip; zypper -n clean; rm -rf /var/log/*



CMD ["/usr/lib/systemd/systemd"]
HEALTHCHECK --interval=5s --timeout=5s --retries=5     CMD ["/usr/bin/systemctl", "is-active", "multi-user.target"]
