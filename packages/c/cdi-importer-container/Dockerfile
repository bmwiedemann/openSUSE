# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%.%RELEASE%

# cdi-importer container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="CDI Data fetching service container"
PREFIXEDLABEL org.opencontainers.image.description="Data fetching service for VM container images"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install \
           qemu-tools qemu-block-curl skopeo tar util-linux \
           nbdkit nbdkit-basic-filters nbdkit-gzip-filter \
           nbdkit-xz-filter nbdkit-curl-plugin nbdkit-vddk-plugin \
           containerized-data-importer-importer && \
    zypper clean -a

ENTRYPOINT [ "/usr/bin/virt-cdi-importer", "-alsologtostderr" ]
