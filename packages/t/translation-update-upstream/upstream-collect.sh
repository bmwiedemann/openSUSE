#!/bin/bash

# This program collects all upstream translations defined in
# configuration and merges them together.

# If you want to use po files for completing of translations, you can remove --no-fuzzy-matching.
# It will run much slower, but you could start with fuzzy matches.

# Debug mode. Set to true if you want to keep working directories.
DEBUG=false
# Incremental mode. With exception of bootstrapping or resetting the memory, it should be true.
# Non-incremental update cannot process a single package.
# FIXME: The incremental mode does not drop obsolete packages. You
# need to delete them manually afterwards using time stamp.
INCREMENTAL=true
# Set to false to generate only pot files, true to collect po files.
COLLECT_UPSTREAM=true
# Number of CPUs. When > 1, then parallel processing of more po files is possible.
CPUS=$(cat /proc/cpuinfo | grep processor | wc -l)
WORK_DIR=$PWD

set -o errexit
shopt -s nullglob

rpm -q obs-service-tar >/dev/null
rpm -q obs-service-recompress >/dev/null

source ${0%.sh}.conf

function get_pot_name {
	POT=
	for POT in *.pot ; do
	    :
	done
}

function validate_po_with_plural_check {
    local LOG=$HOME/.validate${1##*/}.log$$
    trap "rm -f $LOG" 0
    if LC_ALL=C LANG=C msgfmt -c -o /dev/null "$1" 2>$LOG ; then
	RC=0
    else
	RC=1
    fi
    PLURAL_FAILURE=false
    if grep -q 'plural form' $LOG ; then
	PLURAL_FAILURE=true
    fi
    rm $LOG
    trap - 0
    return $RC
}

function validate_po {
    LC_ALL=C LANG=C msgfmt -c -o /dev/null "$1"
}

function rpmprep {
    RPMDIR=$HOME/.var.rpmpatch$$
    rm -rf BUILD $HOME/.var.rpmpatch$$
    trap "rm -rf $RPMDIR" 0
    mkdir -p BUILD $RPMDIR
    # Add "%BUILD_ORIG 1" to support original source translation:
    cat >$RPMDIR/macros <<EOF
%_sourcedir      $PWD
%_builddir       $PWD/BUILD
EOF

    sed -i '
	# Remove <RELEASE> tag from Release and delete shell escape comments.
	/^Release:/s/[<>]//g
	# Remove bash shell escape comments (gstreamer, calls autoreconf that can fail).
	/#%(bash/d
	# Remove negative expressions in BuildRequires.
	:1
	s/^\(BuildRequires:.*[[:space:]]\)-[^[:space:]]*/\1/
	t1
	/^BuildRequires:[[:space:]]*$/d
	# Modify some requirements to work without relevant packages installed.
	s/%{xulrunner_version}/dummy/g
	s/%{mozilla_ver}/dummy/g
	s/%{glib2_gsettings_schema_requires}/Requires: dummy/g
	s/%glib2_gsettings_schema_requires/Requires: dummy/g
	s/%{gtk2_immodule_requires}/Requires: dummy/g
	s/%{gtk3_immodule_requires}/Requires: dummy/g
	s/%{py_requires}/Requires: dummy/g
	s/%py_requires/Requires: dummy/g
	s/%kde4_runtime_requires/Requires: dummy/g
	s/%systemd_requires/Requires: dummy/g
	s/%gconf_schemas_prereq/Requires: dummy/g
	s/%{gconf_schemas_prereq}/Requires: dummy/g
	s/%glib2_gio_module_requires/Requires: dummy/g
	s/%{glib2_gio_module_requires}/Requires: dummy/g
	s/%{_bluezVersion}/0/g
	' *.spec
    eval rpmbuild --macros=/usr/lib/rpm/macros:/usr/lib/rpm/suse_macros:/usr/lib/rpm/suse/macros:/usr/lib/rpm/macros.d/macros.systemd:/usr/lib/rpm/platform/$(uname -i)-linux/macros:/etc/rpm/\\\*:$RPMDIR/macros --nodeps -bp ${*:-*.spec}
    rm -rf $RPMDIR
    trap - 0
}

ONLY_PACKAGES=()
FULL_PROCESS=true
SNAPSHOT=$(LC_ALL=C LANG=C date +%Y%m%d)
MSNAPSHOT=$SNAPSHOT
case $1 in
    --help )
	# "only_new" is tricky: Processing new is the default. "only_new" has no match => only_new.
	echo "Usage: $0 [ package | only_new ]"
	exit
	;;
    # no arguments: process everything
    "" )
	;;
    * )
	ONLY_PACKAGES=("$@")
	FULL_PROCESS=false
	;;
esac

rm -rf UPSTREAM
mkdir UPSTREAM
if ! test -d STAMPS ; then
    mkdir -p pot pot-tuu pot-diff
    mkdir OSC PACKAGES UPDATE STAMPS
    rm -f upstream-collect.log
    rm -f upstream-collect.domain-map.tmp
fi

# wd may contain ":" in the name, use ~/ instead:
mkdir -p ~/.upstream-collect.tmp
cat >~/.upstream-collect.tmp/translation-update-upstream <<EOF
#!/bin/sh
echo "Dummy translation-update-upstream for upstream-collect.sh. Skipping merge of old translations."

DOMAIN=\$2
USE_MESON=false
if test -f meson.build -a ! \( -f \${1:-po}/Makefile.in.in -o -f \${1:-po}/Makefile.in -o -f \${1:-po}/Makefile \) ; then
    echo "Switching to meson style pot file extraction." >&2
    USE_MESON=true
    if test -z "\$DOMAIN" ; then
	MESON_PROJECT="\$(sed -n "/^project(/,+1{1{h;d};2{x;G}};s/^project[[:space:]]*([[:space:]]*'\([^']*\)'.*/\1/p" <meson.build)"
	DOMAIN="\$(sed -n "s/meson.project_name[[:space:]]*([[:space:]]*)/'\$MESON_PROJECT'/g;s/.*\.set_quoted[[:space:]]*('GETTEXT_PACKAGE',[[:space:]]'\([^']*\)').*/\1/p" <meson.build)"
	if test -z "\$DOMAIN" ; then
	    if ! grep -q GETTEXT_PACKAGE meson.build ; then
		DOMAIN="\$MESON_PROJECT"
	    else
		echo "Error: Gettext domain cannot be determined." >&2
		exit 1
	    fi
	fi
    fi
