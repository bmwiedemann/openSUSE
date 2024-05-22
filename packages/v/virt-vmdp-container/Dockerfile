# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/vmdp:latest
#!BuildTag: %%TAGPREFIX%%/vmdp:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/vmdp:%%PKG_VERSION%%.%RELEASE%

#!ExclusiveArch: x86_64

# Hack: workaround for https://github.com/openSUSE/obs-build/issues/487
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

FROM scratch

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="VMDP container"
LABEL org.opencontainers.image.description="Container for Virtual Machine Driver Pack (VMDP) ISO"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.url="https://www.opensuse.org/"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/vmdp:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

ADD --chown=107:107 VMDP-WIN-%%PKG_VERSION%%-Community.iso /disk/
