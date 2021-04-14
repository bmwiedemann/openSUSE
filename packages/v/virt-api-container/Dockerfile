# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-api:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-api:%%PKG_VERSION%%.%RELEASE%

# virt-api container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="kubevirt virt-api container"
PREFIXEDLABEL org.opencontainers.image.description="Entrypoint for all kubevirt CR exentions"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/virt-api:%%PKG_VERSION%%.%RELEASE%"

RUN zypper update -y && \
    zypper install -y \
           kubevirt-virt-api \
           shadow && \
    useradd -u 1001 --create-home -s /bin/bash virt-api
USER 1001
ENTRYPOINT [ "/usr/bin/virt-api" ]
