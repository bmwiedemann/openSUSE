# SPDX-License-Identifier: Apache-2.0

# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# cdi-importer container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="CDI Data fetching service container"
LABEL org.opencontainers.image.description="Data fetching service for VM container images"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%.%RELEASE%"
LABEL com.suse.supportlevel="%%SUPPORT_LEVEL%%"
# endlabelprefix

RUN zypper -n install \
           containerized-data-importer-importer \
           curl \
           nbdkit-server \
           nbdkit-basic-filters \
           nbdkit-curl-plugin \
           nbdkit-xz-filter \
           qemu-img \
           shadow \
           tar \
           util-linux

# nbdkit-vddk-plugin is available only on x86_64
#!ArchExclusiveLine: x86_64
RUN if [ "$(uname -m)" = "x86_64" ]; then \
        zypper -n install nbdkit-vddk-plugin ; \
    fi;

RUN zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash cdi-importer

WORKDIR /home/cdi-importer
USER 1001
ENTRYPOINT [ "/usr/bin/virt-cdi-importer", "-alsologtostderr" ]
