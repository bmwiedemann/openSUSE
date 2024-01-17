# SPDX-License-Identifier: Apache-2.0

# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-exportproxy:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-exportproxy:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/virt-exportproxy:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# virt-exportproxy container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="kubevirt virt-exportproxy container"
LABEL org.opencontainers.image.description="Export proxy for the VirtualMachineExport resources"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-exportproxy:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install kubevirt-virt-exportproxy shadow && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash virt-exportproxy
USER 1001
ENTRYPOINT [ "/usr/bin/virt-exportproxy" ]
