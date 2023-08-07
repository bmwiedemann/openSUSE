# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/nginx:%%nginx_version%%
#!BuildTag: opensuse/nginx:%%nginx_version%%-%RELEASE%
#!BuildTag: opensuse/nginx:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.nginx
LABEL org.opencontainers.image.title="openSUSE Tumbleweed NGINX"
LABEL org.opencontainers.image.description="NGINX open source all-in-one load balancer, content cache and web server based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%nginx_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/nginx:%%nginx_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends gawk nginx; zypper -n clean; rm -rf /var/log/*
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
EXPOSE 80
RUN set -euo pipefail; mkdir /docker-entrypoint.d
COPY [1-3]0-*.sh /docker-entrypoint.d/
COPY docker-entrypoint.sh /usr/local/bin
COPY index.html /srv/www/htdocs/
RUN set -euo pipefail; chmod +x /docker-entrypoint.d/*.sh /usr/local/bin/docker-entrypoint.sh
RUN set -euo pipefail; install -d -o nginx -g nginx -m 750 /var/log/nginx;     ln -sf /dev/stdout /var/log/nginx/access.log;     ln -sf /dev/stderr /var/log/nginx/error.log

STOPSIGNAL SIGQUIT