fi
USE_INTLTOOL=false
if test -f configure.ac ; then
    if grep PROG_INTLTOOL configure.ac ; then
	USE_INTLTOOL=true
    fi
fi
if test -f configure.in ; then
    if grep PROG_INTLTOOL configure.in ; then
	USE_INTLTOOL=true
    fi
fi
DIR=\${1:-po}

if test -z "\$3" ; then
    if \$USE_MESON ; then
	if test -f POTFILES ; then
	    POTFILES="\$PWD/\${1:-po}/POTFILES"
	else
	    POTFILES="\$PWD/\${1:-po}/POTFILES.in"
	fi
    echo "cd \\"\$PWD\\"
xgettext --package-name=\\"\$DOMAIN\\"\\\\
	-p \\"\$PWD\\"\\\\
	-f \\"\$POTFILES\\"\\\\
	-D \\"\$PWD\\"\\\\
	-k_ -o \\"\$PWD/\${1:-po}/\$DOMAIN.pot\\"\\\\
	--keyword=NC_:1c,2\\\\
	--flag=g_strdup_printf:1:c-format\\\\
	--flag=g_set_error:4:c-format\\\\
	--flag=g_dngettext:2:pass-c-format\\\\
	--flag=g_string_printf:2:c-format\\\\
	--add-comments\\\\
	--from-code=UTF-8\\\\
	--keyword=C_:1c,2\\\\
	--flag=N_:1:pass-c-format\\\\
	--flag=g_string_append_printf:2:c-format\\\\
	--flag=C_:2:pass-c-format\\\\
	--keyword=N_\\\\
	--flag=g_error_new:3:c-format\\\\
	--flag=NC_:2:pass-c-format\\\\
	--keyword=g_dngettext:2,3\\\\
	--keyword=g_dpgettext2:2c,3\\\\
	--keyword=_\\\\
	--keyword=g_dcgettext:2" >\${1:-po}/.translation-update-upstream-implemented
    else
	if \$USE_INTLTOOL ; then
	    if test -z "\$DOMAIN" ; then
		echo "intltool-update --pot" >\${1:-po}/.translation-update-upstream-implemented
	    else
		intltool-update --gettext-package=\$DOMAIN --pot
		echo "intltool-update --gettext-package=\$DOMAIN --pot" >\${1:-po}/.translation-update-upstream-implemented
	    fi
	else
	# Fallback: use xgettext with default options except those that we
	# cannot guess (it can stil fail, as options can be customized).
	    echo "cd \\"\$DIR\\"
	    if test -z \\"\$DOMAIN\\" ; then
		## Ugly hack! intltool could return invalid po, but its
		## FindPackageName() can guess domain.  Call it to get it.
		intltool-update --pot
		for POT in *.pot ; do
		    DOMAIN=\\\${POT%.pot}
		done
	    fi
	    xgettext --default-domain=\\"\$DOMAIN\\" --directory=\\"\$OLDPWD\\" \\\\
		     --add-comments=TRANSLATORS: --from-code=UTF-8 --keyword=_ --keyword=N_ --keyword=C_:1c,2 --keyword=NC_:1c,2 --keyword=g_dngettext:2,3 --add-comments \\\\
		     --files-from=./POTFILES.in
	    mv \\"\\\$DOMAIN.po\\" \\"\\\$DOMAIN.pot\\"" >\${1:-po}/.translation-update-upstream-implemented
	fi
    fi
else
    echo \$3 >\${1:-po}/.translation-update-upstream-implemented
fi
cd \${1:-po}
# Generate and save a copy of the pot file now and compare later.
bash ./.translation-update-upstream-implemented
mkdir -p tuu
for POT in *.pot ; do
	cp -a \$POT tuu/
done
EOF
chmod +x ~/.upstream-collect.tmp/translation-update-upstream

# executable flag does not survive some build systems
chmod +x msgheadermerge msgheadermerge-compose msgheadermerge-parse upstream-collect.sh create-tlst-step*.sh translation-update-upstream-to-translation-update.sh

# Strings in installed instance of gnome-patch-translation may interfere
# with upstream-collect.sh. Use of dummies allows to import upstream
# strings, that are part of openSUSE patches.
for FILE in gnome-patch-translation-prepare gnome-patch-translation-update ; do
    cat >~/.upstream-collect.tmp/$FILE <<EOF
#!/bin/sh
set -x
echo "Dummy $FILE for upstream-collect.sh. Skipping gnome-patch-translation."
# gnome-patch-translation may be a symlink (libgweather), that is why we have to check even with mkdir -p.
if ! test -L gnome-patch-translation ; then
	mkdir -p gnome-patch-translation
fi
touch po/.gnome-patch-translation-implemented
EOF
    chmod +x ~/.upstream-collect.tmp/$FILE
done

export PATH=~/.upstream-collect.tmp:$PATH

