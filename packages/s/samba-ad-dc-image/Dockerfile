# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/samba-ad-dc:latest
#!BuildTag: opensuse/samba-ad-dc:%%MINOR%%
#!BuildTag: opensuse/samba-ad-dc:%%PKG_VERSION%%
#!BuildTag: opensuse/samba-ad-dc:%%PKG_VERSION%%-%RELEASE%

FROM opensuse/tumbleweed
LABEL maintainer="David Mulder <dmulder@suse.com>"

# labelprefix=org.opensuse.samba-ad-dc
LABEL org.opencontainers.image.title="Samba ADDC container"
LABEL org.opencontainers.image.description="Samba ADDC container"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%-%RELEASE%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/samba-ad-dc:%%PKG_VERSION%%-%RELEASE%"
# endlabelprefix

COPY entrypoint.sh /entrypoint.sh

RUN zypper --non-interactive install --no-recommends catatonit timezone system-user-mail system-user-nobody shadow samba-ad-dc krb5-server samba-winbind python3-dnspython && zypper clean && chmod 755 /entrypoint.sh
RUN mkdir -p /var/lib/samba-ad-dc/sysvol && chmod 755 /var/lib/samba-ad-dc/sysvol

EXPOSE 53/tcp
EXPOSE 53/udp
EXPOSE 88/tcp
EXPOSE 88/udp
EXPOSE 123/udp
EXPOSE 135/tcp
EXPOSE 137/udp
EXPOSE 138/udp
EXPOSE 139/tcp
EXPOSE 389/tcp
EXPOSE 389/udp
EXPOSE 445/tcp
EXPOSE 464/tcp
EXPOSE 636/tcp
EXPOSE 3268/tcp
EXPOSE 3269/tcp
EXPOSE 49152-65535/tcp

# The container must be run with `--cap-add SYS_ADMIN` otherwise acls will fail

ENTRYPOINT ["/usr/bin/catatonit", "--", "/entrypoint.sh"]
