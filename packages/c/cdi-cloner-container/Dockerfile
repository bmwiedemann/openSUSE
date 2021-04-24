# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-cloner:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-cloner:%%PKG_VERSION%%.%RELEASE%

# cdi-cloner container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="Cloner container for host assisted cloning"
PREFIXEDLABEL org.opencontainers.image.description="Source and Target cloner image for host assisted cloning"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/cdi-cloner:%%PKG_VERSION%%.%RELEASE%"

RUN zypper update -y && \
    zypper install -y \
           containerized-data-importer-cloner

ENTRYPOINT [ "/usr/bin/cloner_startup.sh" ]
