#!/bin/bash
# mingw64-find-debuginfo.sh - automatically generate debug info, sources and file list
# for inclusion in an rpm spec file for mingw64-* packages.
#
# syntax: mingw64--find-debuginfo.sh [<options>] [<BUILDDIR>]
# options:
#    --merge-debug-source-package  merge debug source package into debug info package
#    --no-debug-source-package     do not create debug source package
#    --src-root-dir                root dir for installing debug source files (src/debug is appended)
# BUILDDIR                         build directory (often $HOME/rpmbuild/BUILD)
# 
# $PWD package dir below $BUILDDIR

target="mingw64"
host="x86_64-w64-mingw32"

# extract debug info for a single file as child process
if [[ -v RUN_SINGLE ]]; then
	f=$1
	case $("$host-objdump" -h "$f" 2>/dev/null | egrep -o '(debug[\.a-z_]*|gnu.version)') in
		*debuglink*) exit 0;;
		*debug*) ;;
		*gnu.version*)
			echo "WARNING: "`echo $f | sed -e "s,^$RPM_BUILD_ROOT/*,/,"`" is already stripped!"
			exit 0
		;;
		*) exit 0 ;;
	esac
	echo extracting debug info from $f
	# grep all listed source files belonging to this package into temporary source file list.
	"$host-objdump" -Wi "$f" | "$host-objdump-srcfiles" | grep $srcdir >>"$SOURCEFILE.tmp"
	"$host-objcopy" --only-keep-debug "$f" "$f.debug" || :
	pushd `dirname $f`
	"$host-objcopy" --add-gnu-debuglink=`basename "$f.debug"` --strip-unneeded `basename "$f"` || :
	popd
	exit 0
fi

# speed up running objdump, see bug https://bugzilla.opensuse.org/show_bug.cgi?id=1202431
export MALLOC_CHECK_=0
export MALLOC_PERTURB_=0

BUILDDIR=.
MERGE_SOURCE_PACKAGE=0
SOURCE_PACKAGE=1

while [ $# -gt 0 ]; do
  case "$1" in
  --merge-debug-source-package)
    MERGE_SOURCE_PACKAGE=1
    ;;
  --no-debug-source-package)
    SOURCE_PACKAGE=0
    ;;
  --src-root-dir)
    ROOT_DIR=$2
    shift
    ;;
  *)
    BUILDDIR=$1
    shift
    break
    ;;
  esac
  shift
done

SOURCEFILE="$BUILDDIR/$target-debugsources.list"
> "$SOURCEFILE"
> $SOURCEFILE.tmp

srcdir=`realpath $PWD`

if [ ! -e "$BUILDDIR" ]; then
	mkdir -p "$BUILDDIR"
fi

# extract debug info
find $RPM_BUILD_ROOT -type f -name "*.exe" -or -name "*.dll" | sort | \
	srcdir=$srcdir SOURCEFILE=$SOURCEFILE BUILDDIR=$BUILDDIR RPM_BUILD_ROOT=$RPM_BUILD_ROOT RUN_SINGLE=1 xargs --max-args=1 --max-procs=0 bash -x $0

# generate debug info file list
find $RPM_BUILD_ROOT -type f \
		-name "*.exe.debug" \
	-or -name "*.dll.debug" \
	-or -name "*.exe.mdb" \
	-or -name "*.dll.mdb" \
| sort \
| sed -n -e "s#^$RPM_BUILD_ROOT##p" > $BUILDDIR/$target-debugfiles.list

if [ "$SOURCE_PACKAGE" -eq 0 ]; then
    echo creating debugsource file structure skipped
    exit 0
else
    echo creating debugsource file structure
fi

# create debug sources
ROOT_DIR="${ROOT_DIR:-/usr/$host/sys-root/mingw}"
SOURCE_DIR="${ROOT_DIR}/src"
DEBUGSOURCE_DIR="${SOURCE_DIR}/debug"

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

if [ "$MERGE_SOURCE_PACKAGE" -eq 1 ]; then
	cat $SOURCEFILE >> $BUILDDIR/$target-debugfiles.list
	rm $SOURCEFILE*
fi
