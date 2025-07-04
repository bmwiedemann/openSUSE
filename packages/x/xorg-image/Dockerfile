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
#!ExclusiveArch: x86_64 aarch64
#!BuildTag: opensuse/xorg:%%xorg_server_ver%%-%RELEASE%
#!BuildTag: opensuse/xorg:%%xorg_server_ver%%
#!BuildTag: opensuse/xorg:21
#!BuildTag: opensuse/xorg:notaskbar
#!BuildTag: opensuse/xorg:latest

FROM opensuse/bci/bci-micro:latest AS target
FROM opensuse/tumbleweed:latest AS builder
COPY --from=target / /target

RUN set -euo pipefail; \
    zypper -n --installroot /target --gpg-auto-import-keys install --no-recommends hostname icewm-lite procps sysvinit-tools which xdm xf86-input-evdev xf86-input-libinput xhost xinit xinput xkeyboard-config xorg-x11 xorg-x11-essentials xorg-x11-server xrandr xsession
# sanity check that the version from the tag is equal to the version of xorg-x11-server that we expect
RUN set -euo pipefail; \
    [ "$(rpm --root /target -q --qf '%{version}' xorg-x11-server | \
    cut -d '.' -f -1)" = "21" ]
RUN useradd -m user -u 1000
RUN set -euo pipefail; zypper -n --installroot /target clean -a; \
    rm -rf {/target,}/var/log/{alternatives.log,lastlog,tallylog,zypper.log,zypp/history,YaST2}
FROM opensuse/bci/bci-micro:latest
COPY --from=builder /target /
# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.application.xorg
LABEL org.opencontainers.image.title="openSUSE Tumbleweed Xorg Server"
LABEL org.opencontainers.image.description="Xorg Server container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%xorg_server_ver%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opencontainers.image.ref.name="%%xorg_server_ver%%-%RELEASE%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/xorg:%%xorg_server_ver%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime#openSUSE_BCI"
LABEL org.opensuse.release-stage="released"
# endlabelprefix
LABEL io.artifacthub.package.readme-url="%SOURCEURL_WITH(README.md)%"
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /home/user /home/user
COPY preferences /etc/icewm/preferences
COPY xinitrc /etc/X11/xinit/xinitrc
COPY xorg.conf /etc/X11/xorg.conf.d/xorg.conf

ENV XDG_SESSION_TYPE=x11

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN set -euo pipefail; chmod +x /usr/local/bin/entrypoint.sh
