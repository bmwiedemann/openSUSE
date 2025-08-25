#!/bin/bash

# This script does the post install tasks specific for mingw32-*
# packages.
target="mingw32"
host="i686-w64-mingw32"

# If using normal root, avoid changing anything.
if [ -z "$RPM_BUILD_ROOT" -o "$RPM_BUILD_ROOT" = "/" ]; then
	exit 0
fi

[ -z "$OBJDUMP" ] && OBJDUMP="$host-objdump"
[ -z "$STRIP" ] && STRIP="$host-strip"

for i in $OBJDUMP $STRIP; do
	if ! [ -x "$(command -v $i)" ]; then
		echo "Error: $i is not installed." >&2
		exit 1
	fi
done

LC_ALL=
LANG=
LC_TIME=POSIX

cd "$RPM_BUILD_ROOT"

for f in `find . -type f -name "*.exe" -or -name "*.dll"`; do
	case $("$OBJDUMP" -h "$f" 2>/dev/null | grep -E -o '(debug[\.a-z_]*|gnu.version)') in
	    *debuglink*) continue ;;
	    *debug*) ;;
	    *gnu.version*)
		echo "WARNING: "`echo "$f" | sed -e "s,^$RPM_BUILD_ROOT/*,/,"`" is already stripped!"
		continue
		;;
	    *) continue ;;
	esac

	"$STRIP" --strip-unneeded "$f"
done
find . -type f -name "*.a" -exec chmod -x "{}" "+"
find . -type f -name "*.la" -delete

if [ -d "$RPM_BUILD_ROOT/usr/$host/sys-root/mingw/share/man" ]; then
    pushd "$RPM_BUILD_ROOT/usr/$host/sys-root/mingw/share/man"
    for f in `find -type f`; do
	    case "$f" in
	        *.Z) gunzip "$f"; b=`echo "$f" | sed -e 's/\.Z$//'`;;
	        *.gz) gunzip "$f"; b=`echo "$f" | sed -e 's/\.gz$//'`;;
	        *.bz2) bunzip2 "$f"; b=`echo "$f" | sed -e 's/\.bz2$//'`;;
	        *) b="$f";;
	    esac
        gzip -9 -n "$b"
    done
	popd
fi
    

if [ -d "$RPM_BUILD_ROOT/usr/$host/sys-root/mingw/share/info" ]; then
    pushd "$RPM_BUILD_ROOT/usr/$host/sys-root/mingw/share/info"
    for f in `find -type f`; do
	    case "$f" in
	        *.Z) gunzip "$f"; b=`echo "$f" | sed -e 's/\.Z$//'`;;
	        *.gz) gunzip "$f"; b=`echo "$f" | sed -e 's/\.gz$//'`;;
	        *.bz2) bunzip2 "$f"; b=`echo "$f" | sed -e 's/\.bz2$//'`;;
	        *) b="$f";;
	    esac
        gzip -9 -n "$b"
    done
	popd
fi
    
if [ -d "$RPM_BUILD_ROOT/usr/$host/sys-root/mingw/lib/pkgconfig" ]; then
    pushd "$RPM_BUILD_ROOT/usr/$host/sys-root/mingw/lib/pkgconfig"
    for f in `find . -type f -name "*.pc"`; do
        mv "$f" "$f~"
        sed \
         -e 's#L/usr/'"$host"'/sys-root/mingw/lib#L\${libdir}#g' \
         -e 's#I/usr/'"$host"'/sys-root/mingw/include#I\${includedir}#g' \
         -e '/original_prefix/!s#/usr/'"$host"'/sys-root/mingw#\${prefix}#g' \
         -e 's#^prefix=\${prefix}#prefix=/usr/'"$host"'/sys-root/mingw#g' \
         <"$f~" >"$f"
        rm -f "$f~"
    done
    popd
fi
    
if [ -d "$RPM_BUILD_ROOT/usr/$host/sys-root/mingw/share/pkgconfig" ]; then
    pushd "$RPM_BUILD_ROOT/usr/$host/sys-root/mingw/share/pkgconfig"
    for f in `find . -type f -name "*.pc"`; do
        mv "$f" "$f~"
        sed \
         -e 's#L/usr/'"$host"'/sys-root/mingw/lib#L\${libdir}#g' \
         -e 's#I/usr/'"$host"'/sys-root/mingw/include#I\${includedir}#g' \
         -e '/original_prefix/!s#/usr/'"$host"'/sys-root/mingw#\${prefix}#g' \
         -e 's#^prefix=\${prefix}#prefix=/usr/'"$host"'/sys-root/mingw#g' \
         <"$f~" >"$f"
        rm -f "$f~"
    done
    popd
fi
