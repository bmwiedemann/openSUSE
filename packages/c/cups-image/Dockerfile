# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/cups:%PKG_VERSION%
#!BuildTag: opensuse/cups:latest
#!BuildTag: opensuse/cups:%PKG_VERSION%-%RELEASE%
FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.cups
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Cups Server Container Image"
LABEL org.opencontainers.image.description="Container containing CUPS from openSUSE Tumbleweed"
LABEL org.opencontainers.image.version="%PKG_VERSION%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/cups:%PKG_VERSION%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"

LABEL com.suse.release-stage="released"
# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends cups manufacturer-PPDs OpenPrintingPPDs; zypper -n clean; rm -rf /var/log/*

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/usr/sbin/cupsd", "-f"]

COPY docker-entrypoint.sh /usr/local/bin/
RUN set -euo pipefail; chmod 755 /usr/local/bin/docker-entrypoint.sh

# Add user and disable sudo password checking
RUN useradd \
  --groups=root \
  --create-home \
  --shell=/bin/bash \
  admin

# log to stderr
RUN set -euo pipefail; \
  sed -i -e "s|^AccessLog .*|AccessLog stderr|g" \
         -e "s|^ErrorLog .*|ErrorLog stderr|g" \
         -e "s|^PageLog .*|PageLog stderr|g" \
         /etc/cups/cups-files.conf

# enable access to CUPS
RUN set -euo pipefail; /usr/sbin/cupsd \
  && while [ ! -f /var/run/cups/cupsd.pid ]; do sleep 1; done \
  && cupsctl --remote-admin --remote-any --share-printers \
  && kill $(cat /var/run/cups/cupsd.pid) \
  && echo "ServerAlias *" >> /etc/cups/cupsd.conf

# copy /etc/cups for skeleton usage
RUN set -euo pipefail; cp -rp /etc/cups /etc/cups-skel

# volumes
VOLUME /etc/cups

# port
EXPOSE 631

