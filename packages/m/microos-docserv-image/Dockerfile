# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/microos-docserv:%PKG_VERSION%
#!BuildTag: opensuse/microos-docserv:latest
#!BuildTag: opensuse/microos-docserv:%PKG_VERSION%-%RELEASE%
#!UseOBSRepositories
#!ExcludeArch: i586 s390 armv6l armv6hl

FROM opensuse/tumbleweed AS build-stage
WORKDIR /src
COPY microos.yaml /src/
RUN zypper --non-interactive install --no-recommends mandoc cpio rpm2docserv docserv-auxserver docserv-config-nginx openssl && zypper clean
RUN zypper --disable-system-resolvables --non-interactive  --pkg-cache-dir=/var/cache/rpm2docserv install --recommends --auto-agree-with-licenses --auto-agree-with-product-licenses --download-only patterns-base-documentation patterns-base-enhanced_base patterns-base-sw_management patterns-containers-container_runtime patterns-microos-base-zypper patterns-microos-basesystem patterns-microos-cloud patterns-microos-cockpit patterns-microos-defaults patterns-microos-hardware patterns-microos-ima_evm patterns-microos-onlyDVD patterns-microos-selinux patterns-microos-sssd_ldap libpwquality-tools pam-manpages pam-devel coreutils-doc MicroOS-release-dvd
# patterns-base-bootloader patterns-microos-ra_verifier patterns-microos-alt_onlyDVD patterns-microos-base-microdnf

RUN mkdir -p /srv/docserv && rpm2docserv -config microos.yaml

FROM opensuse/nginx:latest
LABEL maintainer="Thorsten Kukuk <kukuk@thkukuk.de>"

# labelprefix=org.opensuse.microos-docserv
LABEL org.opencontainers.image.title="MicroOS Documentation Server"
LABEL org.opencontainers.image.description="Manual pages and documentation to browse with a web server."
PREFIXEDLABEL org.opencontainers.image.created="%BUILDTIME%"
PREFIXEDLABEL org.opencontainers.image.version="%PKG_VERSION%-%RELEASE%"
PREFIXEDLABEL org.opencontainers.image.vendor="openSUSE Project"
PREFIXEDLABEL org.openbuildservice.disturl="%DISTURL%"
PREFIXEDLABEL org.opensuse.reference="registry.opensuse.org/opensuse/microos-docserv:%PKG_VERSION%-%RELEASE%"


COPY --from=build-stage /srv/docserv /srv/docserv
COPY --from=build-stage /usr/share/docserv/nginx/nginx.conf /usr/local/nginx/etc/
COPY --from=build-stage /usr/share/docserv/nginx/*.sh /docker-entrypoint.d/
COPY --from=build-stage /usr/sbin/docserv-auxserver /usr/sbin/
COPY --from=build-stage /usr/bin/openssl /usr/bin/
COPY --from=build-stage /etc/ssl/openssl.cnf /etc/ssl/
