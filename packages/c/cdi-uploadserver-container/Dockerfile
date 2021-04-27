# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-uploadserver:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-uploadserver:%%PKG_VERSION%%.%RELEASE%

# cdi-uploadserver container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="CDI upload server container"
PREFIXEDLABEL org.opencontainers.image.description="Upload server for the data fetching service for VM container images"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/cdi-uploadserver:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install \
           qemu-tools qemu-block-curl tar util-linux \
           containerized-data-importer-uploadserver && \
    zypper clean -a

ENTRYPOINT [ "/usr/bin/virt-cdi-uploadserver", "-alsologtostderr" ]
