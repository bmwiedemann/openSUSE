# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-apiserver:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-apiserver:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/cdi-apiserver:%%PKG_VERSION%%-%%PKG_RELEASE%%

# cdi-apiserver container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="CDI API server container"
PREFIXEDLABEL org.opencontainers.image.description="Kubernetes API extension for CDI"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/cdi-apiserver:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install \
           containerized-data-importer-api \
           shadow && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash cdi-apiserver
WORKDIR /home/cdi-apiserver
USER 1001
ENTRYPOINT [ "/usr/bin/virt-cdi-apiserver", "-alsologtostderr" ]
