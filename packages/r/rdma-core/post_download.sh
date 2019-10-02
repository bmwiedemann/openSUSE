#!/bin/bash
# Script to be run after updating the spec file from a newer release

# Enable pyverbs by default
sed -i -e 's/^%define with_pyverbs .*$/%define with_pyverbs 1/' rdma-core.spec
# Disable static
sed -i -e 's/^%define with_static .*$/%define with_static 0/' rdma-core.spec

# Fixup pandoc
# To remove a build dependency to pandoc in the core rings, prebuild the pandoc
# tarball and patch the spec file
TARBALL=$(rpmspec --parse rdma-core.spec | grep Source: |  awk '{ print $NF}')
OUTDIR=$(tar tf $TARBALL | head -n 1)

rm -Rf $OUTDIR
tar xf $TARBALL
cd $OUTDIR
mkdir build
cd build
cmake ..
make docs
tar czf ../../prebuilt-pandoc.tgz pandoc-prebuilt
cd ../..

EXTRA_SOURCES="Source2:        post_download.sh\nSource3:        prebuilt-pandoc.tgz\nSource4:        rdma-core-rpmlintrc"
PANDOC_SETUP="#Extract prebuilt pandoc file in the buildlib directory\n(cd buildlib && tar xf %{S:3})"
sed -i -e '/Source1:/a '"$EXTRA_SOURCES" rdma-core.spec
sed -i -e '/^BuildRequires:  pandoc/d' rdma-core.spec
sed -i -e '/^BuildRequires:  python3-docutils/d' rdma-core.spec
sed -i -e '/^%setup /a '"$PANDOC_SETUP" rdma-core.spec
