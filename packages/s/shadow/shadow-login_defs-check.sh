#!/bin/bash

# login.defs and lib/getdef.c contain support for third party variables.
# It also contains support for variables that are unusable in installations with PAM support enabled.
# This script generates a list of used and unused variables in login.defs
# with respect to the current configuration.
# Arguments: arguments of osc build
# If the shadow-login_defs-check-unused.lst is generated, you should
# update login.defs.

set -o errexit

echo "Preparing..."

# Check for required commands
which quilt >/dev/null
which osc >/dev/null

# login.defs is shared with util-linux login, su and runuser.
# Extract list of referenced variables.
if ! test -f openSUSE:Factory/util-linux/BUILD/*/configure.ac ; then
	echo "Checking out util-linux..."
	if test -d ../util-linux ; then
		echo -n "../util-linux found. Are you preparing new version? (y/N) "
		read
		if test "${REPLY:0:1}" = "y" ; then
		mkdir -p openSUSE:Factory
			cp -a ../util-linux openSUSE:Factory/
		else
			osc co openSUSE:Factory util-linux
		fi
	else
		osc co openSUSE:Factory util-linux
	fi
	cd openSUSE:Factory/util-linux
# BEGIN HACK
# quilt does not understand our util-linux.spec.
	sed -i s/@BUILD_FLAVOR@// util-linux.spec
# END HACK
	quilt setup -d BUILD util-linux.spec
	cd $(ls -1d BUILD/* | sed /SPECPARTS/d)
	quilt push -a
	cd ../../../..
fi

echo "Extracting variables from util-linux..."
cd $(ls -1d openSUSE:Factory/util-linux/BUILD/* | sed /SPECPARTS/d)
(
	grep -rh getlogindefs . |
		sed -n 's/^.*getlogindefs[a-z_]*("\([A-Z0-9_]*\)".*$/\1/p'
	grep -rh logindefs_setenv . |
		sed -n 's/^.*logindefs_setenv*("[A-Z0-9_]*", "\([A-Z0-9_]*\)".*$/\1/p'
) |
	LC_ALL=C sort -u >../../../../shadow-login_defs-check-util-linux.lst
cd ../../../..

# login.defs is shared pam_unix*.so, pam_faildelay.so and pam_umask.so.
# Extract list of referenced variables.
if ! test -f openSUSE:Factory/pam/BUILD/*/configure.ac ; then
	echo "Checking out pam..."
	if test -d ../pam ; then
		echo -n "../pam found. Are you preparing new version? (y/N) "
		read
		if test "${REPLY:0:1}" = "y" ; then
		mkdir -p openSUSE:Factory
			cp -a ../pam openSUSE:Factory/
		else
			osc co openSUSE:Factory pam
		fi
	else
		osc co openSUSE:Factory pam
	fi
	cd openSUSE:Factory/pam
	quilt setup -d BUILD pam.spec
	cd $(ls -1d BUILD/* | sed /SPECPARTS/d)
	quilt push -a
	cd ../../../..
fi

echo "Extracting variables from pam..."
cd $(ls -1d openSUSE:Factory/pam/BUILD/* | sed /SPECPARTS/d)
grep -rh LOGIN_DEFS . |
	sed -n 's/CRYPTO_KEY/\"HMAC_CRYPTO_ALGO\"/g;s/^.*search_key *([A-Za-z_]*, *[A-Z_]*LOGIN_DEFS, *"\([A-Z0-9_]*\)").*$/\1/p' |
	LC_ALL=C sort -u >../../../../shadow-login_defs-check-pam.lst
cd ../../../..

if ! test -f shadow-login_defs-check-build/stamp ; then
	echo "Performing preprocessing of shadow by osc..."
	if ! test -f shadow.spec.shadow-login_defs-check-save ; then
		cp -a shadow.spec shadow.spec.shadow-login_defs-check-save

# In case of shadow, variables extraction is more complicated. The list
# depends on configure options, so we have to perform a fake build and
# extract variables from prepreocessed sources.
#		sed -i '/^%make_build/i\_smp_mpflags="%{?_smp_mpflags} -k CPPFLAGS=\\"-E\\""' shadow.spec
		sed -i 's/^%make_build/%make_build -k CPPFLAGS=\\"-E\\"/' shadow.spec
		if cmp -s shadow.spec shadow.spec.shadow-login_defs-check-save ; then
			echo "$0: Please fix sed expression modifying shadow.spec."
			mv shadow.spec.shadow-login_defs-check-save shadow.spec
			exit 1
		fi
	fi

	if osc build "$@" ; then
		echo "This build command was expected to fail, but it succeeded."
		echo "$0: Please fix sed expression modifying shadow.spec."
		mv shadow.spec.shadow-login_defs-check-save shadow.spec
		exit 1
	else
		echo "This build command was expected to fail."
		echo ""
	fi
	mv shadow.spec.shadow-login_defs-check-save shadow.spec

	BUILD_ROOT=$(osc lbl | sed -n 's/^.*Using BUILD_ROOT=//p')
	BUILD_DIR=$(osc lbl | sed -n 's/^.* cd //p' | head -n1)
	rm -rf shadow-login_defs-check-build
	mkdir shadow-login_defs-check-build
	cp -a "$BUILD_ROOT/$BUILD_DIR"/shadow-* shadow-login_defs-check-build/
	touch shadow-login_defs-check-build/stamp
fi

echo "Extracting list of deleted binaries..."
sed -n 's~rm %{buildroot}/%{_\(s\|\)bindir}/\(.*\)$~\2~p' <shadow.spec >shadow-login_defs-check-deleted.lst

# The build above is optional only for case of failure or edits in the
# code below. If any other build was performed, don't expect correct
# results.

cd shadow-login_defs-check-build/shadow-*

echo "Extracting variables from etc/login.defs..."
# Extract variables referenced in login.defs, both active and commented out.
sed -n "s/^#//;s/\([A-Z0-9_]*\)\([[:space:]].*\|\)$/\1/p" <etc/login.defs | sed '/^$/d' | uniq | sed '/^$/d' >../../shadow-login_defs-check-login_defs.lst
LC_ALL=C sort -u ../../shadow-login_defs-check-login_defs.lst >../../shadow-login_defs-check-login_defs-sorted.lst

echo "Extracting variables from lib/getdef.c..."
# Extract variables referenced in lib/getdef.c using current defines.
sed -n 's/^\(},\|\) {"\([A-Z0-9_]*\)", /\2/p' <lib/libshadow_la-getdef.o >../../shadow-login_defs-check-getdef.lst
LC_ALL=C sort -u ../../shadow-login_defs-check-getdef.lst >../../shadow-login_defs-check-getdef-sorted.lst

echo "Extracting variables from shadow..."
# Extract variables referenced in preprocessed files.
grep -r '\(getdef[a-z_]*\|call_script\|is_listed\) *( *"[A-Za-z0-9_]*"' |
	grep '[^ ]*\.o:' >../../shadow-login_defs-check-shadow.log

cd ../..

export RC=0
echo ""
echo ""
echo "Performing checks..."

sed '
	s/^.*\(getdef[a-z_]*\|call_script\|is_listed*\) *( *"\([A-Za-z0-9_]*\)".*$/\2/
'  <shadow-login_defs-check-shadow.log | LC_ALL=C sort -u >../../shadow-login_defs-check-shadow-all.lst

sed 's%^\(.*\)%/^.*\\\/\1\.o:/d%' <shadow-login_defs-check-deleted.lst >shadow-login_defs-check-deleted.sed
sed -f shadow-login_defs-check-deleted.sed <shadow-login_defs-check-shadow.log |
	sed '
	s/^.*\(getdef[a-z_]*\|call_script\|is_listed*\) *( *"\([A-Za-z0-9_]*\)".*$/\2/
' | LC_ALL=C sort -u  >shadow-login_defs-check-shadow-used.lst

if ! test -s shadow-login_defs-check-deleted.sed ; then
	echo "  BUG: Empty shadow-login_defs-check-deleted.sed Results will be unreliable!"
	if test $RC -le 4 ; then export RC=4 ; fi
fi

echo ""
echo "Checking that variables in login.defs are referred only once..."
if test $(wc -l shadow-login_defs-check-login_defs.lst | sed 's/ .*//') != $(wc -l shadow-login_defs-check-login_defs-sorted.lst | sed 's/ .*//') ; then
	echo "  ERROR: Some variable referred at more places of login.defs!"
	LC_ALL=C sort shadow-login_defs-check-login_defs.lst >shadow-login_defs-check-login_defs-sorted-nu.lst
	diff shadow-login_defs-check-login_defs-sorted-nu.lst shadow-login_defs-check-login_defs-sorted.lst
	if test $RC -le 3 ; then export RC=3 ; fi
fi

echo ""
echo "Checking that variables in lib/getdef.c are referred only once..."
if test $(wc -l shadow-login_defs-check-getdef.lst | sed 's/ .*//') != $(wc -l shadow-login_defs-check-getdef-sorted.lst | sed 's/ .*//') ; then
	echo "  ERROR: Some variable referred at more places of lib/getdef.c!"
	LC_ALL=C sort shadow-login_defs-check-getdef.lst >shadow-login_defs-check-getdef-sorted-nu.lst
	diff shadow-login_defs-check-getdef-sorted-nu.lst shadow-login_defs-check-getdef-sorted.lst
	if test $RC -le 3 ; then export RC=3 ; fi
fi

cat shadow-login_defs-check-shadow-used.lst shadow-login_defs-check-util-linux.lst shadow-login_defs-check-pam.lst | LC_ALL=C sort -u >shadow-login_defs-check-all-used.lst
# RC inside pipe cannot be read directly. Use 3 for a real stdout inside the pipe, and use stdout for RC.
exec 3>&1
function report_packages() {
	echo -n " ("
	grep -l $1 shadow-login_defs-check-{shadow-used,util-linux,pam}.lst |
		sed 's/shadow-login_defs-check-//;s/\.lst//;s/-used//;s/$/, /;$s/, $//' |
		tr -d '\n'
	echo -n ")"
}

# Extracting variables from shadow is not capable to identify compiled-but-unused library code.
# This function will identify known false matches.
function falsematch() {
	case "$1" in
# MAIL_* used by library call mailcheck() used only by login.c that is deleted in the spec.
	MAIL_* ) return 0 ;;
# FTMP_FILE used by library call failtmp() used only by login.c that is deleted in the spec.
	FTMP_FILE ) return 0 ;;
