# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/bci/golang:stable
#!BuildTag: opensuse/bci/golang:stable-1.%RELEASE%
#!BuildTag: opensuse/bci/golang:1.20
#!BuildTag: opensuse/bci/golang:1.20-1.%RELEASE%
#!BuildTag: opensuse/bci/golang:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.golang
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI Golang 1.20"
LABEL org.opencontainers.image.description="Golang 1.20 container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="1.20"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/bci/golang:1.20-1.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends go1.20 distribution-release make git-core; zypper -n clean; rm -rf /var/log/*
ENV GOLANG_VERSION="%%golang_version%%"
ENV GOPATH="/go"
ENV PATH="/go/bin:/usr/local/go/bin:/root/go/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

