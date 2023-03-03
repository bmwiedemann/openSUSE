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

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="kubevirt virt-handler container"
LABEL org.opencontainers.image.description="Virtualization handler for kubevirt"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-handler:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install \
              curl \
              iproute2 \
              iptables \
              kubevirt-container-disk \
              kubevirt-virt-handler \
              lsscsi \
              nftables \
              qemu-tools \
              system-user-qemu \
              tar \
              util-linux-systemd && \
    zypper clean -a

RUN cp -f /usr/share/kube-virt/virt-handler/nsswitch.conf /etc/ && \
    cp -f /usr/share/kube-virt/virt-handler/virt_launcher.cil /

ENTRYPOINT [ "/usr/bin/virt-handler" ]
