# SPDX-License-Identifier: Apache-2.0

# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-operator:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-operator:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/virt-operator:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# virt-operator container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="kubevirt virt-operator container"
LABEL org.opencontainers.image.description="Virtualization operator for kubevirt"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-operator:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install kubevirt-virt-operator shadow && \
    zypper clean -a && \
    useradd --system --no-create-home -u 1001 virt-operator
USER 1001
ENTRYPOINT [ "/usr/bin/virt-operator" ]
