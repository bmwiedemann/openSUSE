# SPDX-License-Identifier: MIT

#     Copyright (c) 2025 SUSE LLC

# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon.

# The content of THIS FILE IS AUTOGENERATED and should not be manually modified.
# It is maintained by the BCI team and generated by
# https://github.com/SUSE/BCI-dockerfile-generator

# Please submit bugfixes or comments via https://bugs.opensuse.org/
# You can contact the BCI team via https://github.com/SUSE/bci/discussions

#!UseOBSRepositories

#!BuildTag: opensuse/stunnel:%%stunnel_re%%-%RELEASE%
#!BuildTag: opensuse/stunnel:%%stunnel_re%%
#!BuildTag: opensuse/stunnel:5
#!BuildTag: opensuse/stunnel:latest

FROM opensuse/bci/bci-micro:latest AS target
FROM opensuse/tumbleweed:latest AS builder
COPY --from=target / /target

RUN set -euo pipefail; \
    zypper -n --installroot /target --gpg-auto-import-keys install --no-recommends stunnel
# sanity check that the version from the tag is equal to the version of stunnel that we expect
RUN set -euo pipefail; \
    [ "$(rpm --root /target -q --qf '%{version}' stunnel | \
    cut -d '.' -f -1)" = "5" ]
RUN set -euo pipefail; zypper -n --installroot /target clean -a; \
    rm -rf {/target,}/var/log/{alternatives.log,lastlog,tallylog,zypper.log,zypp/history,YaST2}
FROM opensuse/bci/bci-micro:latest
COPY --from=builder /target /
# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.stunnel
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Stunnel"
LABEL org.opencontainers.image.description="Stunnel container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%stunnel_re%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opencontainers.image.ref.name="%%stunnel_re%%-%RELEASE%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/stunnel:%%stunnel_re%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime#openSUSE_BCI"
LABEL org.opensuse.release-stage="released"
# endlabelprefix
LABEL io.artifacthub.package.readme-url="%SOURCEURL_WITH(README.md)%"
COPY entrypoint.sh /usr/local/bin/
COPY stunnel.conf /etc/stunnel/stunnel.conf
RUN set -euo pipefail; chmod 0755 /usr/local/bin/entrypoint.sh;     chown --recursive stunnel /etc/stunnel
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/usr/sbin/stunnel"]
USER stunnel
