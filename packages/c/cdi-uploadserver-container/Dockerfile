# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-uploadserver:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-uploadserver:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/cdi-uploadserver:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# cdi-uploadserver container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="CDI upload server container"
LABEL org.opencontainers.image.description="Upload server for the data fetching service for VM container images"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/cdi-uploadserver:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install \
           qemu-tools qemu-block-curl tar util-linux \
           containerized-data-importer-uploadserver && \
    zypper clean -a

ENTRYPOINT [ "/usr/bin/virt-cdi-uploadserver", "-alsologtostderr" ]
