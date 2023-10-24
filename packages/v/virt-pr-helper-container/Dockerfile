# SPDX-License-Identifier: Apache-2.0

# Define the tags for OBS and build script builds:
#!BuildTag: %%TAGPREFIX%%/pr-helper:%%PKG_VERSION%%
#!BuildTag: %%TAGPREFIX%%/pr-helper:%%PKG_VERSION%%.%RELEASE%
#!BuildTag: %%TAGPREFIX%%/pr-helper:%%PKG_VERSION%%-%%PKG_RELEASE%%

#!ExclusiveArch: x86_64 aarch64

# pr-helper container image
# KUBEVIRTFROM defined in prjconf, e.g.
#  BuildFlags: dockerarg:KUBEVIRTFROM=opensuse/tumbleweed
ARG KUBEVIRTFROM
FROM $KUBEVIRTFROM

# Mandatory labels for the build service:
#   https://en.opensuse.org/Building_derived_containers
# labelprefix=%%LABELPREFIX%%
LABEL org.opencontainers.image.title="kubevirt pr-helper container"
LABEL org.opencontainers.image.description="QEMU persistent reservation helper"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.version="%%PKG_VERSION%%.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.reference="%%REGISTRY%%/%%TAGPREFIX%%/pr-helper:%%PKG_VERSION%%.%RELEASE%"
# endlabelprefix

RUN zypper -n install \
        kubevirt-pr-helper-conf \
        qemu-pr-helper && \
    zypper clean -a

RUN cp -f /usr/share/kube-virt/pr-helper/multipath.conf /etc/

ENTRYPOINT [ "/usr/bin/qemu-pr-helper" ]
