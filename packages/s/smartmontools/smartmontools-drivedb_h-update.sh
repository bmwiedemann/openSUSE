#!/bin/bash

# Packaged drivedb.h/smartmontools-drivedb.h update script.
# Usage: bash ./smartmontools-drivedb_h-update.sh
# Exit codes:
#	O: Changes performed. You should commit.
#	1: No changes performed.
#	2: Internal error.

set -o errexit

# get_db_version DRIVEDB > VERSION
get_db_version()
{
  local v
  v=`sed -n '/^[ {]*"VERSION: .*"/{
       s,^[ {]*"VERSION: \([1-9][./0-9]*\)[ "].*$,\1,p
       q
     }' "$1"` || return 1
  test -n "$v" || return 0
  test "${v%/*}" != "$v" || v="$v/?"
  echo "$v"
}

VERSION=`sed -n 's/^Version:[[:space:]]*//p' <smartmontools.spec`

WORKDIR="smartmontools-drivedb_h-update.tmp"

rm -rf "$WORKDIR"
mkdir "$WORKDIR"
cd "$WORKDIR"

tar --wildcards -zxf ../smartmontools-$VERSION.tar.gz "smartmontools-$VERSION/update-smart-drivedb.*" "smartmontools-$VERSION/configure*" smartmontools-$VERSION/drivedb.h
# There can be script update.
# TODO: This patch can be generated automatically.
if test -f ../smartmontools-update-smart-drivedb.patch ; then
	patch -p0 <../smartmontools-update-smart-drivedb.patch
fi

# Extract expression that derives DRIVEDB_BRANCH from the version string
# (from configure, to not include autoconf square brackets):
eval "$(sed -n -e '/^[^ ]*drivedb_version=/p; /^DRIVEDB_BRANCH=/,/^$/p' <smartmontools-$VERSION/configure)"
if test -z "$DRIVEDB_BRANCH"; then
	echo "Unable to derive DRIVEDB_BRANCH from VERSION=$VERSION."
	cd - >/dev/null
	rm -r "$WORKDIR"
	exit 2
fi
BRANCHNAME=$DRIVEDB_BRANCH

DEF_VERSION=$(get_db_version smartmontools-$VERSION/drivedb.h)
if test -f ../smartmontools-drivedb.h ; then
	PCK_VERSION=$(get_db_version ../smartmontools-drivedb.h)
	PCK_DRIVEDB=../smartmontools-drivedb.h
else
	PCK_VERSION=$DEF_VERSION
	PCK_DRIVEDB=smartmontools-$VERSION/drivedb.h
fi

echo "Updating drivedb.h for branch $DRIVEDB_BRANCH."

# Generate and call specially crafted update-smart-drivedb.
sed "
	/^PACKAGE=/i rm update-smart-drivedb-wd
	s:@PACKAGE@:smartmontools:g
	s:@VERSION@:$VERSION:g
	s:@DRIVEDB_BRANCH@:$DRIVEDB_BRANCH:g
	s:@ENABLE_SCRIPTPATH_TRUE@:#:g
	s:@ENABLE_SCRIPTPATH_FALSE@::g
	s:@gnupg@:/usr/bin/gpg:
	s:^DRIVEDB=.*$:DRIVEDB=smartmontools-drivedb.h:
	s:@drivedbdir@:.:g
	s:@os_dltools@:curl wget lynx:g
	" <smartmontools-$VERSION/update-smart-drivedb.in >update-smart-drivedb-wd
chmod +x update-smart-drivedb-wd
# Verification of the downloaded drivedb.h has to be done by the packaged smartctl.
# Skip it on the host system, and run it as part of %build stage.
./update-smart-drivedb-wd -u github -s -
if test -f drivedb.h ; then
	mv drivedb.h smartmontools-drivedb.h
fi
rm -f "$DEST.lastcheck"
rm -f "$DEST.old"

# Compare time (file in the drivedb branch can be older) and compare
# files without Id (files can be equal but committed in two commits).

UPD_VERSION=$(get_db_version smartmontools-drivedb.h)
sed '/"VERSION: /d' <smartmontools-$VERSION/drivedb.h >drivedb-noid.h
sed '/"VERSION: /d' <smartmontools-drivedb.h >smartmontools-drivedb-noid.h
if cmp -s drivedb-noid.h smartmontools-drivedb-noid.h ; then
	EQUAL=true
else
	EQUAL=false
fi

# Return to the OSC repository and perform needed changes.
cd - >/dev/null

DEF_VER=${DEF_VERSION#*/}
if test "$DEF_VER" = "?" ; then
	DEF_VER=0
fi
PCK_VER=${PCK_VERSION#*/}
if test "$PCK_VER" = "?" ; then
	PCK_VER=0
fi

UPD_VER=${UPD_VERSION#*/}
if test $EQUAL = true -o \( $UPD_VER -le $DEF_VER \) ; then
	echo "No drivedb.h update available."
	if test -f smartmontools-drivedb.h ; then
		osc rm --force smartmontools-drivedb.h
	fi
	sed 's/^Source[0-9]*:[ 	]*smartmontools-drivedb.h$/#&/;s/^cp -a .* drivedb\.h\.new$/#&/' <smartmontools.spec >"$WORKDIR/smartmontools.spec"
	if ! cmp -s smartmontools.spec "$WORKDIR/smartmontools.spec" ; then
		echo "Removing smartmontools-drivedb.h from spec file."
		osc vc -m "Remove smartmontools-drivedb.h. No update available in the
  upstream branch $BRANCHNAME."
		mv "$WORKDIR/smartmontools.spec" ./
	fi
else
	if test -f smartmontools-drivedb.h ; then
		if cmp -s "$WORKDIR/smartmontools-drivedb.h" smartmontools-drivedb.h ; then
			echo "smartmontools-drivedb.h is up to date. Nothing to be done."
			rm -r "$WORKDIR"
			exit 1
		else
			echo "smartmontools-drivedb.h updated."
			mv "$WORKDIR/smartmontools-drivedb.h" ./
			osc vc -m "Update smartmontools-drivedb.h to the latest version from the
  upstream branch $BRANCHNAME."
		fi
	else
		sed 's/^#\(Source[0-9]*:[ 	]*smartmontools-drivedb.h\)$/\1/;s/^#\(cp -a .* drivedb\.h\.new\)$/\1/' <smartmontools.spec >"$WORKDIR/smartmontools.spec"
		if ! cmp -s smartmontools.spec "$WORKDIR/smartmontools.spec" ; then
			echo "Adding smartmontools-drivedb.h to the spec file."
			osc vc -m "Add smartmontools-drivedb.h, the latest version from the upstream
  branch $BRANCHNAME."
			mv "$WORKDIR/smartmontools.spec" ./
			mv "$WORKDIR/smartmontools-drivedb.h" ./
			osc add smartmontools-drivedb.h
		fi
	fi
fi

echo "Consider submitting of changes that just were done."
rm -r "$WORKDIR"
