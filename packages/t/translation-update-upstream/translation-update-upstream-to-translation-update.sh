#!/bin/bash

# This program searches for packages that are not updated and extracts
# their translation updates to a separate tarball that can be used by
# translation-update package.

WORK_DIR=$PWD

set -o errexit
shopt -s nullglob

if ! test -f upstream-collect.domain-map ; then
    echo "Missing generated files. Please make a full run of ./upstream-collect.sh first."
    exit 1
fi

if ! test -d gnome-patch-translation ; then
    echo "Please provide directory gnome-patch-translation with contents of"
    echo "/usr/share/gnome-patch-translation from gnome-patch-translation RPM"
    echo "on the target system."
    exit 1
fi

source ${0%translation-update-upstream-to-translation-update.sh}upstream-collect.conf

mkdir\
 TRANSLATION_UPDATE TRANSLATION_UPDATE/translation-update TRANSLATION_UPDATE/TUU\
 TRANSLATION_UPDATE/NOT_UPDATED \
 TRANSLATION_UPDATE/UPDATED \
 TRANSLATION_UPDATE/complete TRANSLATION_UPDATE/rebuilt \
 TRANSLATION_UPDATE/complete/translation-update TRANSLATION_UPDATE/rebuilt/translation-update

# more tarballs are available => use the latest one
# FIXME: Fix 20090213.10 < 20090213.9
# (but it should not happen for people who update and submit)
for ARCHIVE in translation-update-upstream-*.tar.bz2 ; do
    :
done
tar -jtf $ARCHIVE >${0%.sh}-updates.lst
SNAPSHOT=${ARCHIVE%.tar.bz2}
SNAPSHOT=${SNAPSHOT#translation-update-upstream-}
for ARCHIVE in translation-update-mandatory-*.tar.bz2 ; do
    :
done
MSNAPSHOT=${ARCHIVE%.tar.bz2}
MSNAPSHOT=${MSNAPSHOT#translation-update-mandatory-}
if [[ "$MSNAPSHOT" > "$SNAPSHOT" ]] ; then
    SNAPSHOT=$MSNAPSHOT
fi

# FIXME: It should list all gnome-patch-translation references, not only the first on the line.
# But there is a bug in the gnome-patch-translation: Only first reference contain domain.
# Hopefully, the output is complete even with it.
sed -n 's%^#: \([^/]*\).*$%\1%p' gnome-patch-translation/gnome-patch-translation.pot | sort -u >${0%.sh}-gpt.lst

# Process translations to get complete sets of strings.
cd po-full
for DOMAIN in * ; do
    if grep -q "^$DOMAIN\$" ../${0%.sh}-gpt.lst ; then
	SUPPORTS_GPT=true
    else
	SUPPORTS_GPT=false
    fi
    for PO in $DOMAIN/*.po ; do
	LNG=${PO##*/}
	LNG=${LNG%.po}
	mkdir -p "../TRANSLATION_UPDATE/complete/translation-update/$DOMAIN/$LNG"

	if test -f "../po-mandatory-full/$PO" ; then
	    if $SUPPORTS_GPT && test -f "../gnome-patch-translation/$LNG.po" ; then
		# mandatory strings take precedence over gnome-patch-translation, but gnome-patch-translation takes precedence over upstream.
		msgcat --use-first "../po-mandatory-full/$PO" "../gnome-patch-translation/$LNG.po" "$PO" -o "../TRANSLATION_UPDATE/complete/translation-update/$DOMAIN/$LNG/$LNG.po.p1"
		# There are mandatory strings. We must update.
		mkdir -p "../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN"
		echo "po-mandatory-full/$PO" >"../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN/$LNG"
	    else
		msgcat --use-first "../po-mandatory-full/$PO" "$PO" -o "../TRANSLATION_UPDATE/complete/translation-update/$DOMAIN/$LNG/$LNG.po"
		# There are mandatory strings. We must update.
		mkdir -p "../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN"
		touch "../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN/$LNG"
	    fi
	else
	    if $SUPPORTS_GPT && test -f "../gnome-patch-translation/$LNG.po" ; then
		msgcat --use-first "../gnome-patch-translation/$LNG.po" "$PO" -o "../TRANSLATION_UPDATE/complete/translation-update/$DOMAIN/$LNG/$LNG.po.p1"
		# We don't know, whether strings from gnome-patch-translation were updated. There is no check yet. We must update.
		mkdir -p "../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN"
		echo "po-full/$PO" >"../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN/$LNG"
	    else
		ln "$PO" "../TRANSLATION_UPDATE/complete/translation-update/$DOMAIN/$LNG/$LNG.po"
	    fi
	fi
    done
done

cd ../po-mandatory-full
for DOMAIN in * ; do
    if grep -q "^$DOMAIN\$" ../${0%.sh}-gpt.lst ; then
	SUPPORTS_GPT=true
    else
	SUPPORTS_GPT=false
    fi
    for PO in $DOMAIN/*.po ; do
	LNG=${PO##*/}
	LNG=${LNG%.po}
	# There are mandatory strings. We must update.
	mkdir -p "../TRANSLATION_UPDATE/complete/translation-update/$DOMAIN/$LNG"
	# Handle only po files not processed above.
	if ! test -f "../po-full/$PO" ; then
	    mkdir -p "../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN"
	    if $SUPPORTS_GPT -a -f "../gnome-patch-translation/$LNG.po" ; then
		# mandatory strings take precedence over gnome-patch-translation, but gnome-patch-translation takes precedence over upstream.
		msgcat --use-first "$PO" "../gnome-patch-translation/$LNG.po" -o "../TRANSLATION_UPDATE/complete/translation-update/$DOMAIN/$LNG/$LNG.po.p1"
		echo "po-mandatory-full/$PO" >"../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN/$LNG"
	    else
		ln "$PO" "../TRANSLATION_UPDATE/complete/translation-update/$DOMAIN/$LNG/$LNG.po"
		touch "../TRANSLATION_UPDATE/complete/stamp-force/$DOMAIN/$LNG"
	    fi
	fi
    done
