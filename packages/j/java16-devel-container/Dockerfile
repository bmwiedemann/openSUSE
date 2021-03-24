# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/openjdk:16
#!BuildTag: opensuse/openjdk:%%PKG_VERSION%%
#!BuildTag: opensuse/openjdk:%%PKG_VERSION%%.%RELEASE%

ARG BASE=opensuse/tumbleweed
FROM $BASE

# labelprefix=org.opensuse.openjdk
PREFIXEDLABEL org.opencontainers.image.title="Java 16 development container"
PREFIXEDLABEL org.opencontainers.image.description="Environment for Java 16 development"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/openjdk:%%PKG_VERSION%%.%RELEASE%"

# Work around https://github.com/openSUSE/obs-build/issues/487
ARG RELEASE_PACKAGE=openSUSE-release-appliance-docker
RUN zypper install -y $RELEASE_PACKAGE

# Development packages
RUN zypper install -y --no-recommends java-16-openjdk-devel maven git-core

ENTRYPOINT [ "/bin/bash" ]
