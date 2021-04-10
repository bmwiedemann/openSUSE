# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/samba:latest
#!BuildTag: opensuse/samba:%%MINOR%%
#!BuildTag: opensuse/samba:%%PKG_VERSION%%
#!BuildTag: opensuse/samba:%%PKG_VERSION%%-%RELEASE%

FROM opensuse/tumbleweed
LABEL maintainer="Bruno Leon <bruno.leon@suse.com>"

# labelprefix=org.opensuse.samba
PREFIXEDLABEL org.opencontainers.image.title="Samba container"
PREFIXEDLABEL org.opencontainers.image.description="Samba container"
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%%PKG_VERSION%%-%RELEASE%"
PREFIXEDLABEL org.opencontainers.image.vendor="openSUSE Project"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/samba:%%PKG_VERSION%%-%RELEASE%"

COPY entrypoint.sh /entrypoint.sh

RUN zypper --non-interactive install --no-recommends catatonit timezone system-user-mail shadow samba && zypper clean && chmod 755 /entrypoint.sh

EXPOSE 137/udp 138/udp 139 445

HEALTHCHECK --interval=60s --timeout=15s \
            CMD smbclient -L \\localhost -U % -m SMB3

ENTRYPOINT ["/usr/bin/catatonit", "--", "/entrypoint.sh"]
