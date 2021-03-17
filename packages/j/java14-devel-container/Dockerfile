# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/java-devel:14
#!BuildTag: opensuse/java-devel:%%PKG_VERSION%%
#!BuildTag: opensuse/java-devel:%%PKG_VERSION%%.%RELEASE%

FROM opensuse/tumbleweed

# labelprefix=org.opensuse.java-devel
PREFIXEDLABEL org.opencontainers.image.title="Java 14 development container"
PREFIXEDLABEL org.opencontainers.image.description="Environment for Java 14 development"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="opensuse/java-devel:%%PKG_VERSION%%.%RELEASE%"

# Work around https://github.com/openSUSE/obs-build/issues/487
RUN zypper install -y openSUSE-release-appliance-docker

# Development packages
RUN zypper install -y --no-recommends java-14-openjdk-devel maven git-core

