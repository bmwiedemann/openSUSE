# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/distrobox:latest
#!BuildTag: opensuse/distrobox:%OS_VERSION_ID%
#!BuildTag: opensuse/distrobox:%OS_VERSION_ID%.%RELEASE%

#!ExclusiveArch: x86_64

FROM opensuse/tumbleweed:latest
LABEL maintainer="Richard Brown <rbrownsuse@opensuse.org>"

# labelprefix=org.opensuse.distrobox
PREFIXEDLABEL org.opencontainers.image.title="Distrobox base container"
PREFIXEDLABEL org.opencontainers.image.description="Distrobox base container"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%OS_VERSION_ID%.%RELEASE%"
PREFIXEDLABEL org.opencontainers.image.vendor="openSUSE Project"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/distrobox:%OS_VERSION_ID%.%RELEASE%"

# Packagelist from https://github.com/89luca89/distrobox/blob/main/docs/distrobox_custom.md
# openSUSE-release included explicitly to ensure kiwi-metainfo-helper finds it for %OS_VERSION_ID%
RUN zypper --non-interactive install --no-recommends bash \
    Mesa-dri \
    bash-completion \
    bc \
    bzip2 \
    curl \
    diffutils \
    findutils \
    glibc-locale \
    glibc-locale-base \
    gnupg \
    host-spawn \
    hostname \
    iputils \
    keyutils \
    less \
    libvte-2_91-0 \
    libvulkan1 \
    libvulkan_intel \
    libvulkan_radeon \
    lsof \
    man \
    man-pages \
    mtr \
    ncurses \
    nss-mdns \
    openSUSE-release \
    openssh-clients \
    pam \
    pam-extra \
    pigz \
    pinentry \
    procps \
    rsync \
    shadow \
    sudo \
    system-group-wheel \
    systemd \
    time \
    timezone \
    tree \
    unzip \
    util-linux \
    util-linux-systemd \
    vte \
    wget \
    words \
    xauth \
    zip \
  && zypper al parallel-printer-support \
  && zypper clean \
  && sed -i 's/.*solver.onlyRequires.*/solver.onlyRequires = false/g' /etc/zypp/zypp.conf \
  && sed -i 's/.*rpm.install.excludedocs.*/rpm.install.excludedocs = no/g' /etc/zypp/zypp.conf
