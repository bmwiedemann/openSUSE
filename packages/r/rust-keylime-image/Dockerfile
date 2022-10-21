# SPDX-License-Identifier: Apache-2.0
#!BuildTag: opensuse/rust-keylime:%%KEYLIME_VERSION%%
#!BuildTag: opensuse/rust-keylime:%%KEYLIME_VERSION%%-%RELEASE%
#!BuildTag: opensuse/rust-keylime:latest
FROM opensuse/tumbleweed:latest

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.rust-keylime
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Keylime Rust Agent Service Container Image"
LABEL org.opencontainers.image.description="Keylime Rust agent service based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%KEYLIME_VERSION%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.authors="aplanas@suse.de"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/rust-keylime:%%KEYLIME_VERSION%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"

LABEL com.suse.release-stage="released"
# endlabelprefix

LABEL RUN="podman run --name rust-keylime-container --rm --device /dev/tpm0 --device /dev/tpmrm0 -v rust-keylime-volume:/var/lib/keylime -v rust-keylime-volume:/etc/keylime --tmpfs /var/lib/keylime/secure:rw,size=1m,mode=0700 -dt IMAGE"
LABEL INSTALL="podman volume create rust-keylime-volume"
LABEL CONFIGURE="podman run --rm -v rust-keylime-volume:/var/lib/keylime -v rust-keylime-volume:/etc/keylime IMAGE /rust-keylime-configure.sh"
LABEL UNINSTALL="podman volume rm rust-keylime-volume"

RUN set -euo pipefail; \
    zypper -n in --no-recommends \
      rust-keylime \
      iproute2; \
    zypper -n clean; \
    rm -rf /var/log/*

COPY rust-keylime-configure.sh /
RUN set -euo pipefail; \
    chmod a+x rust-keylime-configure.sh

ENV UUID="<UUID>" REMOTE_IP="<REMOTE_IP>" RUST_LOG="keylime_agent=info"

CMD ["/usr/bin/keylime_agent"]
VOLUME ["/var/lib/keylime"]
EXPOSE 9002

HEALTHCHECK --start-period=5m --timeout=5s --interval=5s --retries=2 \
    CMD /usr/bin/ss -ltn | /usr/bin/grep -q 0.0.0.0:9002

STOPSIGNAL SIGQUIT
