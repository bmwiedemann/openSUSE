# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# cdi-importer container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM
# TARGETARCH defined in prjconf, to handle architecture specific bits
# since TARGETARCH is not defined in OBS builds yet. Default to amd64.
ARG TARGETARCH=amd64

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="CDI Data fetching service container"
PREFIXEDLABEL org.opencontainers.image.description="Data fetching service for VM container images"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/cdi-importer:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install \
           qemu-tools qemu-block-curl skopeo tar util-linux \
           nbdkit nbdkit-basic-filters nbdkit-gzip-filter \
           nbdkit-xz-filter nbdkit-curl-plugin \
           containerized-data-importer-importer

# nbdkit-vddk-plugin is available only on x86_64
#!ArchExclusiveLine: x86_64
RUN if [ "$TARGETARCH" = "amd64" ]; then \
              zypper -n install nbdkit-vddk-plugin ; \
              fi;

RUN zypper clean -a

ENTRYPOINT [ "/usr/bin/virt-cdi-importer", "-alsologtostderr" ]
