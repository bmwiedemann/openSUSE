#!/bin/bash

# This program creates makes dumb guesses about relation of upstream
# projects and openSUSE packages and creates initial configuration file.
#
# It needs osc and net access.
#
# It tries to assign packages to GNOME GTP projects and adds other known packages.
#

set -o errexit

source ${0%create-tlst-step2-create-gnome_gtp.sh}upstream-collect.conf

for REPOSITORY in ${OSC_REPOSITORIES[@]} ; do
	osc ${OSC_APIURL:+--apiurl=$OSC_APIURL} list $REPOSITORY
done | sort -u >create-tlst-temp-osc-projects.lst

# branches tried for all apps:
KNOWN_BRANCHES="gnome-3-34|gnome-3-36"
# branches tried apps with the same name base:
# Do not forget hardcoded strings in the code below!
APP_BRANCHES="|gimp-2-8|gimp-2-10|gtk-3-22|gtk-3-24|gtk-2-24|glib-2.62|glib-2.64"
# FIXME: support for libgda:release-3-0-branch gnome-background:gnome-2-22

echo "# This file was generated $(LANG=C LC_ALL=C date) by create-tlst-step2-create-gnome_gtp.sh." >upstream-gnome_gtp.tlst
echo "# package                   domain                                      method repository                       dir                        branch" >>upstream-gnome_gtp.tlst

SPACES='                                                                     '

# listing of all GNOME GTP projects
curl https://l10n.gnome.org/POT/ | sed -n 's:^.*href="\([^"]*\)/".*$:\1:p' | sed '/^$/d' |
	(
	while read ; do
	    BRANCH=${REPLY##*.}
	    REPLY=${REPLY%.*}
	    (
		grep -i ^$REPLY'\( \|\[0-9]\|-[0-9]\|-lang\)' create-tlst-temp-all-po-projects.lst || :
		# For network-manager*, try to match with NetworkManager
		if test "${REPLY#network-manager}" != "$REPLY" ; then
		    grep -i ^${REPLY/network-manager/NetworkManager}'\( \|\[0-9]\|-[0-9]\|-lang\)' create-tlst-temp-all-po-projects.lst
		fi

	    ) |
	    while read PACKAGE DOMAIN ; do
		if test "${PACKAGE%-lang}/$DOMAIN" = "NetworkManager/nm-applet" ; then
		    continue
		fi
		echo $REPLY ${PACKAGE%-lang} $DOMAIN $BRANCH
	    done
	done
        # Packages known to have special name in GTP:
	for LBRANCH in $KNOWN_BRANCHES master ; do
	    echo gconf gconf2 GConf2 $LBRANCH
	done
	echo glib glib2 glib20 glib-2-62
	echo glib glib2 glib20 glib-2-64
	echo glib glib2 glib20 master
	echo gtk+ gtk2 gtk20 gtk-2-24
	echo gtk+ gtk2 gtk20 master
	echo gtk+ gtk2 gtk20-properties gtk-2-24
	echo gtk+ gtk2 gtk20-properties master
	echo gtk+ gtk3 gtk30 gtk-3-24
	echo gtk+ gtk3 gtk30 master
	echo gtk+ gtk3 gtk30-properties gtk-3-24
	echo gtk+ gtk3 gtk30-properties master
	echo gnome-phone-manager phonemgr gnome-phone-manager gnome-3-34
	echo gnome-phone-manager phonemgr gnome-phone-manager gnome-3-36
	echo gnome-phone-manager phonemgr gnome-phone-manager master
	echo network-manager-applet NetworkManager-gnome nm-applet master
	echo udisks udisks2 udisks2 master
# For other versions than sles10:
#	echo network-manager-applet NetworkManager nm-applet
	) |
    while read PROJECT PACKAGE DOMAIN BRANCH ; do
	if test -z "$PACKAGE" ; then
	    continue
	fi
	# Test, whether package name is also the source name:
	if ! grep -q "^$PACKAGE\$" create-tlst-temp-osc-projects.lst ; then
	    continue
	fi

	# Projects known to use special directories:
	case $DOMAIN in
	    gimp20-libgimp )
		PO_DIR=po-libgimp
		;;
	    gimp20-script-fu )
		PO_DIR=po-script-fu
		;;
	    gimp20-python )
		PO_DIR=po-python
		;;
	    gimp20-std-plug-ins )
		PO_DIR=po-plug-ins
		;;
	    gimp20-tags )
		PO_DIR=po-tags
		;;
	    gimp20-tips )
		PO_DIR=po-tips
		;;
	    gtk20-properties )
		PO_DIR=po-properties
		;;
	    gnumeric-functions )
		PO_DIR=po-functions
		;;
	    # FIXME: Only some teams use GTP for gstreamer. Run 'find -name "*-fixes.po"' on processed downstream to find possible regressions.
	    gst-plugins-base-1.0 )
		PROJECT=gst-plugins-base
		;;
	    gst-plugins-good-1.0 )
		PROJECT=gst-plugins-good
		;;
	    gst-plugins-bad-1.0 )
		PROJECT=gst-plugins-bad
		;;
	    gst-plugins-ugly-1.0 )
		PROJECT=gst-plugins-ugly
		;;
	    libgweather-locations )
		PO_DIR=po-locations
		;;
	    * )
		PO_DIR=po
		;;
	esac
	USE_IT=false
	eval "case \"\$BRANCH\" in
	    $KNOWN_BRANCHES$APP_BRANCHES|master)
		USE_IT=true
		;;
	esac"
	if $USE_IT ; then
	    BRANCH=${BRANCH/master/zzzz_master}
	    echo "$PACKAGE${SPACES:0:28-${#PACKAGE}}$DOMAIN${SPACES:0:47-${#DOMAIN}}gtp l10n.gnome.org/POT               $PROJECT/$PO_DIR${SPACES:0:26-${#PROJECT}-${#PO_DIR}}$BRANCH"
	fi

# Disabled for now. Final merge will happen in spec file.
#	# We want to include LCN only for projects, which need merge with GNOME GTP.
#	if test -d translation-update-lcn/$DOMAIN ; then
#	    echo "$PACKAGE${SPACES:0:28-${#PACKAGE}}$DOMAIN${SPACES:0:27-${#DOMAIN}}zzzz_lcn"
#	fi

    done |
tee upstream-gnome_gtp_raw.lst |
LC_COLLATE=C LC_ALL= sort |
sed '
s/ *zzzz_master//
s/zzzz_lcn/lcn/
' >>upstream-gnome_gtp.tlst

# Remove temporary progress file:
rm upstream-gnome_gtp_raw.lst
rm create-tlst-temp-*
