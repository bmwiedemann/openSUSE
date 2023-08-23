# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/rmt-server:%%rmt_version%%
#!BuildTag: opensuse/rmt-server:%%rmt_version%%-%RELEASE%
#!BuildTag: opensuse/rmt-server:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.rmt-server
LABEL org.opencontainers.image.title="openSUSE Tumbleweed SUSE RMT Server"
LABEL org.opencontainers.image.description="SUSE RMT Server container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%rmt_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/rmt-server:%%rmt_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends rmt-server catatonit; zypper -n clean; rm -rf /var/log/*
ENV RAILS_ENV="production"
ENV LANG="en"

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/usr/share/rmt/bin/rails", "server", "-e", "production"]
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN set -euo pipefail; chmod +x /usr/local/bin/entrypoint.sh
