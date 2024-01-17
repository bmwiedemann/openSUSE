#!/bin/sh
set -eu
tmpdir=$(mktemp -d)
trap 'rm -rf ${tmpdir}' EXIT

script="$(realpath "$(dirname $0)")/docker_label_helper"

cd $tmpdir

# Test old syntax
cat >Dockerfile <<EOF
# labelprefix=org.opensuse.nano
PREFIXEDLABEL org.opencontainers.image.title="Example container."
PREFIXEDLABEL org.opencontainers.image.description="This contains nano"
PREFIXEDLABEL org.opencontainers.image.source="https://build.opensuse.org/package/show/openSUSE:Factory/opensuse-tumbleweed-image?rev=1afbea7e9b8ecf976071564312c2db66"
PREFIXEDLABEL	test.whitespace="Two  spaces. One	tab."
EOF

export BUILD_DIST=
sh "${script}"

diff -u Dockerfile - <<EOF
LABEL org.opensuse.nano.title="Example container."
LABEL org.opencontainers.image.title="Example container."
LABEL org.opensuse.nano.description="This contains nano"
LABEL org.opencontainers.image.description="This contains nano"
LABEL org.opensuse.nano.source="https://build.opensuse.org/package/show/openSUSE:Factory/opensuse-tumbleweed-image?rev=1afbea7e9b8ecf976071564312c2db66"
LABEL org.opencontainers.image.source="https://build.opensuse.org/package/show/openSUSE:Factory/opensuse-tumbleweed-image?rev=1afbea7e9b8ecf976071564312c2db66"
LABEL org.opensuse.nano.whitespace="Two  spaces. One	tab."
LABEL	test.whitespace="Two  spaces. One	tab."
EOF

rm -f Dockerfile

# Test new syntax
cat >Dockerfile <<EOF
# labelprefix=org.opensuse.nano
LABEL org.opencontainers.image.title="Example container."
LABEL org.opencontainers.image.description="This contains nano"
LABEL org.opencontainers.image.source="https://build.opensuse.org/package/show/openSUSE:Factory/opensuse-tumbleweed-image?rev=1afbea7e9b8ecf976071564312c2db66"
LABEL	test.whitespace="Two  spaces. One	tab."
# endlabelprefix
LABEL not.expanded.label="example"
EOF

export BUILD_DIST=
sh "${script}"

diff -u Dockerfile - <<EOF
LABEL org.opensuse.nano.title="Example container."
LABEL org.opencontainers.image.title="Example container."
LABEL org.opensuse.nano.description="This contains nano"
LABEL org.opencontainers.image.description="This contains nano"
LABEL org.opensuse.nano.source="https://build.opensuse.org/package/show/openSUSE:Factory/opensuse-tumbleweed-image?rev=1afbea7e9b8ecf976071564312c2db66"
LABEL org.opencontainers.image.source="https://build.opensuse.org/package/show/openSUSE:Factory/opensuse-tumbleweed-image?rev=1afbea7e9b8ecf976071564312c2db66"
LABEL org.opensuse.nano.whitespace="Two  spaces. One	tab."
LABEL	test.whitespace="Two  spaces. One	tab."
LABEL not.expanded.label="example"
EOF
