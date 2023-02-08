# Defines the tag for OBS and build script builds:
#!BuildTag: opensuse/samba-server:latest
#!BuildTag: opensuse/samba-server:%%MINOR%%
#!BuildTag: opensuse/samba-server:%%PKG_VERSION%%
#!BuildTag: opensuse/samba-server:%%PKG_VERSION%%-%RELEASE%

FROM opensuse/tumbleweed
LABEL maintainer="David Mulder <dmulder@suse.com>"

# labelprefix=org.opensuse.samba-server
LABEL org.opencontainers.image.title="Samba container"
LABEL org.opencontainers.image.description="Samba container"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%-%RELEASE%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/samba-server:%%PKG_VERSION%%-%RELEASE%"
# endlabelprefix

COPY smb.conf /etc/samba/smb.conf
RUN zypper --non-interactive install --no-recommends \
  findutils \
  python3-pip \
  python3-jsonschema \
  samba-python3 \
  python3-pyxattr \
  samba \
  samba-winbind \
  tdb-tools \
  ctdb \
  sambacc
RUN ln -sf /usr/share/sambacc/examples/minimal.json /etc/samba/container.json
COPY nsswitch.conf /etc/nsswitch.conf


VOLUME ["/share"]

EXPOSE 445

ENV SAMBACC_CONFIG="/etc/samba/container.json:/etc/samba/users.json"
ENV SAMBA_CONTAINER_ID="demo"
ENV SAMBA_SPECIFICS="daemon_cli_debug_output"
ENTRYPOINT ["samba-container"]
CMD ["run", "smbd"]

# vim:set syntax=dockerfile:
