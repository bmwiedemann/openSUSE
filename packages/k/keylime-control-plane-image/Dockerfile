# SPDX-License-Identifier: Apache-2.0
#!BuildTag: opensuse/keylime-control-plane:%%KEYLIME_VERSION%%
#!BuildTag: opensuse/keylime-control-plane:%%KEYLIME_VERSION%%-%RELEASE%
#!BuildTag: opensuse/keylime-control-plane:latest
FROM opensuse/tumbleweed:latest

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.keylime-control-plane
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Keylime Registrar and Verifier Services Container Image"
LABEL org.opencontainers.image.description="Keylime registar and verifier services based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%KEYLIME_VERSION%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.authors="aplanas@suse.de"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/keylime-control-plane:%%KEYLIME_VERSION%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"

LABEL com.suse.release-stage="released"
# endlabelprefix

LABEL RUN="podman run --name keylime-control-plane-container --rm -p 8881:8881 -p 8890:8890 -p 8891:8891 -v keylime-control-plane-volume:/var/lib/keylime -dt IMAGE"
LABEL INSTALL="podman volume create keylime-control-plane-volume"
LABEL UNINSTALL="podman volume rm keylime-control-plane-volume"

# The tenant can be run with
# podman run \
#    --rm -v keylime-control-plane-volume:/var/lib/keylime IMAGE \
#    keylime_tenant -v 10.88.0.1 -r 10.88.0.1 --cert default -c CMD

RUN set -euo pipefail; \
    zypper -n in --no-recommends \
      keylime-registrar \
      keylime-verifier \
      keylime-tenant \
      python3-packaging \
      python3-pyasn1 \
      python3-pyasn1-modules \
      libefivar1 \
      iproute2; \
    zypper -n clean; \
    rm -rf /var/log/*

COPY keylime-control-plane-start.sh /
RUN set -euo pipefail; \
    chmod a+x /keylime-control-plane-start.sh

CMD ["/keylime-control-plane-start.sh"]
VOLUME ["/var/lib/keylime"]
EXPOSE 8881 8890 8891

HEALTHCHECK --start-period=5m --timeout=5s --interval=5s --retries=2 \
    CMD /usr/bin/ss -ltn | /usr/bin/grep -q 0.0.0.0:8890

STOPSIGNAL SIGQUIT
