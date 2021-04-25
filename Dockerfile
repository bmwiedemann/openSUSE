# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-operator:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-operator:%%PKG_VERSION%%.%RELEASE%

# virt-operator container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="kubevirt virt-operator container"
PREFIXEDLABEL org.opencontainers.image.description="Virtualization operator for kubevirt"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/virt-operator:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install kubevirt-virt-operator shadow && \
    zypper clean -a && \
    useradd --system --no-create-home -u 1001 virt-operator
USER 1001
ENTRYPOINT [ "/usr/bin/virt-operator" ]