# ISSUE_FILE used by library call login_prompt() used only by login.c that is deleted in the spec.
	ISSUE_FILE ) return 0 ;;
# PREVENT_NO_AUTH us used only by login.c and su.c that are deleted in the spec.
	PREVENT_NO_AUTH ) return 0 ;;
	* ) return 1 ;;
	esac
}

echo ""
echo "Checking that all used variables are covered by login.defs..."
RC=$(cat shadow-login_defs-check-all-used.lst | (
	while read ; do
		if falsematch "$REPLY" ; then
			echo "  FALSE MATCH: Variable $REPLY is not present in login.defs$(report_packages $REPLY)" >&3
			continue
		fi
		if ! grep -q -x "$REPLY" shadow-login_defs-check-login_defs-sorted.lst ; then
			echo "  NOTICE: Variable $REPLY is not present in login.defs$(report_packages $REPLY)" >&3
			if test $RC -le 2 ; then RC=2 ; fi
		fi
	done
	echo $RC
) )

echo ""
echo "Checking that all used variables are covered by lib/getdef.c..."
RC=$(cat shadow-login_defs-check-all-used.lst | (
	while read ; do
		if falsematch "$REPLY" ; then continue ; fi
		if ! grep -q -x "$REPLY" shadow-login_defs-check-getdef.lst ; then
			echo "  ERROR: Variable $REPLY is missing in the parser$(report_packages $REPLY)" >&3
			if test $RC -le 3 ; then RC=3 ; fi
		fi
	done
	echo $RC
) )

