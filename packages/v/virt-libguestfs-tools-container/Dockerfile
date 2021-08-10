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
              mdadm \
              parted \
              qemu-tools \
              qemu-x86 \
              reiserfs \
              xfsprogs \
              xorriso \
              zerofree && \
    zypper clean -a

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
