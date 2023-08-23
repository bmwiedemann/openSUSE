# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/bci/python:3.9
#!BuildTag: opensuse/bci/python:3.9-%RELEASE%
#!BuildTag: opensuse/bci/python:3
#!BuildTag: opensuse/bci/python:3-%RELEASE%

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.python
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI Python 3.9 development"
LABEL org.opencontainers.image.description="Python 3.9 development container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="3.9"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/bci/python:3.9-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends python39-devel python39 python39-pip curl git-core python39-wheel; zypper -n clean; rm -rf /var/log/*
ENV PYTHON_VERSION="%%py39_ver%%"
ENV PIP_VERSION="%%pip_ver%%"

RUN set -euo pipefail; ln -s /usr/bin/python3.9 /usr/local/bin/python3; \
    ln -s /usr/bin/pydoc3.9 /usr/local/bin/pydoc
