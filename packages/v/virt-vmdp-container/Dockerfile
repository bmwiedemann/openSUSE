# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/vmdp:latest
#!BuildTag: %%TAGPREFIX%%/vmdp:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/vmdp:%%PKG_VERSION%%.%RELEASE%

FROM scratch

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="VMDP container"
PREFIXEDLABEL org.opencontainers.image.description="Container for Virtual Machine Driver Pack (VMDP) ISO"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/vmdp:%%PKG_VERSION%%.%RELEASE%"

ADD --chown=107:107 vmdp-att-%%PKG_VERSION%%.iso /disk/
