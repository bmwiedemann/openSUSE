#!/bin/sh
set -u

install() {
	if [ -n "${2-}" ]; then
		PACKAGES="$PACKAGES\n    <package name=\"$1\" arch=\"$2\"/>"
	else
		PACKAGES="$PACKAGES\n    <package name=\"$1\"/>"
	fi
}

buildignore() {
	# Normally, <package name="foo" onlyarch="skipit"/> should work,
        # but https://github.com/openSUSE/obs-build/issues/420 requires a workaround
        ## Due to "--ignoreignore--" this has no effect either, so workaround the workaround
        ## by using <ignore/>, which gets ignored by OBS completely...
	if [ -n "${2-}" ]; then
		PACKAGES="$PACKAGES\n    <package name=\"aaa_base\" replaces=\"$1\" arch=\"$2\"/>"
		PACKAGES="$PACKAGES\n    <ignore name=\"$1\" arch=\"$2\"/>"
	else
		PACKAGES="$PACKAGES\n    <package name=\"aaa_base\" replaces=\"$1\"/>"
		PACKAGES="$PACKAGES\n    <ignore name=\"$1\"/>"
	fi
}

installPattern() {
	PACKAGES="$PACKAGES\n    <namedCollection name=\"$1\"/>"
}

archive() {
	PACKAGES="$PACKAGES\n    <archive name=\"$1\"/>"
}

for distro in leap tumbleweed; do
	distroname="openSUSE Tumbleweed"
	bootsplash="bgrt"
	releaseprefix="openSUSE"
	if [ "${distro}" = "leap" ]; then
		distroname="openSUSE Jump %OS_VERSION_ID%"
		# This changes every few weeks, apparently.
		#releaseprefix="Leap"
	fi

	for flavor in gnome kde xfce x11; do
		[ "${flavor}" = "xfce" -a "${distro}" = "leap" ] && continue # Prevent creation of livecd-leap-xfce.kiwi
		uppercaseflavor="$(echo "${flavor}" | tr [:lower:] [:upper:])"
	
		if [ "${flavor}" = "x11" ]; then
			name="${distroname} Rescue CD"
		else
			name="${distroname} ${uppercaseflavor} Live"
		fi

		PACKAGES="\n    <!-- list-common.sh -->"
		. "$PWD/list-common.sh"
		PACKAGES="$PACKAGES\n\n    <!-- list-${flavor}.sh -->"
		. "$PWD/list-${flavor}.sh"

		sed "s#@FLAVOR@#${flavor}#g;\
		     s#@NAME@#${name// /-}#g;\
		     s#@DISPLAYNAME@#${name}#g;\
		     s#@VOLID@#${name// /_}#g;\
		     s#@BOOTSPLASH@#${bootsplash}#g;\
		     s#@RELEASEPREFIX@#${releaseprefix}#g;\
		     s#@PACKAGES@#${PACKAGES}#g;" livecd.kiwi.in > livecd-${distro}-${flavor}.kiwi      
	done
done
