# SPDX-License-Identifier: Apache-2.0

# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-synchronization-controller:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-synchronization-controller:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/virt-synchronization-controller:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# virt-synchronization-controller container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="kubevirt virt-synchronization-controller container"
LABEL org.opencontainers.image.description="Synchronization controller for decentralized migration"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-synchronization-controller:%%PKG_VERSION%%.%RELEASE%"
LABEL com.suse.supportlevel="%%SUPPORT_LEVEL%%"
# endlabelprefix

RUN zypper -n install kubevirt-virt-synchronization-controller shadow && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash virt-synchronization-controller
USER 1001
ENTRYPOINT [ "/usr/bin/virt-synchronization-controller" ]
