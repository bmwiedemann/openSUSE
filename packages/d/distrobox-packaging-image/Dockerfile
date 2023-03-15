# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/distrobox-packaging:latest
#!BuildTag: opensuse/distrobox-packaging:%OS_VERSION_ID%
#!BuildTag: opensuse/distrobox-packaging:%OS_VERSION_ID%.%RELEASE%

#!ExclusiveArch: x86_64

FROM opensuse/distrobox:latest
LABEL maintainer="Richard Brown <rbrownsuse@opensuse.org>"

# labelprefix=org.opensuse.distrobox-packaging
PREFIXEDLABEL org.opencontainers.image.title="Distrobox openSUSE Packaging container"
PREFIXEDLABEL org.opencontainers.image.description="Distrobox openSUSE Packaging container"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%OS_VERSION_ID%.%RELEASE%"
PREFIXEDLABEL org.opencontainers.image.vendor="openSUSE Project"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/distrobox-packaging:%OS_VERSION_ID%.%RELEASE%"

# openSUSE-release included to ensure %OS_VERSION_ID% can be found/used by kiwi-metainfo-helper
RUN zypper --non-interactive install --no-recommends git \
    osc \
    build \
    vim \
    vim-data \
    scout-command-not-found \
    obs-service-download_files \
    obs-service-tar \
    obs-service-tar_scm \
    obs-service-obs_scm \
    obs-service-set_version \
    obs-service-recompress \
    obs-service-go_modules \
    obs-service-product_converter \
    obs-service-format_spec_file \
    osc-plugin-cycle \
    osc-plugin-origin \
    osc-plugin-staging \
    openSUSE-release-tools-pkglistgen \
    openSUSE-release-tools \
    openSUSE-release \
  && zypper clean
