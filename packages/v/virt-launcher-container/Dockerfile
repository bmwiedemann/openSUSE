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
# since TARGETARCH is not defined in OBS builds yet. Default to amd64.
ARG TARGETARCH=amd64

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="kubevirt virt-launcher container"
LABEL org.opencontainers.image.description="Container to host VM processes for kubevirt"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install \
              augeas \
              augeas-lenses \
              curl \
              ethtool \
              gawk \
              iptables \
              kubevirt-container-disk \
              kubevirt-virt-launcher \
              libcap-progs \
              libvirt-client \
              libvirt-daemon-driver-qemu \
              ncat \
              nftables \
              qemu-hw-usb-redirect \
              qemu-tools \
              socat \
              tar \
              timezone \
              vim-small \
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

RUN zypper clean -a

RUN ln -s ncat /usr/bin/nc

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

# KubeVirt expects virtiofsd to be installed in /usr/libexec
RUN ls /usr/libexec/virtiofsd || \
    (mkdir -p /usr/libexec && ln -s ../lib/virtiofsd /usr/libexec/virtiofsd)

COPY augconf /augconf

RUN augtool -f /augconf
RUN cd /var && rm -rf run && ln -s ../run .

# Setup permissions and capabilities for non-root VMIs. KubeVirt sets
# XDG_* directories to /var/run.
RUN setcap 'cap_net_bind_service,cap_sys_ptrace=+ep' /usr/bin/virt-launcher && \
    setcap 'cap_net_bind_service=+ep' /usr/bin/qemu-system-$(uname -m) && \
    chmod 0755 /etc/libvirt && \
    chown qemu:qemu /var/run

ENTRYPOINT [ "/usr/bin/virt-launcher" ]
