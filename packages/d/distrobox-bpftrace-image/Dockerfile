# SPDX-License-Identifier: Apache-2.0
#!BuildTag: opensuse/distrobox-bpftrace:latest
#!BuildTag: opensuse/distrobox-bpftrace:%OS_VERSION_ID%
#!BuildTag: opensuse/distrobox-bpftrace:%OS_VERSION_ID%.%RELEASE%

#!ExclusiveArch: x86_64

FROM opensuse/distrobox:latest
LABEL maintainer="Alessio Biancalana <dottorblaster@opensuse.org>"

# labelprefix=org.opensuse.distrobox-bpftrace
PREFIXEDLABEL org.opencontainers.image.title="Distrobox openSUSE bpftrace container"
PREFIXEDLABEL org.opencontainers.image.description="Distrobox openSUSE bpftrace container"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%OS_VERSION_ID%.%RELEASE%"
PREFIXEDLABEL org.opencontainers.image.vendor="openSUSE Project"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/distrobox-bpftrace:%OS_VERSION_ID%.%RELEASE%"


# openSUSE-release included to ensure %OS_VERSION_ID% can be found/used by kiwi-metainfo-helper
RUN zypper --non-interactive install --no-recommends bpftrace \
    kernel-devel \
    kernel-syms \
  && zypper clean

