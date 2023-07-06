# SPDX-License-Identifier: MIT
#!BuildTag: opensuse/bci/ruby:3.2
#!BuildTag: opensuse/bci/ruby:3.2-%RELEASE%
#!BuildTag: opensuse/bci/ruby:3
#!BuildTag: opensuse/bci/ruby:3-%RELEASE%
#!BuildTag: opensuse/bci/ruby:latest

FROM opensuse/tumbleweed:latest

MAINTAINER openSUSE (https://www.opensuse.org/)

# Define labels according to https://en.opensuse.org/Building_derived_containers
# labelprefix=org.opensuse.bci.ruby
LABEL org.opencontainers.image.title="openSUSE Tumbleweed BCI Ruby 3.2"
LABEL org.opencontainers.image.description="Ruby 3.2 container based on the openSUSE Tumbleweed Base Container Image."
LABEL org.opencontainers.image.version="3.2"
LABEL org.opencontainers.image.url="https://www.opensuse.org"
LABEL org.opencontainers.image.created="%BUILDTIME%"
LABEL org.opencontainers.image.vendor="openSUSE Project"
LABEL org.opencontainers.image.source="%SOURCEURL%"
LABEL org.opensuse.reference="registry.opensuse.org/opensuse/bci/ruby:3.2-%RELEASE%"
LABEL org.openbuildservice.disturl="%DISTURL%"
LABEL org.opensuse.lifecycle-url="https://en.opensuse.org/Lifetime"
LABEL org.opensuse.release-stage="released"

# endlabelprefix

RUN set -euo pipefail; zypper -n in --no-recommends ruby3.2 ruby3.2-rubygem-bundler ruby3.2-devel util-linux curl git-core distribution-release gcc-c++ sqlite3-devel make awk timezone; zypper -n clean; rm -rf /var/log/*
ENV LANG="C.UTF-8"
ENV RUBY_VERSION="%%rb_ver%%"
ENV RUBY_MAJOR="%%rb_maj%%"

RUN set -euo pipefail; sed -i 's/--format-executable/--no-format-executable/' /etc/gemrc
