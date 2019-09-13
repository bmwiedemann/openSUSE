# removes stuff under old Unicode license
# $1 is directory with tarballs
set -o errexit
VERSION=2.2.5
if test -f "$1/figlet-$VERSION.tar.gz" ; then
	TMPDIR=`mktemp -d`
	if test -d $TMPDIR ; then
		trap "rm -rf \"$TMPDIR\" \"$1/figlet-$VERSION-patched.tar.bz2\"" ERR
		cd $TMPDIR
		gzip -cd "$1/figlet-$VERSION.tar.gz" > "$1/figlet-$VERSION-patched.tar"
		tar --delete -f "$1/figlet-$VERSION-patched.tar" figlet-$VERSION/fonts/jis0201.flc
		bzip2 -f "$1/figlet-$VERSION-patched.tar"
		cd - 1>/dev/null
		rm -Rf $TMPDIR
	else
		echo "creating tmp dir failed"
		exit 102
	fi
else
	echo "file: $1/figlet-$VERSION.tar.gz doesn't exist"
fi
