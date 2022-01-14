# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-handler:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-handler:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/virt-handler:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# virt-handler container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="kubevirt virt-handler container"
PREFIXEDLABEL org.opencontainers.image.description="Virtualization handler for kubevirt"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-handler:%%PKG_VERSION%%.%RELEASE%"

RUN zypper -n install \
              curl \
              dbus-1 \
              iproute2 \
              iptables \
              kubevirt-container-disk \
              kubevirt-virt-handler \
              libvirt-client \
              lsscsi \
              qemu-tools \
              system-user-qemu \
              util-linux-systemd && \
    zypper clean -a

ENTRYPOINT [ "/usr/bin/virt-handler" ]
