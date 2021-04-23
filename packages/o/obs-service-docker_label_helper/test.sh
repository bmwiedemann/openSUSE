#!/bin/sh
set -eu
tmpdir=$(mktemp -d)
trap 'rm -rf ${tmpdir}' EXIT

script="$(realpath "$(dirname $0)")/docker_label_helper"

cd $tmpdir

cat >Dockerfile <<EOF
# labelprefix=org.opensuse.nano
PREFIXEDLABEL org.opencontainers.image.title="Example container"
PREFIXEDLABEL org.opencontainers.image.description="This contains nano"
EOF

export BUILD_DIST=
sh "${script}"

diff -u Dockerfile - <<EOF
LABEL org.opensuse.nano.title="Example container"
LABEL org.opencontainers.image.title="Example container"
LABEL org.opensuse.nano.description="This contains nano"
LABEL org.opencontainers.image.description="This contains nano"
EOF
