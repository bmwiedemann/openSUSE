#!/bin/bash

TMPDIR=$(mktemp -d /tmp/inst-source-utils-XXXXXX)
TOPDIR=$TMPDIR/inst-source-utils
SUSEDIR=/
BINDIR=${SUSEDIR}usr/bin
MODULEDIR=/usr/share/inst-source-utils
BUILD_ETC=${MODULEDIR}/etc

BINFILES="/work/cd/bin/tools/mk_listings /work/cd/bin/tools/create_directory.yast 
          /work/cd/bin/tools/create_md5sums /work/cd/bin/tools/create_package_descr 
          /work/cd/bin/tools/create_sha1sums /work/cd/lib/m_cd/gen-s390-cd-kernel.pl 
          /work/cd/bin/tools/create_sha1sum /work/cd/bin/tools/compress_susetags
          /work/cd/bin/tools/packages2eula.pl /work/cd/lib/mach_cd/mk_changelog
          /work/cd/bin/tools/create_repo_for_patch.sh /work/cd/bin/createpatch
          /work/cd/bin/tools/create_update_source.sh
          /work/cd/bin/tools/rezip_repo_rsyncable"

mkdir -p $TOPDIR$BINDIR
mkdir -p $TOPDIR$MODULEDIR/modules

#copy binaries
for i in $BINFILES ; do
  echo "Preparing: $(basename $i)"
  sed -e "s|/work/abuild/lib/abuild|$MODULEDIR|g"  \
      -e "s|/work/abuild|$SUSEDIR|g" \
      -e "s|/work/cd/bin/tools|$BINDIR|g" \
      -e "s|/work/cd|$SUSEDIR|g" \
      -e "s|/work/src/bin|$SUSEDIR|g" \
      -e "s|/work/built/info|$SUSEDIR/data|g" \
      -e "s|/mounts/you/ftp|/media/dvdrecorder|g" \
      $i > $TOPDIR$BINDIR/$(basename $i)
  chmod 755 $TOPDIR$BINDIR/$(basename $i)
done

# needed perl module
for i in /mounts/work/abuild/lib/abuild/modules/RPMQ.pm \
	/mounts/work/abuild/lib/abuild/modules/ABXML.pm \
	/mounts/work/abuild/lib/abuild/modules/ABStructured.pm ; do
  echo "Preparing: $(basename $i)"
  sed -e "s|/work/abuild|$BINDIR|g" $i > $TOPDIR$MODULEDIR/modules/`basename $i`
done
chmod 644 $TOPDIR$MODULEDIR/modules/*.pm

# extra sed for scripts using the perl modules
for i in create_package_descr ; do
  echo "Preparing: $(basename $i)"
  sed -e "s|$BINDIR/lib/abuild|$MODULEDIR|g" $TOPDIR$BINDIR/$i > $TOPDIR$BINDIR/$i.tmp
  mv $TOPDIR$BINDIR/$i.tmp $TOPDIR$BINDIR/$i
  chmod 755 $TOPDIR$BINDIR/$i
done

# don't package lines between <!--internal--> and <!--/internal-->
for i in $TOPDIR$BINDIR/*; do
	perl `dirname $0`/split.pl $i $i.new
	mv $i.new $i
	chmod 755 $i
done

pushd $TMPDIR >/dev/null
tar cjfp ../inst-source-utils.tar.bz2 inst-source-utils
popd >/dev/null
cp -v $TMPDIR/../inst-source-utils.tar.bz2 .
test "$TMPDIR" != "/" -a -d "$TMPDIR" &&  rm -rf $TMPDIR

LASTFILE=`find_newest_file *.tar.bz2`
VERSION=`get_date_version_string $LASTFILE`
sed -i -e "s@^Version:.*@Version:        $VERSION@" inst-source-utils.spec
