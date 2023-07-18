# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/bci/nodejs:20
#!BuildTag: opensuse/bci/nodejs:20-%RELEASE%
#!BuildTag: opensuse/bci/nodejs:latest
#!BuildTag: opensuse/bci/node:20
#!BuildTag: opensuse/bci/node:20-%RELEASE%
#!BuildTag: opensuse/bci/node:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.nodejs
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI Node.js 20 development"
LABEL org.opencontainers.image.description="Node.js 20 development container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="20"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/bci/nodejs:20-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends nodejs20 npm20 git-core update-alternatives; zypper -n clean; rm -rf /var/log/*
ENV NODE_VERSION="20"

