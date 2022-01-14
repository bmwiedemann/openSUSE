# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/vmdp:latest
#!BuildTag: %%TAGPREFIX%%/vmdp:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/vmdp:%%PKG_VERSION%%.%RELEASE%

#!ExclusiveArch: x86_64

# Hack: workaround for https://github.com/openSUSE/obs-build/issues/487
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

FROM scratch

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="VMDP container"
PREFIXEDLABEL org.opencontainers.image.description="Container for Virtual Machine Driver Pack (VMDP) ISO"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.opencontainers.image.vendor="openSUSE Project"
PREFIXEDLABEL org.opencontainers.image.url="https://www.opensuse.org/"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/vmdp:%%PKG_VERSION%%.%RELEASE%"

ADD --chown=107:107 VMDP-WIN-%%PKG_VERSION%%-Community.iso /disk/
