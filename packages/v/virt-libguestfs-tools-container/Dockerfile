# Defines the tag for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/libguestfs-tools:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/libguestfs-tools:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/libguestfs-tools:%%PKG_VERSION%%-%%PKG_RELEASE%%

# libguestfs-tools container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# labelprefix=%%LABELPREFIX%%
PREFIXEDLABEL org.opencontainers.image.title="kubevirt libguestfs-tools container"
PREFIXEDLABEL org.opencontainers.image.description="Container for libguestfs tools"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/libguestfs-tools:%%PKG_VERSION%%.%RELEASE%"

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
              ldmtool \
              libguestfs \
              libguestfs-devel \
              mdadm \
              parted \
              qemu-tools \
              qemu-x86 \
              reiserfs \
              supermin \
              xfsprogs \
              xorriso \
              zerofree && \
    zypper clean -a

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

# Make a "fixed appliance" for libguestfs.
# Note: the resulting 'appliance/root' is a sparse file. Docker does not
# preserve sparseness hence a compressed tarball is created.
RUN LIBGUESTFS_BACKEND=direct \
    LIBGUESTFS_DEBUG=1 \
    libguestfs-make-fixed-appliance --xz && \
    rm -rf /var/tmp/.guestfs-*

ENTRYPOINT [ "/entrypoint.sh" ]
