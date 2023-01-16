# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/libguestfs-tools:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/libguestfs-tools:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/libguestfs-tools:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# libguestfs-tools container image
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
LABEL org.opencontainers.image.title="kubevirt libguestfs-tools container"
LABEL org.opencontainers.image.description="Container for libguestfs tools"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/libguestfs-tools:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

# Note: the trick with install/remove kubevirt-manifests is needed to ensure
# that OBS triggers the rebuild of the container whenever the main kubevirt
# package is updated. Even though there is no direct dependency on the RPM
# itself, we still need to add proper tags. Having a reference to the build
# service obs-service-kubevirt_containers_meta in the _service file apparently
# is not enough.
RUN zypper -n install \
              bash \
              btrfsprogs \
              cryptsetup \
              dosfstools \
              e2fsprogs \
              gptfdisk \
              guestfs-data \
              guestfs-tools \
              guestfs-winsupport \
              jfsutils \
              kernel-kvmsmall \
              kubevirt-manifests \
              ldmtool \
              libguestfs \
              libguestfs-devel \
              mdadm \
              parted \
              qemu-tools \
              shadow \
              supermin \
              xfsprogs \
              xorriso \
              zerofree

#!ArchExclusiveLine: x86_64
RUN if [ "$TARGETARCH" = "amd64" ]; then \
              zypper -n install qemu-x86 ; \
              fi;

# qemu-x86 is required on aarch64 to get the test to pass (allow fallback to non KVM mode)
#!ArchExclusiveLine: aarch64
RUN if [ "$TARGETARCH" = "arm64" ]; then \
              zypper -n install qemu-arm qemu-uefi-aarch64 qemu-x86; \
              fi;

RUN zypper -n remove kubevirt-manifests && \
    zypper clean -a && \
    useradd -u 1001 --create-home -s /bin/bash virt-libguestfs-tools

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

# Make a "fixed appliance" for libguestfs.
# Note: the resulting 'appliance/root' is a sparse file. Docker does not
# preserve sparseness hence a compressed tarball is created.
RUN LIBGUESTFS_BACKEND=direct \
    LIBGUESTFS_DEBUG=1 \
    libguestfs-make-fixed-appliance --xz && \
    mv appliance-*.tar.xz appliance.tar.xz && \
    rm -rf /var/tmp/.guestfs-*

USER 1001
ENTRYPOINT [ "/entrypoint.sh" ]
