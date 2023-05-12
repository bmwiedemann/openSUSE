# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-cloner:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-cloner:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/cdi-cloner:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# cdi-cloner container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="Cloner container for host assisted cloning"
LABEL org.opencontainers.image.description="Source and Target cloner image for host assisted cloning"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/cdi-cloner:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install \
           containerized-data-importer-cloner \
           curl \
           shadow \
           tar \
           util-linux && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash cdi-cloner

WORKDIR /usr/bin
USER 1001
ENTRYPOINT [ "/usr/bin/cloner_startup.sh" ]
