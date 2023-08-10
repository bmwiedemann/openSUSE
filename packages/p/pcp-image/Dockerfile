# SPDX-License-Identifier: (LGPL-2.1+ AND GPL-2.0+)
#!BuildTag: opensuse/pcp:%%pcp_patch%%
#!BuildTag: opensuse/pcp:%%pcp_patch%%-%RELEASE%
#!BuildTag: opensuse/pcp:%%pcp_minor%%
#!BuildTag: opensuse/pcp:%%pcp_minor%%-%RELEASE%
#!BuildTag: opensuse/pcp:%%pcp_major%%
#!BuildTag: opensuse/pcp:%%pcp_major%%-%RELEASE%
#!BuildTag: opensuse/pcp:latest

FROM opensuse/bci/bci-init:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.pcp
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Performance Co-Pilot (pcp)"
LABEL org.opencontainers.image.description="Performance Co-Pilot (pcp) container based on the openSUSE Tumbleweed Base Container Image. This container is only supported with podman."
LABEL org.opencontainers.image.version="%%pcp_patch%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/pcp:%%pcp_patch%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends pcp hostname shadow gettext-runtime util-linux-systemd; zypper -n clean; rm -rf /var/log/*
ENTRYPOINT ["/usr/local/bin/container-entrypoint"]
CMD ["/usr/lib/systemd/systemd"]
EXPOSE 44321 44322 44323

RUN set -euo pipefail; mkdir -p /usr/share/container-scripts/pcp; mkdir -p /etc/sysconfig
COPY container-entrypoint healthcheck /usr/local/bin/
RUN set -euo pipefail; chmod +x /usr/local/bin/container-entrypoint /usr/local/bin/healthcheck
COPY pmproxy.conf.template 10-host_mount.conf.template /usr/share/container-scripts/pcp/
COPY pmcd pmlogger /etc/sysconfig/

# This can be removed after the pcp dependency on sysconfig is removed
RUN set -euo pipefail; systemctl disable wicked wickedd || :

HEALTHCHECK --start-period=30s --timeout=20s --interval=10s --retries=3     CMD /usr/local/bin/healthcheck

VOLUME /var/log/pcp/pmlogger