done

# Finish processing of po files that included strings from gnome-patch-translation.
cd ../TRANSLATION_UPDATE/complete/translation-update
for POP1 in */*/*.po.p1 ; do
    PO=${POP1%.p1}
    DOMAIN=${PO%%/*}
    LNG=${PO%/*}
    LNG=${LNG#*/}

    # Include only gnome-patch-translation strings from particular domain.
    msgmerge --no-fuzzy-matching "$POP1" ../../../pot/$DOMAIN.pot -o "$PO.p2"
    msgattrib --no-obsolete "$PO.p2" -o "$PO.p3"

    # Put header from the most important source stored into stamp-force.
    # Extract header. Broken pipe is an expected behavior. Redirect stderr to /dev/null.
    msgmerge --quiet --force-po ../../../$(<"../stamp-force/$DOMAIN/$LNG") ../../../msgheadermerge-empty.pot -o "$PO.p4"
    msgattrib --no-obsolete --force-po "$PO.p4" -o "$PO.p5"
    msgcat --use-first --force-po "$PO.p5" "$PO.p3" -o "$PO"

    rm "$PO.p"*
done

cd ../..

# Now create a copy of all files to TUU (they will be moved later to particular directories).
cp -al complete/translation-update/* TUU/

cd ..

osc ${OSC_APIURL:+--apiurl=$OSC_APIURL} ls "${OSC_REPOSITORIES[OSC_MAIN_INDEX]}" >${0%.sh}-rebuilt.lst
if test -n "$OSC_PROPOSED_INDEX" ; then
    osc ${OSC_APIURL:+--apiurl=$OSC_APIURL} ls "${OSC_REPOSITORIES[OSC_PROPOSED_INDEX]}" >${0%.sh}-outdated.lst
else
    echo -n '' >${0%.sh}-outdated.lst
fi

for TLST in *.tlst ; do
    exec <$WORK_DIR/$TLST

    while read PACKAGE DOMAIN METHOD REPO DIR BRANCH MANDATORY ; do

	# Continue for empty lines and comments
	if test "${PACKAGE###}" != "$PACKAGE" ; then
	    continue
	fi
	if test -z "$PACKAGE" ; then
	    continue
	fi

	echo "$(tput setf 3)Processing: package=$PACKAGE domain=$DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:-(default)} mandatory=$MANDATORY$(tput init)"
	PACKAGE_REBUILT_UP_TO_DATE=false
	if grep -q "^$PACKAGE\$" ${0%.sh}-rebuilt.lst ; then
	    if grep -q "^$PACKAGE\$" ${0%.sh}-outdated.lst ; then
		echo " is rebuilt in the distro, but has pending translation related update, adding"
	    else
		PACKAGE_REBUILT_UP_TO_DATE=true
		echo " is rebuilt in the distro, not adding"
	    fi
	else
	    echo " not rebuilt in the distro, adding"
	fi

	if $PACKAGE_REBUILT_UP_TO_DATE ; then
	    cat ${0%translation-update-upstream-to-translation-update.sh}upstream-collect.domain-map |
	    while read PACKAGE_ REAL_DOMAIN STATUS ; do
		if test "$PACKAGE" = "$PACKAGE_" ; then
		    case $STATUS in
			OK*)
			    echo " domain $REAL_DOMAIN is correctly updated, OK"
			    if test -d TRANSLATION_UPDATE/TUU/$REAL_DOMAIN ; then
				mv TRANSLATION_UPDATE/TUU/$REAL_DOMAIN TRANSLATION_UPDATE/UPDATED/
			    fi
			    ;;
			*)
			    echo " domain $REAL_DOMAIN is not correctly updated, needs to be added"
			    if test -d TRANSLATION_UPDATE/TUU/$REAL_DOMAIN ; then
				mv TRANSLATION_UPDATE/TUU/$REAL_DOMAIN TRANSLATION_UPDATE/NOT_UPDATED/
			    fi
			    ;;
		    esac
		fi
	    done
	else
	    cat ${0%translation-update-upstream-to-translation-update.sh}upstream-collect.domain-map |
	    while read PACKAGE_ REAL_DOMAIN STATUS ; do
		if test "$PACKAGE" = "$PACKAGE_" ; then
		    if test -d TRANSLATION_UPDATE/TUU/$REAL_DOMAIN ; then
			mv TRANSLATION_UPDATE/TUU/$REAL_DOMAIN TRANSLATION_UPDATE/NOT_UPDATED/
		    fi
		fi
	    done
	fi
	echo
    done
done

# If files remain in TUU, there is something wrong. Move them to NOT_UPDATED and hope that domain is correct.
# It can happen when domain mapping process failed.
cd TRANSLATION_UPDATE/TUU
for DIR in * ; do
    echo "$(tput setf 4)Something went wrong, domain=${DIR#*/} was not listed and processed$(tput init)"
    echo "  assuming that it was not updated"
    mv $DIR ../NOT_UPDATED/$DIR
