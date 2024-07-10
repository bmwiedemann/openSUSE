#!/bin/sh
#
# repackage kbd source tar ball, 
# to remove fonts that forbid commercial distribution.
#
# 2005-07-11, jw@suse.de

tmpdir=`mktemp -d`
in="$1"
if [ -z $in ]; then
  echo "usage: $0 <tarball>"
  exit 1
fi
name="${in%.tar.*}"

# recent gnu tar can autodetect gzip / bzip2
if ! tar xf "$in" -C $tmpdir; then
	rm -rf $tmpdir
	exit 1
fi
 
echo removing files...
find $tmpdir -iname \*agafari\* | tee /dev/tty | xargs rm
tar Jcf $name-repack.tar.xz -C $tmpdir $name

rm -rf $tmpdir
