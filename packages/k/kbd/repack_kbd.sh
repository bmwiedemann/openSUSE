#! /bin/sh
#
# repackage kbd source tar ball, 
# to remove fonts that forbid commercial distribution.
#
# 2005-07-11, jw@suse.de

tmpdir=`mktemp -d`

in=$1

case "$in" in
  *.tar.gz)
    tar zxf $in -C $tmpdir
    ;;
  *.tgz)
    tar zxf $in -C $tmpdir
    ;;
  *.tar.bz2)
    tar jxf $in -C $tmpdir
    ;;
  *.tar)
    tar xf $in -C $tmpdir
    ;;
  *)
    echo "hmm, '$in' is not a tar ball?"
    rmdir $tmpdir
    exit 1
esac
 
echo removing files...
find $tmpdir -iname \*agafari\* | tee /dev/tty | xargs rm
tar jcf $in-repack.tar.bz2 -C $tmpdir .

rm -rf $tmpdir
