# SPDX-License-Identifier: Apache-2.0

# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-uploadproxy:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-uploadproxy:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/cdi-uploadproxy:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# cdi-uploadproxy container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="CDI uploadproxy container"
LABEL org.opencontainers.image.description="Upload proxy for the data fetching service for VM container images"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/cdi-uploadproxy:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install \
           containerized-data-importer-uploadproxy \
           shadow && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash cdi-uploadproxy
WORKDIR /home/cdi-uploadproxy
USER 1001
ENTRYPOINT [ "/usr/bin/virt-cdi-uploadproxy", "-alsologtostderr" ]
