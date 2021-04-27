# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-controller:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-controller:%%PKG_VERSION%%.%RELEASE%

# cdi-controller container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="Controller container for CDI"
PREFIXEDLABEL org.opencontainers.image.description="Controller for the data fetching service for VM container images"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/cdi-controller:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install \
           containerized-data-importer-controller \
           shadow && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash cdi-controller
WORKDIR /home/cdi-controller
USER 1001
ENTRYPOINT [ "/usr/bin/virt-cdi-controller", "-alsologtostderr" ]
