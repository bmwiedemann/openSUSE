# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%.%RELEASE%

# virt-launcher container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="kubevirt virt-launcher container"
PREFIXEDLABEL org.opencontainers.image.description="Container to host VM processes for kubevirt"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%.%RELEASE%"

RUN zypper update -y && \
    zypper install -y \
           socat \
           qemu-x86 \
           qemu-tools \
           libcap-progs \
           mkisofs \
           nftables \
           iptables \
           augeas \
           augeas-lenses \
           libvirt-daemon-qemu \
           libvirt-client \
           libvirt-daemon-driver-storage-core \
           vim \
           kubevirt-container-disk \
           kubevirt-virt-launcher && \
     mkdir -p /usr/share/kubevirt/virt-launcher

COPY augconf /augconf

RUN augtool -f /augconf
RUN cd /var && rm -rf run && ln -s ../run .
RUN ln -s /usr/bin/mkisofs /usr/bin/genisoimage

ENTRYPOINT [ "/usr/bin/virt-launcher" ]