echo ""
echo "Checking that all used variables referred in login.defs are valid..."
RC=$(cat shadow-login_defs-check-login_defs.lst | (
	while read ; do
		if ! grep -q -x "$REPLY" shadow-login_defs-check-all-used.lst ; then
			echo "  ERROR: Failed to find reference for $REPLY" >&3
			if test $RC -le 3 ; then RC=3 ; fi
		fi
		if ! grep -q -x "$REPLY" shadow-login_defs-check-getdef.lst ; then
			echo "  BUG: Parser does not contain reference for $REPLY" >&3
			if test $RC -le 4 ; then RC=4 ; fi
		fi
	done
	echo $RC
) )


echo ""
echo ""
echo "All checks finished."
echo -n "Result: "
case $RC in
0) echo "OK." ;;
1) echo "Notices only. Action is optional." ;;
2) echo "Warnings only. Evaluation is needed." ;;
3) echo "Errors found. Fix is recommended." ;;
4) echo "Fatal error. Fix has to be done." ;;
esac

if test $RC -ge 1 ; then
	exit 1
fi

echo "
If you ported shadow-util-linux.patch to the new util-linux version,
please submit these updates:
Change in util-linux.spec:"
sed -n 's/^Version:[[:space:]]*/Requires:       login_defs-support-for-util-linux >= /p' <openSUSE\:Factory/util-linux/util-linux.spec
echo "Change in shadow.spec:"
sed -n 's/^Version:[[:space:]]*/Provides:       login_defs-support-for-util-linux = /p' <openSUSE\:Factory/util-linux/util-linux.spec

echo "
If you ported shadow-login_defs-unused-by-pam.patch to the new pam version,
please submit these updates:
Change in pam.spec:"
sed -n 's/^Version:[[:space:]]*/Requires:       login_defs-support-for-pam >= /p' <openSUSE\:Factory/pam/pam.spec
echo "Change in shadow.spec:"
sed -n 's/^Version:[[:space:]]*/Provides:       login_defs-support-for-pam = /p' <openSUSE\:Factory/pam/pam.spec
