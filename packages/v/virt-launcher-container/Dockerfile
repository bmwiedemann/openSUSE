# SPDX-License-Identifier: Apache-2.0

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

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="kubevirt virt-launcher container"
LABEL org.opencontainers.image.description="Container to host VM processes for kubevirt"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/virt-launcher:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install \
              curl \
              ethtool \
              gawk \
              iptables \
              kubevirt-container-disk \
              kubevirt-virt-launcher \
              libcap-progs \
              libvirt-client \
              libvirt-daemon-driver-qemu \
              netcat \
              nftables \
              procps \
              psmisc \
              qemu-hw-usb-host \
              qemu-hw-usb-redirect \
              qemu-img \
              socat \
              tar \
              timezone \
              vim-small \
              virtiofsd \
              xorriso

#!ArchExclusiveLine: x86_64
RUN if [ "$(uname -m)" = "x86_64" ]; then \
        zypper -n install qemu-x86 && \
        mkdir -p /usr/share/OVMF && \
        ln -s ../qemu/ovmf-x86_64-code.bin /usr/share/OVMF/OVMF_CODE.fd && \
        ln -s ../qemu/ovmf-x86_64-vars.bin /usr/share/OVMF/OVMF_VARS.fd && \
        ln -s ../qemu/ovmf-x86_64-code.bin /usr/share/OVMF/OVMF_CODE.cc.fd && \
        ln -s ../qemu/ovmf-x86_64-smm-ms-code.bin /usr/share/OVMF/OVMF_CODE.secboot.fd && \
        ln -s ../qemu/ovmf-x86_64-smm-ms-vars.bin /usr/share/OVMF/OVMF_VARS.secboot.fd ; \
    fi

#!ArchExclusiveLine: aarch64
RUN if [ "$(uname -m)" = "aarch64" ]; then \
        zypper -n install \
                  qemu-arm \
                  qemu-uefi-aarch64 && \
        mkdir -p /usr/share/AAVMF && \
        ln -s ../qemu/aavmf-aarch64-code.bin /usr/share/AAVMF/AAVMF_CODE.fd && \
        ln -s ../qemu/aavmf-aarch64-vars.bin /usr/share/AAVMF/AAVMF_VARS.fd ; \
    fi

RUN zypper clean -a

RUN cp -f /usr/share/kube-virt/virt-launcher/virtqemud.conf /etc/libvirt/virtqemud.conf && \
    cp -f /usr/share/kube-virt/virt-launcher/qemu.conf /etc/libvirt/qemu.conf

# KubeVirt expects virtiofsd to be installed in /usr/libexec
# NOTE: the value of %{_libexecdir} may vary across distros
RUN VIRTIOFSD=$(rpm --eval '%{_libexecdir}')/virtiofsd; \
    [ -d ${VIRTIOFSD} ] && VIRTIOFSD=${VIRTIOFSD}/virtiofsd; \
    [ -f /usr/libexec/virtiofsd ] || \
    (mkdir -p /usr/libexec && ln -svrt /usr/libexec ${VIRTIOFSD})

# Setup permissions and capabilities for non-root VMIs
RUN setcap 'cap_net_bind_service=+ep' /usr/bin/virt-launcher && \
    setcap 'cap_net_bind_service=+ep' /usr/bin/virt-launcher-monitor && \
    setcap 'cap_net_bind_service=+ep' /usr/bin/qemu-system-$(uname -m) && \
    chmod 0755 /etc/libvirt

RUN cd /var && rm -rf run && ln -s ../run .

ENTRYPOINT [ "/usr/bin/virt-launcher-monitor" ]
