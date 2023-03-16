#!/bin/sh
#mingw64-find-debuginfo.sh - automagically generate debug info and file list
#for inclusion in an rpm spec file for mingw64-* packages.
#
# $PWD package dir below $BUILDDIR

target="mingw64"
host="x86_64-w64-mingw32"

# speed up running objdump, see bug https://bugzilla.opensuse.org/show_bug.cgi?id=1202431
export MALLOC_CHECK_=0
export MALLOC_PERTURB_=0

BUILDDIR=.
if [ -n "$1" ]; then
	BUILDDIR="$1"
fi

# generate separate debuginfo and debugsource or single debug package combining both
if [ -n "$2" ]; then
	SINGLE_DEBUG_PACKAGE=1
else
	SINGLE_DEBUG_PACKAGE=0
fi

SOURCEFILE="$BUILDDIR/$target-debugsources.list"
> "$SOURCEFILE"
> $SOURCEFILE.tmp

srcdir=`realpath $PWD`

ROOT_DIR="/usr/$host/sys-root/mingw"
SOURCE_DIR="${ROOT_DIR}/src"
DEBUGSOURCE_DIR="${SOURCE_DIR}/debug"

for f in `find $RPM_BUILD_ROOT -type f -name "*.exe" -or -name "*.dll" | sort`
do
	case $("$host-objdump" -h "$f" 2>/dev/null | egrep -o '(debug[\.a-z_]*|gnu.version)') in
	    *debuglink*) continue ;;
	    *debug*) ;;
	    *gnu.version*)
		echo "WARNING: "`echo $f | sed -e "s,^$RPM_BUILD_ROOT/*,/,"`" is already stripped!"
		continue
		;;
	    *) continue ;;
	esac

	echo extracting debug info from $f

	# grep all listed source files belonging to this package into temporary source file list.
	"$host-objdump" -Wi "$f" | "$host-objdump-srcfiles" | grep $srcdir >>"$SOURCEFILE.tmp"

	"$host-objcopy" --only-keep-debug "$f" "$f.debug" || :
	pushd `dirname $f`
	"$host-objcopy" --add-gnu-debuglink=`basename "$f.debug"` --strip-unneeded `basename "$f"` || :
	popd
done

if [ ! -e "$BUILDDIR" ]; then
	mkdir -p "$BUILDDIR"
fi
find $RPM_BUILD_ROOT -type f \
		-name "*.exe.debug" \
	-or -name "*.dll.debug" \
	-or -name "*.exe.mdb" \
	-or -name "*.dll.mdb" \
| sort \
| sed -n -e "s#^$RPM_BUILD_ROOT##p" > $BUILDDIR/$target-debugfiles.list

echo creating debugsource file structure

destdir=${RPM_BUILD_ROOT}${DEBUGSOURCE_DIR}
if [ ! -e "$destdir" ]; then
	install -d "$destdir"
fi

for f in `cat $SOURCEFILE.tmp | sort | uniq`
do
	if ! test -f "$f"; then
		echo "excluded not present file '$f"
		continue
	fi
	o=`echo $f | sed "s,$BUILDDIR,$destdir,g"`
	p=`dirname $o`
	if [ ! -e "$p" ]; then
		install -d "$p"
	fi
	echo copying $f to $o
	install -m 644 $f $o
done
rm $SOURCEFILE.tmp

# add package source directory to list of files
if [ -e "$RPM_BUILD_ROOT/$DEBUGSOURCE_DIR" ]; then
	echo "%dir $SOURCE_DIR" >> $SOURCEFILE
	echo "$DEBUGSOURCE_DIR" >> $SOURCEFILE
fi

if test "$SINGLE_DEBUG_PACKAGE" -eq 1; then
	cat $SOURCEFILE >> $BUILDDIR/$target-debugfiles.list
	rm $SOURCEFILE*
fi
