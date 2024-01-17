#!ExclusiveArch: do_not_build
FROM registry.opensuse.org/opensuse/tumbleweed-dnf as builder

WORKDIR /rpm/

COPY create-filelists.sh .

RUN ./create-filelists.sh
