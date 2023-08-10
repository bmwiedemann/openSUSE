# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/389-ds:%%389ds_version%%
#!BuildTag: opensuse/389-ds:%%389ds_version%%-%RELEASE%
#!BuildTag: opensuse/389-ds:latest

FROM opensuse/tumbleweed:latest

MAINTAINER william.brown@suse.com

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.389-ds
LABEL org.opencontainers.image.title="openSUSE Tumbleweed 389 Directory Server"
LABEL org.opencontainers.image.description="389 Directory Server container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%389ds_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/389-ds:%%389ds_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends 389-ds timezone openssl nss_synth; zypper -n clean; rm -rf /var/log/*
CMD ["/usr/lib/dirsrv/dscontainer", "-r"]
EXPOSE 3389 3636

COPY nsswitch.conf /etc/nsswitch.conf

RUN set -euo pipefail; mkdir -p /data/config; \
    mkdir -p /data/ssca; \
    mkdir -p /data/run; \
    mkdir -p /var/run/dirsrv; \
    ln -s /data/config /etc/dirsrv/slapd-localhost; \
    ln -s /data/ssca /etc/dirsrv/ssca; \
    ln -s /data/run /var/run/dirsrv

HEALTHCHECK --start-period=5m --timeout=5s --interval=5s --retries=2 \
    CMD /usr/lib/dirsrv/dscontainer -H

VOLUME /data
