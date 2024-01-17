# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/tomcat:latest
#!BuildTag: opensuse/tomcat:%%MINOR%%
#!BuildTag: opensuse/tomcat:%%PKG_VERSION%%
#!BuildTag: opensuse/tomcat:%%PKG_VERSION%%-%RELEASE%

FROM opensuse/tumbleweed

# labelprefix=org.opensuse.tomcat
PREFIXEDLABEL org.opencontainers.image.title="Apache tomcat container"
PREFIXEDLABEL org.opencontainers.image.description="Apache tomcat container"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%-%RELEASE%"
PREFIXEDLABEL org.opencontainers.image.vendor="openSUSE Project"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/tomcat:%%PKG_VERSION%%-%RELEASE%"

RUN zypper install -y --no-recommends tomcat && \
    zypper clean

USER tomcat

EXPOSE 8080
ENTRYPOINT ["/usr/libexec/tomcat/server", "start"]
