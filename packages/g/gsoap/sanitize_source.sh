#!/bin/sh -ex
#
# Shrink the gsoap archive from 32 MB -> 17 MB and removes .exe/.dll files.
#
# Requires: fdupes, hardlink

if ! which fdupes >/dev/null; then
	echo "fdupes not installed.";
	exit 1;
fi;
if ! which hardlink >/dev/null; then
	echo "The \"hardlink\" utility (package: hardlink) is not installed.";
	exit 1;
fi;

version="2.8.124"
shortver="2.8" # agh...
if [ ! -e "gsoap_$version.zip" ]; then
	wget -c "https://downloads.sf.net/gsoap2/gsoap_$version.zip"
fi

rm -Rf "gsoap-$shortver" "gsoap-$version"
unzip -q "gsoap_$version.zip"

# Someone failed at sane version number tagging.
mv "gsoap-$shortver" "gsoap-$version"

# Remove executables, backups, cache files, non-Linux parts...
rm -Rf "gsoap-$version/gsoap/bin" \
	"gsoap-$version/samples/link++/xmas" \
	"gsoap-$version"/*.old \
	"gsoap-$version/autom4te.cache"
find "gsoap-$version" -type d -name "*.pbxindex" -exec rm -Rf "{}" "+"
rm -Rf "gsoap-$version/gsoap/ios_plugin"
find "gsoap-$version" -type f "(" \
	-iname "*.exe" -o -iname "*.dll" -o -name "*.o" -o \
	-name "*~" -o -name .DS_Store ")" -delete

# And while we are at it, the VS files won't be needed anyway
rm -Rf "gsoap-$version/gsoap/VisualStudio2005"

hardlink "gsoap-$version"
find "gsoap-$version" -print0 | sort -z | \
	tar --no-recur --null -T- --owner=root --group=root --use=xz \
	-cf "gsoap-$version.tar.xz"
