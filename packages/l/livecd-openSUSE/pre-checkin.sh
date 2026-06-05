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
        PACKAGES="$PACKAGES\n    <!-- OBS-IgnorePackage: $1 -->"
        PACKAGES="$PACKAGES\n    <ignore name=\"$1\"/>"
}

installPattern() {
	PACKAGES="$PACKAGES\n    <namedCollection name=\"$1\"/>"
}

archive() {
	PACKAGES="$PACKAGES\n    <archive name=\"$1\"/>"
}

for distro in leap tumbleweed; do
	for flavor in gnome kde xfce x11; do
		uppercaseflavor="$(echo "${flavor}" | tr [:lower:] [:upper:])"

		if [ "${distro}" = "leap" ]; then
			distroname="openSUSE Leap %OS_VERSION_ID%"
			BOOTSTRAP_PACKAGES="<package name=\"Leap-release\"/>"
			# No flavor-specific release flavor packages (yet)
		else
			distroname="openSUSE Tumbleweed"
			BOOTSTRAP_PACKAGES="<package name=\"openSUSE-release\"/>"
			BOOTSTRAP_PACKAGES="$BOOTSTRAP_PACKAGES\n    <package name=\"openSUSE-release-livecd-${flavor}\"/>"
		fi

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
		     s#@BOOTSTRAP_PACKAGES@#${BOOTSTRAP_PACKAGES}#g;\
		     s#@PACKAGES@#${PACKAGES}#g;" livecd.kiwi.in > livecd-${distro}-${flavor}.kiwi      
	done
done
