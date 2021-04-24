# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/cdi-operator:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/cdi-operator:%%PKG_VERSION%%.%RELEASE%

# cdi-operator container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="CDI operator service container"
PREFIXEDLABEL org.opencontainers.image.description="Operator for the data fetching service for VM container images"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/cdi-operator:%%PKG_VERSION%%.%RELEASE%"

RUN zypper update -y && \
    zypper install -y \
           containerized-data-importer-operator \
           shadow && \
    useradd -u 1001 --create-home -s /bin/bash cdi-operator
WORKDIR /home/cdi-operator
USER 1001
ENTRYPOINT [ "/usr/bin/virt-cdi-operator" ]
