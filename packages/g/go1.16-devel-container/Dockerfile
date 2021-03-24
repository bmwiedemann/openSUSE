# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/golang:1.16
#!BuildTag: opensuse/golang:%%PKG_VERSION%%
#!BuildTag: opensuse/golang:%%PKG_VERSION%%.%RELEASE%

FROM opensuse/tumbleweed

# labelprefix=org.opensuse.golang
PREFIXEDLABEL org.opencontainers.image.title="Go 1.16 development container"
PREFIXEDLABEL org.opencontainers.image.description="Environment for Go 1.16 development"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/golang:%%PKG_VERSION%%.%RELEASE%"

# Work around https://github.com/openSUSE/obs-build/issues/487
RUN zypper install -y openSUSE-release-appliance-docker

# Development packages
RUN zypper install -y --no-recommends go1.16 git-core

ENTRYPOINT [ "/bin/bash" ]
