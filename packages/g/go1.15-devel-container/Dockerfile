# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/go-devel:15
#!BuildTag: opensuse/go-devel:%%PKG_VERSION%%
#!BuildTag: opensuse/go-devel:%%PKG_VERSION%%.%RELEASE%

FROM opensuse/tumbleweed

# labelprefix=org.opensuse.java-devel
PREFIXEDLABEL org.opencontainers.image.title="GO 15 development container"
PREFIXEDLABEL org.opencontainers.image.description="Environment for GO 15 development"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="opensuse/go-devel:%%PKG_VERSION%%.%RELEASE%"

# Work around https://github.com/openSUSE/obs-build/issues/487
RUN zypper install -y openSUSE-release-appliance-docker

# Development packages
RUN zypper install -y --no-recommends go1.15 git-core

ENTRYPOINT [ "/bin/bash" ]
