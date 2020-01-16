#!/bin/bash
# Script to be run after updating the spec file from a newer release

# Enable pyverbs by default
sed -i -e 's/^%define with_pyverbs .*$/%if 0%{?sle_version} > 120400\n%define with_pyverbs 1\n%else\n%define with_pyverbs 0\n%endif/' rdma-core.spec
# Disable static
sed -i -e 's/^%define with_static .*$/%define with_static 0/' rdma-core.spec

# Fixup pandoc
# To remove a build dependency to pandoc in the core rings, prebuild the pandoc
# tarball and patch the spec file
bash gen-pandoc.sh || exit 1

EXTRA_SOURCES="Source2:        post_download.sh\nSource3:        prebuilt-pandoc.tgz\nSource4:        rdma-core-rpmlintrc\nSource5:        gen-pandoc.sh\nSource6:        get_build.py"
PANDOC_SETUP="#Extract prebuilt pandoc file in the buildlib directory\n(cd buildlib && tar xf %{S:3})"
sed -i -e '/Source1:/a '"$EXTRA_SOURCES" rdma-core.spec
sed -i -e '/^BuildRequires:  pandoc/d' rdma-core.spec
sed -i -e '/^BuildRequires:  python3-docutils/d' rdma-core.spec
sed -i -e '/^%setup /a '"$PANDOC_SETUP" rdma-core.spec
