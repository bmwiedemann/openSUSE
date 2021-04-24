# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-uploadproxy:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-uploadproxy:%%PKG_VERSION%%.%RELEASE%

# cdi-uploadproxy container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="CDI uploadproxy container"
PREFIXEDLABEL org.opencontainers.image.description="Upload proxy for the data fetching service for VM container images"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/cdi-uploadproxy:%%PKG_VERSION%%.%RELEASE%"

RUN zypper update -y && \
    zypper install -y \
           containerized-data-importer-uploadproxy \
           shadow && \
    useradd -u 1001 --create-home -s /bin/bash cdi-uploadproxy
WORKDIR /home/cdi-uploadproxy
USER 1001
ENTRYPOINT [ "/usr/bin/virt-cdi-uploadproxy", "-alsologtostderr" ]