done

cd ../NOT_UPDATED
for PO in */*/*.po ; do
    DOMAIN=${PO%%/*}
    LNG=${PO%/*}
    LNG=${LNG#*/}

    # Standard update: Pick only files with changes.
    if grep -q "^po/$DOMAIN/$LNG.po\$" ../../${0%.sh}-updates.lst ; then
	mkdir -p "../translation-update/$DOMAIN/$LNG"
	ln "../complete/translation-update/$PO" "../translation-update/$PO"
    fi
    # Mandatory update: Pick all files.
    if test -f "../complete/stamp-force/$DOMAIN/$LNG" ; then
	mkdir -p "../translation-update/$DOMAIN/$LNG"
	ln -f "../complete/translation-update/$PO" "../translation-update/$PO"
    fi
done
cd ../UPDATED
for PO in */*/*.po ; do
    DOMAIN=${PO%%/*}
    LNG=${PO%/*}
    LNG=${LNG#*/}

    # Standard update: Pick only files with changes.
    if grep -q "^po/$DOMAIN/$LNG.po\$" ../../${0%.sh}-updates.lst ; then
	mkdir -p "../rebuilt/translation-update/$DOMAIN/$LNG"
	ln "../complete/translation-update/$PO" "../rebuilt/translation-update/$PO"
    fi
    # Mandatory update: Pick all files.
    if test -f "../complete/stamp-force/$DOMAIN/$LNG" ; then
	mkdir -p "../rebuilt/translation-update/$DOMAIN/$LNG"
	ln -f "../complete/translation-update/$PO" "../rebuilt/translation-update/$PO"
    fi
done

cd ..
tar -jcf ../translation-update-from-translation-update-upstream-$SNAPSHOT.tar.bz2 translation-update
echo "Generated translation-update-from-translation-update-upstream-$SNAPSHOT.tar.bz2
Please add it to the package translation-update"
cd rebuilt
tar -jcf ../../translation-update-from-translation-update-upstream-rebuilt-$SNAPSHOT.tar.bz2 translation-update
echo "Generated translation-update-from-translation-update-upstream-rebuilt-$SNAPSHOT.tar.bz2
It contains translations that that should be provided in build time by translation-update-upstream,
but if translation-update-upstream was not updated to the latest version, then you may want to include
these translations to translation-update as well."
cd ../complete
tar -jcf ../../translation-update-from-translation-update-upstream-complete-$SNAPSHOT.tar.bz2 translation-update
echo "Generated translation-update-from-translation-update-upstream-complete-$SNAPSHOT.tar.bz2
This file includes all avaliable translations."
cd ../..
rm -r TRANSLATION_UPDATE
