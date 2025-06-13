#!/bin/bash -x

# Both pandoc-cli and python3-docutils are required to generate prebuilt docs
# docutils is insidious as it won't complain but final build will
# fail with missing prehashed doc
which pandoc || exit 1
which rst2man || exit 1

TARBALL=$(rpmspec --parse rdma-core.spec | grep Source: |  awk '{ print $NF}')
OUTDIR=$(tar tf $TARBALL | head -n 1)
PATCHES=$(rpmspec --parse rdma-core.spec | grep -E '^Patch[0-9]+:' | awk '{ print $NF}')
BUILD_CMDS=$(python3 -c "
import rpm

spec = rpm.spec(\"rdma-core.spec\")
print('%s' % (getattr(spec, \"build\"),))
")

CMAKE_CMD=$(echo "$BUILD_CMDS" |  sed -e :a -e '/\\$/N; s/\\\n//; ta' | grep /bin/cmake | sed -e 's/-GNinja//' -e 's/$OLDPWD\/./../')

TMPDIR=$(mktemp -d)
CURDIR=$(pwd)

cd $TMPDIR
rm -Rf $OUTDIR
tar xf $CURDIR/$TARBALL
cd $OUTDIR
for patch in $PATCHES; do
	patch -p0 < $CURDIR/$patch || exit 1
done
mkdir build
cd build
eval $CMAKE_CMD || exit 1
make docs -j4 || exit 1
tar czf $CURDIR/prebuilt-pandoc.tgz pandoc-prebuilt
cd $CURDIR/
rm -Rf $TMPDIR
