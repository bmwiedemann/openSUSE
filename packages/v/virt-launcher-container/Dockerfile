# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%-%%PKG_RELEASE%%

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

RUN zypper -n install \
              augeas \
              augeas-lenses \
              iptables \
              kubevirt-container-disk \
              kubevirt-virt-launcher \
              libcap-progs \
              libvirt-client \
              libvirt-daemon-driver-storage-core \
              libvirt-daemon-qemu \
              mkisofs \
              nftables \
              qemu-tools \
              qemu-x86 \
              socat \
              vim && \
    zypper clean -a && \
    mkdir -p /usr/share/kubevirt/virt-launcher

RUN mkdir -p /usr/share/OVMF && \
    ln -s ../qemu/ovmf-x86_64-code.bin /usr/share/OVMF/OVMF_CODE.fd && \
    ln -s ../qemu/ovmf-x86_64-vars.bin /usr/share/OVMF/OVMF_VARS.fd && \
    ln -s ../qemu/ovmf-x86_64-smm-ms-code.bin /usr/share/OVMF/OVMF_CODE.secboot.fd && \
    ln -s ../qemu/ovmf-x86_64-smm-ms-vars.bin /usr/share/OVMF/OVMF_VARS.secboot.fd

COPY augconf /augconf

RUN augtool -f /augconf
RUN cd /var && rm -rf run && ln -s ../run .
RUN ln -s /usr/bin/mkisofs /usr/bin/genisoimage

ENTRYPOINT [ "/usr/bin/virt-launcher" ]
