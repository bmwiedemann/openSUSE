#!ExclusiveArch: aarch64 x86_64 ppc64le s390x
# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/bci/openjdk:11
#!BuildTag: opensuse/bci/openjdk:11-%RELEASE%

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.openjdk
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI OpenJDK 11 runtime"
LABEL org.opencontainers.image.description="OpenJDK 11 runtime container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="11"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/bci/openjdk:11-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends java-11-openjdk; zypper -n clean; rm -rf /var/log/*
ENV JAVA_BINDIR="/usr/lib64/jvm/java-11-openjdk-11/bin"
ENV JAVA_HOME="/usr/lib64/jvm/java-11-openjdk-11"
ENV JAVA_ROOT="/usr/lib64/jvm/java-11-openjdk-11"
ENV JAVA_VERSION="11"

RUN set -euo pipefail; [ -d $JAVA_HOME ]; [ -d $JAVA_BINDIR ]; [ -f "$JAVA_BINDIR/java" ] && [ -x "$JAVA_BINDIR/java" ]
