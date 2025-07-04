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
#!ExclusiveArch: aarch64 x86_64
#!BuildTag: opensuse/bci/spack:%%spack_version%%-%RELEASE%
#!BuildTag: opensuse/bci/spack:%%spack_version%%
#!BuildTag: opensuse/bci/spack:0.23
#!BuildTag: opensuse/bci/spack:latest

FROM opensuse/tumbleweed:latest

RUN set -euo pipefail; \
    zypper -n install spack bison cmake-full flex libtool makeinfo patchelf lsb-release zstd libzip-devel libcurl-devel libopenssl-devel ncurses-devel tack xz-devel
RUN set -euo pipefail; zypper -n clean -a; \
    rm -rf {/target,}/var/log/{alternatives.log,lastlog,tallylog,zypper.log,zypp/history,YaST2}

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.spack
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI Spack development"
LABEL org.opencontainers.image.description="Spack development container for building containerized HPC solution stacks, based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="%%spack_version%%"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opencontainers.image.ref.name="%%spack_version%%-%RELEASE%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/bci/spack:%%spack_version%%-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime#openSUSE_BCI"
LABEL org.opensuse.release-stage="released"
# endlabelprefix
LABEL io.artifacthub.package.readme-url="%SOURCEURL_WITH(README.md)%"
LABEL io.artifacthub.package.logo-url="https://spack.io/assets/images/spack-logo-white.svg"
LABEL usage="This container is enabled and supported only on a SLE15+ host."
ENV SPACK_ROOT="/usr"
ENV CURRENTLY_BUILDING_DOCKER_IMAGE="1"
ENV container="docker"
ENTRYPOINT ["/bin/bash", "/usr/share/spack/docker/entrypoint.bash"]
CMD ["interactive-shell"]

RUN set -euo pipefail; ln -s $SPACK_ROOT/share/spack/docker/entrypoint.bash \
       /usr/local/bin/docker-shell \
    && ln -s $SPACK_ROOT/share/spack/docker/entrypoint.bash \
       /usr/local/bin/interactive-shell \
    && ln -s $SPACK_ROOT/share/spack/docker/entrypoint.bash \
       /usr/local/bin/spack-env \
    && echo 'source $SPACK_ROOT/share/spack/spack-completion.bash' > /root/.bashrc
RUN set -euo pipefail; mkdir -p /root/.spack \
    && cp $SPACK_ROOT/share/spack/docker/modules.yaml \
       /root/.spack/modules.yaml \
    && rm -rf /root/*.* /run/nologin

# sanity check that the version from the tag is equal to the version of spack that we expect
RUN set -euo pipefail; \
    [ "$(rpm -q --qf '%{version}' spack | \
    cut -d '.' -f -2)" = "0.23" ]

WORKDIR /root
SHELL ["docker-shell"]
