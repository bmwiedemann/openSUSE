# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-exportserver:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-exportserver:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/virt-exportserver:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# virt-exportserver container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="kubevirt virt-exportserver container"
PREFIXEDLABEL org.opencontainers.image.description="HTTP server for the VirtualMachineExport resources"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-exportserver:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install kubevirt-virt-exportserver shadow tar && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash virt-exportserver
USER 1001
ENTRYPOINT [ "/usr/bin/virt-exportserver" ]
