# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# virt-launcher container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM
# TARGETARCH defined in prjconf, to handle architecture specific bits
# since TARGETARCH is not defined in OBS builds yet.
ARG TARGETARCH

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="kubevirt virt-launcher container"
PREFIXEDLABEL org.opencontainers.image.description="Container to host VM processes for kubevirt"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%.%RELEASE%"

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
              nftables \
              qemu-tools \
              socat \
              tar \
              timezone \
              vim \
              xorriso
#!ArchExclusiveLine: x86_64
RUN if [ "$TARGETARCH" = "amd64" ]; then \
              zypper -n install qemu-x86 ; \
              fi;

#!ArchExclusiveLine: aarch64
RUN if [ "$TARGETARCH" = "arm64" ]; then \
              zypper -n install \
              qemu-arm \
              qemu-uefi-aarch64 ; \
              fi;

RUN zypper clean -a && \
    mkdir -p /usr/share/kubevirt/virt-launcher

RUN mkdir -p /usr/share/OVMF

#!ArchExclusiveLine: x86_64
RUN if [ "$TARGETARCH" = "amd64" ]; then \
    ln -s ../qemu/ovmf-x86_64-code.bin /usr/share/OVMF/OVMF_CODE.fd && \
    ln -s ../qemu/ovmf-x86_64-vars.bin /usr/share/OVMF/OVMF_VARS.fd && \
    ln -s ../qemu/ovmf-x86_64-code.bin /usr/share/OVMF/OVMF_CODE.cc.fd && \
    ln -s ../qemu/ovmf-x86_64-smm-ms-code.bin /usr/share/OVMF/OVMF_CODE.secboot.fd && \
    ln -s ../qemu/ovmf-x86_64-smm-ms-vars.bin /usr/share/OVMF/OVMF_VARS.secboot.fd ; \
    fi;

#!ArchExclusiveLine: aarch64
RUN if [ "$TARGETARCH" = "arm64" ]; then \
    ln -s ../qemu/aavmf-aarch64-code.bin /usr/share/OVMF/AAVMF_CODE.fd && \
    ln -s ../qemu/aavmf-aarch64-vars.bin /usr/share/OVMF/AAVMF_VARS.fd ; \
    fi;

COPY augconf /augconf

RUN augtool -f /augconf
RUN cd /var && rm -rf run && ln -s ../run .

ENTRYPOINT [ "/usr/bin/virt-launcher" ]