# FIXME: Even in incremental mode, we should drop all updates that generate empty update file after the run. These files are obsolete, included into package, and may even degrade translation quality.
if $INCREMENTAL ; then
    # more tarballs are available => use the latest one
    # FIXME: Fix 20090213.10 < 20090213.9
    # (but it should not happen for people who update and submit)
    for ARCHIVE_ in translation-update-upstream-*.tar.bz2 ; do
	ARCHIVE=$ARCHIVE_
    done
    if ! test -f STAMPS/UPDATE_old_tarball ; then
	cd UPDATE
	echo "$(tput setf 3)Unpacking: $ARCHIVE$(tput init)"
	tar -jxf ../$ARCHIVE
	# If it is not a full process, increment only release
	# SNAPSHOT 20090213 -> 20090213.1, 20090213.1 -> 20090213.2
	cd ..
	touch STAMPS/UPDATE_old_tarball
    fi
    SNAPSHOT_RELEASE=${ARCHIVE#translation-update-upstream-}
    SNAPSHOT_RELEASE=${SNAPSHOT_RELEASE%.tar.bz2}
    SNAPSHOT_RELEASE_PART1=${SNAPSHOT_RELEASE%.*}
    SNAPSHOT_RELEASE_PART2=${SNAPSHOT_RELEASE#*.}
    if test "$SNAPSHOT_RELEASE_PART1" = "$SNAPSHOT_RELEASE" ; then
	SNAPSHOT_RELEASE_PART2=1
    else
	let SNAPSHOT_RELEASE_PART2++
    fi
    SNAPSHOT_RELEASE=$SNAPSHOT_RELEASE_PART1.$SNAPSHOT_RELEASE_PART2

    for ARCHIVE_ in translation-update-mandatory-*.tar.bz2 ; do
	ARCHIVE=$ARCHIVE_
    done
    if ! test -f STAMPS/UPDATE_old_mtarball ; then
	cd UPDATE
	echo "$(tput setf 3)Unpacking: $ARCHIVE$(tput init)"
	tar -jxf ../$ARCHIVE
	# If it is not a full process, increment only release
	# SNAPSHOT 20090213 -> 20090213.1, 20090213.1 -> 20090213.2
	cd ..
	touch STAMPS/UPDATE_old_mtarball
    fi
    MSNAPSHOT_RELEASE=${ARCHIVE#translation-update-mandatory-}
    MSNAPSHOT_RELEASE=${MSNAPSHOT_RELEASE%.tar.bz2}
    SNAPSHOT_RELEASE_PART1=${MSNAPSHOT_RELEASE%.*}
    SNAPSHOT_RELEASE_PART2=${MSNAPSHOT_RELEASE#*.}
    if test "$SNAPSHOT_RELEASE_PART1" = "$MSNAPSHOT_RELEASE" ; then
	SNAPSHOT_RELEASE_PART2=1
    else
	let SNAPSHOT_RELEASE_PART2++
    fi
    MSNAPSHOT_RELEASE=$SNAPSHOT_RELEASE_PART1.$SNAPSHOT_RELEASE_PART2
fi
if ! $FULL_PROCESS ; then
    SNAPSHOT=$SNAPSHOT_RELEASE
    MSNAPSHOT=$MSNAPSHOT_RELEASE
fi

SERIAL=0
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
	if test "$MANDATORY" = "mandatory" ; then
	    MANDATORY=true
	else
	    MANDATORY=false
	fi

	echo
	echo "$(tput setf 3)Processing: package=$PACKAGE domain=$DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:-(default)} mandatory=$MANDATORY$(tput init)"

	STATUS=OK
	# NOTE: Force a limitation: tlst rules for one package must be placed on contiguous line sequence
	if ! $DEBUG ; then
	    if test "$OLD_PACKAGE" != "$PACKAGE" ; then
		if test -n "$RPMPKGDIR" ; then
		    rm -rf $RPMPKGDIR $WORK_DIR/STAMPS/$PACKAGE/.builddir_ok
		fi
	    fi
	    OLD_PACKAGE=$PACKAGE
	fi

	if test -d $WORK_DIR/STAMPS/$PACKAGE/$DOMAIN/$METHOD/${REPO//[\/:.]/_}/$DIR/${BRANCH:-__HEAD__} ; then
	    echo "   Already successfully processed. Skipping..."
	    continue
	fi

	if test "${#ONLY_PACKAGES}" -gt 0 ; then
	    SKIP_PACKAGE=true
	    for ONLY_PACKAGE in "${ONLY_PACKAGES[@]}" ; do
	    	if test "$ONLY_PACKAGE" = "$PACKAGE" ; then
		    SKIP_PACKAGE=false
		    break
		fi
	    done
	    if $SKIP_PACKAGE ; then
		echo "   Not scheduled to process. Recycling old update..."
#FIXME		mkdir -p $WORK_DIR/STAMPS/$PACKAGE/$DOMAIN/$METHOD/${REPO//[\/:.]/_}/$DIR/${BRANCH:-__HEAD__}
#		touch $WORK_DIR/STAMPS/$PACKAGE/.builddir_ok
		continue
	    fi
	fi

	cd $WORK_DIR/OSC

	RPMPKGDIR=$WORK_DIR/PACKAGES/$PACKAGE

	if ! test -f $WORK_DIR/STAMPS/$PACKAGE/.builddir_ok ; then
	    if ! test -d "$RPMPKGDIR" ; then
		for OSC_REPOSITORY in "${OSC_REPOSITORIES[@]}" ; do
		    echo "Trying to check-out PACKAGES $PACKAGE from $OSC_REPOSITORY..."
		    # FIXME: When obs-service-download_url appears in Factory, use --source-service-files
		    if osc ${OSC_APIURL:+--apiurl=$OSC_APIURL} checkout --server-side-source-service-files --expand-link $OSC_REPOSITORY $PACKAGE >gnome-patch-translation-collect-tmp.log 2>&1 ; then
			cd $OSC_REPOSITORY/$PACKAGE
			if test -f _service ; then
			    for FILE in *.obscpio ; do
				cpio -d -i <$FILE
			    done
			    sed -i '/<service .*mode="disabled"\(\|.*[^\/]\)>/,/<\/service>/d;/<service .*mode="disabled".*\/>/d;s/mode="buildtime"//' _service
			    osc service runall
			fi
			cd "$OLDPWD"
			mv $OSC_REPOSITORY/$PACKAGE $WORK_DIR/PACKAGES/
			for FILE in $WORK_DIR/PACKAGES/$PACKAGE/_service\:download_url\:* ; do
				mv "$FILE" "${FILE/_service:download_url:/}"
			done
			break
		    fi
		    if ! grep -q "HTTP Error 404" gnome-patch-translation-collect-tmp.log ; then
			cat gnome-patch-translation-collect-tmp.log
			rm gnome-patch-translation-collect-tmp.log
			echo "ERROR: Checkout failed!"
			exit 1
		    fi
		done
		rm gnome-patch-translation-collect-tmp.log
	    else
		rm -rf "$RPMPKGDIR" $WORK_DIR/STAMPS/$PACKAGE
		echo "$(tput setf 4)Removed possibly incorrect temporary files from previous runs. Please re-run $0 now.$(tput init)"
		exit 1
	    fi
	    cd $RPMPKGDIR
	    rpmprep $PACKAGE.spec
	else
	# During processing, builddir may contain incomplete po files:
	    rm $WORK_DIR/STAMPS/$PACKAGE/.builddir_ok
	fi
	REPODIR=$DIR
	RPMPODIR=$(echo $RPMPKGDIR/BUILD/*/${DIR#*/})

	if test -f $WORK_DIR/${TLST%.tlst}.hook ; then
	    source $WORK_DIR/${TLST%.tlst}.hook
	fi

	cd $RPMPODIR
	get_pot_name
	REAL_DOMAIN=${POT%.pot}
	if test -f .gnome-patch-translation-implemented ; then
	    echo $PACKAGE >>$WORK_DIR/gnome-patch-translation.lst
	fi
	if test -f .translation-update-upstream-implemented ; then
	    if bash ./.translation-update-upstream-implemented ; then
	    	get_pot_name
		REAL_DOMAIN=${POT%.pot}
		cp -a $REAL_DOMAIN.pot $WORK_DIR/pot/
		# pot-tuu DOMAIN is the external domain - LCN may use different domain
		cp -a tuu/$REAL_DOMAIN.pot $WORK_DIR/pot-tuu/$DOMAIN.pot
		# Verify that patches don't introduce new strings.
		msgcomm --uniq $REAL_DOMAIN.pot tuu/$REAL_DOMAIN.pot -o $WORK_DIR/pot-diff/$DOMAIN.pot
		if ! test -f .gnome-patch-translation-implemented ; then
		    if test -f $WORK_DIR/pot-diff/$DOMAIN.pot ; then
			echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)}: new pot file contains unique strings, please check gnome-patch-translation"
			STATUS=OK_INCOMPLETE
		    fi
		fi
	    else
		# translation-update-upstream is implemented but fails:
	    	get_pot_name
		REAL_DOMAIN=${POT%.pot}
		if test -f $REAL_DOMAIN.pot ; then
		    echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)}: pot file update error, continuing with original $DOMAIN.pot"
		    STATUS=OK_OUTDATED
		    cp -a $DOMAIN.pot $WORK_DIR/pot/
		else
		    echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)}: pot file update error, no way to update"
		    STATUS=POT_ERROR
		    mkdir -p $WORK_DIR/STAMPS/$PACKAGE/$DOMAIN/$METHOD/${REPO//[\/:.]/_}/$REPODIR/${BRANCH:-__HEAD__}
		    # However we cannot do anything, build dir is successfully processed.
		    touch $WORK_DIR/STAMPS/$PACKAGE/.builddir_ok
		    continue
		fi
	    fi
	else
	    echo "$RPMPODIR: Missing or incorrect translation-update-upstream in the spec file."
	    # translation-update-upstream is implemented, try the default with the upstream domain:
	    cd ..
	    RC=0
	    if test -f meson.build -a ! \( -f po/Makefile.in.in -o -f po/Makefile.in -o -f po/Makefile \); then
		echo "Switching to meson style pot file extraction."
		MESON_PROJECT="$(sed -n "/^project(/,+1{1{h;d};2{x;G}};s/^project[[:space:]]*([[:space:]]*'\([^']*\)'.*/\1/p" <meson.build)"
		DOMAIN="$(sed -n "s/meson.project_name[[:space:]]*([[:space:]]*)/'$MESON_PROJECT'/g;s/.*\\.set_quoted[[:space:]]*('GETTEXT_PACKAGE',[[:space:]]'\([^']*\)').*/\1/p" <meson.build)"
		if test -f po/POTFILES ; then
		POTFILES="$PWD/po/POTFILES"
		else
		POTFILES="$PWD/po/POTFILES.in"
		fi
		xgettext --package-name="$DOMAIN"\
			-p "$PWD"\
			-f "$POTFILES"\
			-D "$PWD"\
			-k_ -o "$PWD/po/$DOMAIN.pot"\
			--keyword=NC_:1c,2\
			--flag=g_strdup_printf:1:c-format\
			--flag=g_set_error:4:c-format\
			--flag=g_dngettext:2:pass-c-format\
			--flag=g_string_printf:2:c-format\
			--add-comments\
			--from-code=UTF-8\
			--keyword=C_:1c,2\
			--flag=N_:1:pass-c-format\
			--flag=g_string_append_printf:2:c-format\
			--flag=C_:2:pass-c-format\
			--keyword=N_\
			--flag=g_error_new:3:c-format\
			--flag=NC_:2:pass-c-format\
			--keyword=g_dngettext:2,3\
			--keyword=g_dpgettext2:2c,3\
			--keyword=_\
			--keyword=g_dcgettext:2
		RC=$?
		cd -
	    else
		cd -
		USE_INTLTOOL=false
		if test -f configure.ac ; then
		    if grep PROG_INTLTOOL configure.ac ; then
			USE_INTLTOOL=true
		    fi
		fi
		if test -f configure.in ; then
		    if grep PROG_INTLTOOL configure.in ; then
			USE_INTLTOOL=true
		    fi
		fi
		if $USE_INTLTOOL ; then
		    if test -z "$DOMAIN" ; then
			intltool-update --pot
		    else
			intltool-update --gettext-package=$DOMAIN --pot
		    fi
		else
		    # Fallback: use xgettext with default options except those that we
		    # cannot guess (it can stil fail, as options can be customized).
		    if test -z "$DOMAIN" ; then
			## Ugly hack! intltool could return invalid po, but its
			## FindPackageName() can guess domain.  Call it to get it.
			if ! intltool-update --pot ; then
			    echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)}: packaging error, package does not call translation-update-upstream properly and intltool-update fails, no way to update"
			    STATUS=TUU_BROKEN
			    mkdir -p $WORK_DIR/STAMPS/$PACKAGE/$DOMAIN/$METHOD/${REPO//[\/:.]/_}/$REPODIR/${BRANCH:-__HEAD__}
			    # However we cannot do anything, build dir is successfully processed.
			    touch $WORK_DIR/STAMPS/$PACKAGE/.builddir_ok
			    continue
			fi
			for POT in *.pot ; do
			    DOMAIN=${POT%.pot}
			done
		    fi
		    xgettext --default-domain="$DOMAIN" --directory="$OLDPWD" \
			     --add-comments=TRANSLATORS: --from-code=UTF-8 --keyword=_ --keyword=N_ --keyword=C_:1c,2 --keyword=NC_:1c,2 --keyword=g_dngettext:2,3 --add-comments \
			     --files-from=./POTFILES.in
		    mv "$DOMAIN.po" "$DOMAIN.pot"
		fi
		get_pot_name
		REAL_DOMAIN=${POT%.pot}
		echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)}: packaging error, package does not call translation-update-upstream properly"
		STATUS=TUU_NOT_CALLED
		cp -a $DOMAIN.pot $WORK_DIR/pot/
	    fi
	fi

	echo $PACKAGE $REAL_DOMAIN $STATUS >>$WORK_DIR/upstream-collect.domain-map.tmp

	if $COLLECT_UPSTREAM ; then
		cd $WORK_DIR/UPSTREAM
		let SERIAL++ || :
		mkdir $SERIAL
		cd $SERIAL
		echo >.info "package=$PACKAGE domain=$DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)}"

		case "$METHOD" in
		    cvs )
			cvs -z3 -d:pserver:anoncvs@$REPO co $REPODIR $BRANCH
			cd $REPODIR
			;;
		    svn )
			if test -z "$BRANCH" ; then
			    svn co $REPO/${REPODIR%%/*}/trunk/${REPODIR#*/}
			else
			    svn co $REPO/${REPODIR%%/*}/branches/$BRANCH/${REPODIR#*/}
			fi
			cd ${REPODIR##*/}
			;;
		    git )
			if ! test -d $WORK_DIR/GIT/${REPO//[\/:.]/_} ; then
			    mkdir -p $WORK_DIR/GIT/${REPO//[\/:.]/_}
			    cd $WORK_DIR/GIT/${REPO//[\/:.]/_}
			    git clone $REPO
			    cd $OLDPWD
			fi
			cp -a $WORK_DIR/GIT/${REPO//[\/:.]/_}/* .
			if test -n "$BRANCH" ; then
			    cd *
			    git checkout remotes/origin/$BRANCH
			    cd $OLDPWD
			fi
			cd $REPODIR
			;;
		    # Web-based Git repository viewer makes possible to download particular file.
		    cgit )
			# Some tricks to be able to recycle git:// URI
			CGIT_URI=$REPO
			CGIT_URI=${CGIT_URI/git:\/\/anongit./https://cgit.}
			CGIT_URI=${CGIT_URI/git:\/\//https://}
			CGIT_BRANCH=${BRANCH:+?id=$BRANCH}
			CGIT_SERVER=${CGIT_URI#https://}
			CGIT_SERVER=${CGIT_SERVER%%/*}
			curl $CGIT_URI/tree/${REPODIR#*/}$CGIT_BRANCH | sed -n 's:^.*class='\''ls-blob[^'\'']*'\'' href='\''\([^'\'']*\)'\''.*$:\1:p' |
			    while read ; do
				wget -N http://$CGIT_SERVER${REPLY/\/tree\///plain/}
			    done
			;;
		    # standard http directory with po files (BRANCH is not supported)
		    http )
			wget -N -r --no-parent --level=1 http://$REPO/$REPODIR/$DIR
			cd $REPO/$REPODIR/$DIR
			;;
		    # GNOME Translation project l10n directory
		    gtp )
			GTP_NAME_BASE=${REPODIR%%/*}
			# Projects with multiple domains have custom handling in GTP.
			case $DOMAIN in
			    gimp20-libgimp ) GTP_NAME_BASE=gimp-libgimp ;;
			    gimp20-python ) GTP_NAME_BASE=gimp-python ;;
			    gimp20-script-fu ) GTP_NAME_BASE=gimp-script-fu ;;
			    gimp20-std-plug-ins ) GTP_NAME_BASE=gimp-plug-ins ;;
			    gimp20-tags ) GTP_NAME_BASE=gimp-tags ;;
			    gimp20-tips ) GTP_NAME_BASE=gimp-tips ;;
			    gnumeric-functions ) GTP_NAME_BASE=gnumeric-functions ;;
			    gtk20-properties ) GTP_NAME_BASE=gtk+-properties ;;
			    libgweather-locations ) GTP_NAME_BASE=locations ;;
			esac
			curl https://$REPO/${REPODIR%%/*}.${BRANCH:-master}/ | sed -n 's:^.*href="\([^"]*\.po\)".*$:\1:p' |
			    while read ; do
				case $REPLY in
				    *.reduced.po )
					;;
				    $GTP_NAME_BASE.${BRANCH:-master}.*)
					wget -N https://$REPO/${REPODIR%%/*}.${BRANCH:-master}/$REPLY
					mv $REPLY ${REPLY#$GTP_NAME_BASE.${BRANCH:-master}.}
					;;
				esac
			    done
			;;
		    tbz )
			wget -N $REPO
			tar -jxf ${REPO##*/}
			cd $REPODIR
			;;
		    tgz )
			wget -N $REPO
			tar -zxf ${REPO##*/}
			cd $REPODIR
			;;
		    txz )
			wget -N $REPO
			tar -Jxf ${REPO##*/}
			cd $REPODIR
			;;
		    static )
			if ! test -d $WORK_DIR/translation-update-static ; then
			    cd $WORK_DIR
			    tar -jxf translation-update-static.tar.bz2
			    cd -
			fi
			cp -a $WORK_DIR/translation-update-static/$DOMAIN .
			cd $DOMAIN
			;;
		    lcn )
			if ! test -d $WORK_DIR/LCN-${BRANCH:-trunk} ; then
			    mkdir  $WORK_DIR/LCN-${BRANCH:-trunk}
			    cd  $WORK_DIR/LCN-${BRANCH:-trunk}
			    if test "${BRANCH:-trunk}" = "trunk" ; then
				BRANCH_PATH="${BRANCH:-trunk}"
			    else
				BRANCH_PATH="branches/$BRANCH"
			    fi
			    svn co https://svn.opensuse.org/svn/opensuse-i18n/$BRANCH_PATH/lcn
			    for PO in lcn/*/po/*.po ; do
				LCN_LANG=${PO%/*}
				LCN_LANG=${LCN_LANG#lcn/}
				LCN_LANG=${LCN_LANG%%/*}
				LCN_DOMAIN=${PO##*/}
				LCN_DOMAIN=${LCN_DOMAIN%.$LCN_LANG.po}
				mkdir -p data/$LCN_DOMAIN
				ln $PO data/$LCN_DOMAIN/$LCN_LANG.po
			    done
			    cd -
			fi
			cp -a $WORK_DIR/LCN-${BRANCH:-trunk}/data/${REPODIR%/po} .
			cd ${REPODIR%/po}
			;;
		    * )
			echo "$PACKAGE: Unknown update method $METHOD"
			exit 1
			;;
		esac

