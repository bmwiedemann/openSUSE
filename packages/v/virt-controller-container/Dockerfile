# Defines the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-controller:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-controller:%%PKG_VERSION%%.%RELEASE%

# virt-controller container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="kubevirt virt-controller container"
PREFIXEDLABEL org.opencontainers.image.description="Virtualization controller for kubevirt"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/virt-controller:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install kubevirt-virt-controller shadow && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash virt-controller
USER 1001
ENTRYPOINT [ "/usr/bin/virt-controller" ]
