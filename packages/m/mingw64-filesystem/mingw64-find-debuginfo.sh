#!/bin/sh
#mingw64-find-debuginfo.sh - automagically generate debug info and file list
#for inclusion in an rpm spec file for mingw64-* packages.
target="mingw64"
host="x86_64-w64-mingw32"

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
SYMBOL_DIR="${ROOT_DIR}/symbols"
SOURCE_DIR="${ROOT_DIR}/src"
DEBUGSOURCE_DIR="${SOURCE_DIR}/debug"

for f in `find $RPM_BUILD_ROOT -type f -name "*.exe" -or -name "*.dll"`
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

	# breakpad symbols
	symfile=`"$host-gen_sym_files" "$f" "$RPM_BUILD_ROOT$SYMBOL_DIR"`
	echo $symfile
	# grep all listed source files belonging to this package into temporary source file list
	cat $symfile | grep "FILE" | cut -d' ' -f3 | grep $srcdir >> $SOURCEFILE.tmp
	# remap file path in symbol file to src debug location
	# we remap all files to make finding src files from other packages possible
	sed -i "s,$BUILDDIR,$DEBUGSOURCE_DIR,g" $symfile

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
| sed -n -e "s#^$RPM_BUILD_ROOT##p" >"$BUILDDIR/$target-debugfiles.list"

if [ -e "$RPM_BUILD_ROOT/$SYMBOL_DIR" ]; then
	echo "$SYMBOL_DIR" >>"$BUILDDIR/$target-debugfiles.list"
fi

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
	# create debugsource.list
	# we do not add each single file, see below
	# echo $o | sed "s,${RPM_BUILD_ROOT},,g" >> $SOURCEFILE
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