#
# Files created in this section:
#
# upstream dir:
# foo-backport.po: raw upstream translation backported to the downstream
# foo-uheader.po: header with the upstream date from the branch modified as last
# foo-upstream.po: backport + updates from all upstreams processed before (date from the branch modified as last)
# foo-allfz.po: downstream + joined updates. Strings that were modified create fuzzy multi-match.
# foo-all.po: downstream + joined updates. Strings that were modified use the last processed instance.
# foo-fixes.po: Strings that are different while comparing downstream and joined updates.
# foo-additions.po: Strings that are newly introduced in joined updates while comparing with downstream.
# foo-header.po: header with the lastest date, either upstream date from the branch modified as last or the downstream date
# foo-fixes-clean.po: fixes with a nice header.
#
# downstream dir:
# foo-downstream.po: cleaned and complete downstream po file
# foo-updatesraw.po: fixes + additions in a single file, raw form
# foo-updates.po: fixes + additions in a single file, clean form with an useful header (this file will be copied to UPDATE/)
#
		for PO in *.po ; do
		(
		    if $MANDATORY ; then
			if ! validate_po $PO ; then
			    echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)} po=$PO: mandatory validation error!"
			    exit
			fi
			# Mandatory sources: copy the whole source to the mandatory po directory. Strings must not be skipped.
			mkdir -p $WORK_DIR/UPDATE/po-mandatory/$REAL_DOMAIN
			if test -f $WORK_DIR/UPDATE/po-mandatory/$REAL_DOMAIN/$PO ; then
			    msgcat --use-first $PO $WORK_DIR/UPDATE/po-mandatory/$REAL_DOMAIN/$PO -o $WORK_DIR/UPDATE/po-mandatory/$REAL_DOMAIN/$PO~
			    mv $WORK_DIR/UPDATE/po-mandatory/$REAL_DOMAIN/$PO~ $WORK_DIR/UPDATE/po-mandatory/$REAL_DOMAIN/$PO
			else
			    msgcat $PO -o $WORK_DIR/UPDATE/po-mandatory/$REAL_DOMAIN/$PO
			fi
			mkdir -p $WORK_DIR/po-mandatory-full/$REAL_DOMAIN
			if test -f $RPMPODIR/$PO ; then
			    # FIXME: Downstream po file may be invalid and cause invalid po-full po file. It does not
			    # create any regression, but it would be nice to try harder to fix brokenness.
			    if ! msgmerge --no-fuzzy-matching $RPMPODIR/$PO $RPMPODIR/$REAL_DOMAIN.pot -o $RPMPODIR/${PO%.po}-downstream.po ; then
				echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN repository=$REPO directory=$RPMPODIR branch=${BRANCH:(default)} po=$PO: package msgmerge error"
				# Failed initial msgmerge is fatal. There is no way to update. Build may fail.
				exit
			    fi
			    msgcat --use-first --force-po $PO $RPMPODIR/${PO%.po}-downstream.po -o $RPMPODIR/${PO%.po}-merged.po
			    msgattrib --no-obsolete $RPMPODIR/${PO%.po}-merged.po -o $WORK_DIR/po-mandatory-full/$REAL_DOMAIN/$PO
			else
			    msgattrib --no-obsolete $PO -o $WORK_DIR/po-mandatory-full/$REAL_DOMAIN/$PO
			fi
		    else
			# step 0: Merge new po file into old project. Removes unused (too new) translations.
			if ! msgmerge --no-fuzzy-matching $PO $RPMPODIR/$REAL_DOMAIN.pot -o ${PO%.po}-backport.po~ ; then
			    echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)} po=$PO: msgmerge error"
			    exit
			fi
			if ! validate_po ${PO%.po}-backport.po~ ; then
			    echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)} po=$PO: validation error (backported po file)"
			    exit
			fi
			if test -f $RPMPODIR/$PO ; then
			    # step 1: Clean the RPM po file to be safe.
			    if ! msgmerge --no-fuzzy-matching $RPMPODIR/$PO $RPMPODIR/$REAL_DOMAIN.pot -o $RPMPODIR/${PO%.po}-downstream.po ; then
				echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN repository=$REPO directory=$RPMPODIR branch=${BRANCH:(default)} po=$PO: package msgmerge error"
				# Failed initial msgmerge is fatal. There is no way to update. Build may fail.
				exit
			    fi
			    # Do the magic:
			    # step 2: Merge new upstream po and previous upstream updates to RPM po (if any).
			    OLD_UPDATE=false
			    PLURAL_FAILURE=false
			    if test -f $WORK_DIR/UPDATE/po/$REAL_DOMAIN/$PO ; then
				if ! $WORK_DIR/msgheadermerge $WORK_DIR/UPDATE/po/$REAL_DOMAIN/$PO $PO ${PO%.po}-uheader.po --mergemode --continue ; then
				    echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN repository=$REPO directory=$RPMPODIR branch=${BRANCH:(default)} po=$PO: old po file, skipping fixes"
				    OLD_UPDATE=true
				fi
				msgcat --force-po --use-first ${PO%.po}-uheader.po ${PO%.po}-backport.po~ $WORK_DIR/UPDATE/po/$REAL_DOMAIN/$PO -o ${PO%.po}-upstream.po
				if ! validate_po_with_plural_check ${PO%.po}-upstream.po ; then
					if $PLURAL_FAILURE ; then
						# Try to use downstream plural forms.
						$WORK_DIR/msgheadermerge $WORK_DIR/UPDATE/po/$REAL_DOMAIN/$PO $PO ${PO%.po}-uheader_opf.po --mergemode --continue --old-plural-forms
						msgcat --force-po --use-first ${PO%.po}-uheader_opf.po ${PO%.po}-backport.po~ $WORK_DIR/UPDATE/po/$REAL_DOMAIN/$PO -o ${PO%.po}-upstream.po
						if ! validate_po ${PO%.po}-upstream.po ; then
							echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN repository=$REPO directory=$RPMPODIR branch=${BRANCH:(default)} po=$PO: validation error (merged translation), possible plural forms clash"
							exit
						fi
					else
						echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN repository=$REPO directory=$RPMPODIR branch=${BRANCH:(default)} po=$PO: validation error (merged translation)"
						exit
					fi
				fi
			    else
				cp -a ${PO%.po}-backport.po~ ${PO%.po}-upstream.po
			    fi
			    # step 3: Join both translations, without --use-first string changes will disappear as fuzzy.
			    msgcat --force-po ${PO%.po}-upstream.po $RPMPODIR/${PO%.po}-downstream.po -o ${PO%.po}-allfz.po
			    msgcat --use-first --force-po ${PO%.po}-upstream.po $RPMPODIR/${PO%.po}-downstream.po -o ${PO%.po}-all.po
			    # step 4: Find string fixes (existed before, now different).
			    msgcat --force-po --unique ${PO%.po}-all.po ${PO%.po}-allfz.po -o ${PO%.po}-fixes.po~
			    # step 5: Find newly translated strings (translation removal is not supported).
			    msgcat --force-po --unique $RPMPODIR/${PO%.po}-downstream.po ${PO%.po}-all.po -o ${PO%.po}-additions.po~
			    # step 6: Join both to collect all known fixes.
			    if $OLD_UPDATE ; then
				# If the update has an old time stamp, don't include fixes. Use just additions.
				msgcat ${PO%.po}-additions.po~ -o $RPMPODIR/${PO%.po}-updatesraw.po
				# "updatesraw" can have inconsistent plural forms even if "upstream" has them consistent (bsc#894913).
				# Other failures are not possible here (superset was already validated).
				if ! validate_po_with_plural_check ${PO%.po}-updatesraw.po ; then
					# => There is no chance that --old-plural-forms succeeds. Don't try it and fail.
					echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN repository=$REPO directory=$RPMPODIR branch=${BRANCH:(default)} po=$PO: validation error (merged translation additions), possible plural forms clash"
					exit
				fi
			    else
				msgcat ${PO%.po}-fixes.po~ ${PO%.po}-additions.po~ -o $RPMPODIR/${PO%.po}-updatesraw.po
			    fi
			    # Are there any updates? If no, game over.
			    if test -f $RPMPODIR/${PO%.po}-updatesraw.po ; then
				# step 7: Compose the best po file header.
				if $PLURAL_FAILURE ; then
				    $WORK_DIR/msgheadermerge $RPMPODIR/$PO ${PO%.po}-upstream.po ${PO%.po}-header.po --newdate "" --old-plural-forms
				else
				    $WORK_DIR/msgheadermerge $RPMPODIR/$PO ${PO%.po}-upstream.po ${PO%.po}-header.po --newdate
				fi
				# step 8: And yet another ugly game to get rid commented out garbage.
				msgattrib --no-obsolete --force-po $RPMPODIR/${PO%.po}-updatesraw.po -o $RPMPODIR/${PO%.po}-updates.po~
				# step 9: Merge correct header to the updates file.
				msgcat --no-location --use-first ${PO%.po}-header.po $RPMPODIR/${PO%.po}-updates.po~ -o $RPMPODIR/${PO%.po}-updates.po
			    fi
			    # Prepare po-full file.
			    mkdir -p $WORK_DIR/po-full/$REAL_DOMAIN
			    if $OLD_UPDATE ; then
				$WORK_DIR/msgheadermerge ${PO%.po}-upstream.po $RPMPODIR/$PO ${PO%.po}-dheader.po --mergemode --continue
				msgcat --use-first --force-po ${PO%.po}-dheader.po $RPMPODIR/${PO%.po}-downstream.po ${PO%.po}-upstream.po -o ${PO%.po}-alldown.po
				msgattrib --no-obsolete ${PO%.po}-alldown.po -o $WORK_DIR/po-full/$REAL_DOMAIN/$PO
			    else
				msgattrib --no-obsolete ${PO%.po}-all.po -o $WORK_DIR/po-full/$REAL_DOMAIN/$PO
			    fi
			    # step 10: Prepare texts for review. We created them in previous steps, but files need cleanup.
			    if test -f ${PO%.po}-header.po ; then
				if test -f ${PO%.po}-additions.po~ ; then
				    msgattrib --no-obsolete --force-po ${PO%.po}-additions.po~ -o ${PO%.po}-additions.po
				    mkdir -p $WORK_DIR/po-review/${PO%.po}/additions
				    msgcat --use-first ${PO%.po}-header.po ${PO%.po}-additions.po -o $WORK_DIR/po-review/${PO%.po}/additions/$REAL_DOMAIN.po
				    rmdir --ignore-fail-on-non-empty --parents $WORK_DIR/po-review/${PO%.po}/additions
				fi
				if test -f ${PO%.po}-fixes.po~ ; then
				    msgattrib --no-obsolete --force-po ${PO%.po}-fixes.po~ -o ${PO%.po}-fixes.po
				    msgcat --use-first ${PO%.po}-header.po ${PO%.po}-fixes.po -o ${PO%.po}-fixes-clean.po
				fi
				if test -f ${PO%.po}-fixes-clean.po ; then
				    msgmerge ${PO%.po}-allfz.po ${PO%.po}-fixes-clean.po -o ${PO%.po}-fixes-review.po~
				    msgattrib --no-obsolete --force-po ${PO%.po}-fixes-review.po~ -o ${PO%.po}-fixes-review.po~~
				    msgcat ${PO%.po}-fixes-review.po~~ -o ${PO%.po}-fixes-review.po
				    if $OLD_UPDATE ; then
					mkdir -p $WORK_DIR/po-review/${PO%.po}/excluded-changes/${REPO//[\/:.]/_}/$REPODIR
					cp -a ${PO%.po}-fixes-clean.po $WORK_DIR/po-review/${PO%.po}/excluded-changes/${REPO//[\/:.]/_}/$REPODIR/$REAL_DOMAIN.po
					cp -a ${PO%.po}-fixes-review.po $WORK_DIR/po-review/${PO%.po}/excluded-changes/${REPO//[\/:.]/_}/$REPODIR/$REAL_DOMAIN-review.po
					rmdir --ignore-fail-on-non-empty --parents $WORK_DIR/po-review/${PO%.po}/excluded-changes/${REPO//[\/:.]/_}/$REPODIR
					if test -d $WORK_DIR/po-review/${PO%.po}/excluded-changes ; then
					    echo -e "Excluded changes contains changes introduced by upstream po files with\ntime stamp older than our package." >$WORK_DIR/po-review/${PO%.po}/excluded-changes/README
					fi
				    else
					mkdir -p $WORK_DIR/po-review/${PO%.po}/changes
					cp -a ${PO%.po}-fixes-clean.po $WORK_DIR/po-review/${PO%.po}/changes/$REAL_DOMAIN.po
					cp -a ${PO%.po}-fixes-review.po $WORK_DIR/po-review/${PO%.po}/changes/$REAL_DOMAIN-review.po
					rmdir --ignore-fail-on-non-empty --parents $WORK_DIR/po-review/${PO%.po}/changes
				    fi
				fi
			    fi
			else
			    # Test is not needed in current msgmerge, file is generated even if there is nothing inside.
			    if test -f ${PO%.po}-backport.po~ ; then
				# step 1: Merge new po and previous updates (if any).
				msgattrib --no-obsolete --no-fuzzy --translated ${PO%.po}-backport.po~ -o ${PO%.po}-backport.po
				if ! test -f ${PO%.po}-backport.po ; then
				    # backport file does not contain anything useful
				    exit
				fi
				if test -f $RPMPODIR/${PO%.po}-updates.po ; then
				    if ! msgcat --force-po --use-first ${PO%.po}-backport.po $RPMPODIR/${PO%.po}-updates.po -o $RPMPODIR/${PO%.po}-updates.po~ ; then
					echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)} po=$PO: msgcat error"
					exit
				    fi
				    mv $RPMPODIR/${PO%.po}-updates.po~ $RPMPODIR/${PO%.po}-updates.po
				else
				    # To get surely a valid po file, use msgcat instead of cp.
				    if ! msgcat ${PO%.po}-backport.po -o $RPMPODIR/${PO%.po}-updates.po ; then
					echo >>$WORK_DIR/upstream-collect.log "package=$PACKAGE domain=$DOMAIN gettext-package=$REAL_DOMAIN method=$METHOD repository=$REPO directory=$DIR branch=${BRANCH:(default)} po=$PO: msgcat error"
					exit
				    fi
				fi
				# step 2: Prepare texts for review.
				mkdir -p $WORK_DIR/po-review/${PO%.po}/new-files
				cp -a $RPMPODIR/${PO%.po}-updates.po $WORK_DIR/po-review/${PO%.po}/new-files/$REAL_DOMAIN.po
				rmdir --ignore-fail-on-non-empty --parents $WORK_DIR/po-review/${PO%.po}/new-files
				mkdir -p $WORK_DIR/po-full/$REAL_DOMAIN
				cp -a $RPMPODIR/${PO%.po}-updates.po $WORK_DIR/po-full/$REAL_DOMAIN/$PO
			    fi
			fi
		    fi
		) &
		    if test $CPUS -le 1 ; then
			wait
		    else
			echo "JOBS: New job launched."
			SHOWME=true
			while test $(jobs -p | wc -l) -ge $CPUS ; do
				if $SHOWME ; then
					echo -n "JOBS: $CPUS jobs running. Will check later~"
					SHOWME=false
				else
					echo -n "~"
				fi
				sleep 3
			done
		    fi
		    if ! $SHOWME ; then
			echo "JOBS: Releasing."
		    fi
		done
		if test $CPUS -gt 1 ; then
		    echo "JOBS: All tasks launched. Waiting for results."
		    wait
		fi

		mkdir -p $WORK_DIR/UPDATE/po/$REAL_DOMAIN
		cd $RPMPODIR
		for POX in *-updates.po ; do
		    PO=${POX/-updates/}
		    cp -a $POX $WORK_DIR/UPDATE/po/$REAL_DOMAIN/$PO
		done

		if ! $DEBUG ; then
		    rm -rf $WORK_DIR/UPSTREAM/$SERIAL
		fi

	fi

	mkdir -p $WORK_DIR/STAMPS/$PACKAGE/$DOMAIN/$METHOD/${REPO//[\/:.]/_}/$DIR/${BRANCH:-__HEAD__}
	touch $WORK_DIR/STAMPS/$PACKAGE/.builddir_ok

    done
done

if ! $DEBUG ; then
    if test -n "$RPMPKGDIR" ; then
	rm -rf $RPMPKGDIR $WORK_DIR/STAMPS/$PACKAGE/.builddir_ok
    fi
fi

if $COLLECT_UPSTREAM ; then
	cd $WORK_DIR/UPDATE
	if test -d po ; then
	    tar -j -c -f $WORK_DIR/translation-update-upstream-$SNAPSHOT.tar.bz2 po
	fi
	if test -d po-mandatory ; then
	    tar -j -c -f $WORK_DIR/translation-update-mandatory-$MSNAPSHOT.tar.bz2 po-mandatory
	fi
fi

if $FULL_PROCESS ; then
	# FIXME: Partial process should be able to update corresponding parts of domain-map.
	echo >$WORK_DIR/upstream-collect.domain-map "# This file was generated $(LANG=C LC_ALL=C date) by upstream-collect.sh."
	LC_ALL=C LANG=C sort -u <$WORK_DIR/upstream-collect.domain-map.tmp >>$WORK_DIR/upstream-collect.domain-map
	rm $WORK_DIR/upstream-collect.domain-map.tmp
fi

cd $WORK_DIR
if ! $DEBUG ; then
    rm -rf UPSTREAM OSC PACKAGES UPDATE UPDATE_OLD STAMPS BIN translation-update-static
fi
rm -rf ~/.upstream-collect.tmp

echo ""
echo "$(tput setf 2)Done. Please update version date in the spec file.$(tput init)"
