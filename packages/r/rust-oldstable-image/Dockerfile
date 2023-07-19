# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/bci/rust:oldstable
#!BuildTag: opensuse/bci/rust:oldstable-2.%RELEASE%
#!BuildTag: opensuse/bci/rust:1.69
#!BuildTag: opensuse/bci/rust:1.69-2.%RELEASE%

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.rust
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI Rust 1.69"
LABEL org.opencontainers.image.description="Rust 1.69 container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="1.69"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/bci/rust:1.69-2.%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends rust1.69 cargo1.69; zypper -n clean; rm -rf /var/log/*
ENV RUST_VERSION="%%RUST_VERSION%%"
ENV CARGO_VERSION="%%CARGO_VERSION%%"
ENV CC="/usr/local/bin/gcc"

# workaround for gcc only existing as /usr/bin/gcc-N
RUN ln -sf $(ls /usr/bin/gcc-*|grep -P ".*gcc-[[:digit:]]+") /usr/local/bin/gcc
# smoke test that gcc works
RUN gcc --version
RUN ${CC} --version
