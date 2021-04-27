# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/openjdk:14
#!BuildTag: opensuse/openjdk:%%PKG_VERSION%%
#!BuildTag: opensuse/openjdk:%%PKG_VERSION%%.%RELEASE%

ARG BASE=opensuse/tumbleweed
FROM $BASE

# labelprefix=org.opensuse.openjdk
PREFIXEDLABEL org.opencontainers.image.title="Java 14 development container"
PREFIXEDLABEL org.opencontainers.image.description="Environment for Java 14 development"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/openjdk:%%PKG_VERSION%%.%RELEASE%"

# Work around https://github.com/openSUSE/obs-build/issues/487
ARG RELEASE_PACKAGE=openSUSE-release-appliance-docker

ARG LIBDIR=/usr/lib64
ENV JAVA_BINDIR=$LIBDIR/jvm/java/bin
ENV JAVA_HOME=$LIBDIR/jvm/java
ENV JAVA_ROOT=$LIBDIR/jvm/java
ENV JAVA_VERSION=14

# Development packages
RUN zypper -n install --no-recommends $RELEASE_PACKAGE \
	java-14-openjdk-devel maven git-core && \
	zypper clean -a

CMD [ "jshell" ]
