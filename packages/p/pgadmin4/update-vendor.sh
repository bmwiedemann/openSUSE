#!/bin/bash
#
# This script updates the vendor source package.
# It should be run in the developer system in each pgadmin version update
#
# -- Antonio Larrosa <alarrosa@suse.com>
#

version=`grep ^Version: *.spec | sed -e "s/^Version: *//"`
if [ -d pgadmin4-$version ]; then
	echo "The directory pgadmin4-$version already exists. Please remove it in order to recreate it from scratch by running"
	echo "rm -Rf pgadmin4-$version"
	exit 1
fi

quilt setup pgadmin4.spec
pushd pgadmin4-$version
quilt push -a

# Build everything as documented by upstream
make install-node
## We can run make bundle in %build so let's keep the things we do outside obs at a minimum
#make bundle

# Remove binary files that are not needed and shouldn't be packaged in a noarch package
rm web/node_modules/ttf2woff2/build/Release/addon.node
rm web/node_modules/ttf2woff2/build/Release/obj.target/addon.node
rm web/node_modules/ttf2woff2/build/node_gyp_bins/python3
rm web/node_modules/mozjpeg/vendor/cjpeg
rm web/node_modules/optipng-bin/vendor/optipng

# Remove trash files
rm web/node_modules/console-control-strings/README.md~
rm web/node_modules/form-data/README.md.bak

# Remove development files
rm -Rf web/node_modules/ttf2woff2/build/Release/obj.target/addon/csrc
rm web/node_modules/nan/*.h
rm web/node_modules/ttf2woff2/csrc/*/*.h

# Fix files unnecessarily having the executable bit set
find web/node_modules -type f \( -iname *.md -o -iname LICEN[CS]E -o -iname *.html -o -iname *.json -o -iname *.css -o -iname *.ttf -o -iname *.png \) -exec chmod -x "{}" \;

tar cvfJ ../vendor.tar.xz web/node_modules web/pgadmin/misc/themes/pgadmin.themes.json web/pgadmin/static/js/generated/ web/yarn.lock
popd
