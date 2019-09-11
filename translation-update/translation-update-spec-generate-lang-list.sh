#!/bin/bash
# Generate lang list for spec file.
# Usage:
# 1. sh ./translation-update-spec-reset-lang-list.sh
# 2. osc build # it will fail
# 3. sh ./translation-update-spec-generate-lang-list.sh

LNG_LIST=$(osc lbl | sed -n '/Installed (but unpackaged) file(s) found:/,$s:.*  */usr/share/locale-langpack/\(.*\)/LC_MESSAGES/.*:\1:p' | sort -u)
BUILDROOT=$(osc lbl | sed -n 's/.*Using BUILD_ROOT=//p;s:.*/usr/bin/mkdir -p \([^ ]*/BUILDROOT\)$:\1:p' | tr -d '\n')

LNG_COUNT=0
for LNG in $LNG_LIST ; do
	LNG_NAME=
	# Handle special cases manually:
	case $LNG in
	zh_CN )
		LNG_NAME="Simplified Chinese"
		;;
	zh_TW )
		LNG_NAME="Traditional Chinese"
		;;
	esac

	if test -n "$LNG_NAME" ; then
		LNG_NAMES[LNG_COUNT++]=$LNG_NAME
		continue
	fi

	# Guess language name from Language-Team catalog file keyword
	for FILE in $BUILDROOT/translation-update*/usr/share/locale-langpack/$LNG/LC_MESSAGES/*.mo ; do
		LNG_POEDIT_NAME=$(msgunfmt $FILE 2>/dev/null | sed -n 's/^"X-Poedit-Language:  *\([^<\]*\) *.*"$/\1/p')
		LNG_NAME=$(msgunfmt $FILE 2>/dev/null | sed -n 's/^"Language-Team:  *\([^<\]*\) *.*"$/\1/p')
		LNG_NAME=${LNG_NAME%% }
		LNG_NAME=${LNG_NAME% (http*}
		LNG_NAME=${LNG_NAME% Team}
		LNG_NAME=${LNG_NAME% Translation}
		LNG_NAME=${LNG_NAME% Translation Project}
		LNG_NAME=${LNG_NAME#GNOME }
		LNG_NAME=${LNG_NAME#Gnome }
		LNG_NAME=${LNG_NAME% GNOME}
		LNG_NAME=${LNG_NAME% Gnome}
		# for ug:
		LNG_NAME=${LNG_NAME% Computer Science Association}
		# for ml:
		LNG_NAME=${LNG_NAME#Swathanthra }
		LNG_NAME=${LNG_NAME% Computing}
		LNG_NAME=${LNG_NAME%, Modern*}

		# X-Poedit-Language should be correct without hacks. Prefer it, if exists.
		if test -n "$LNG_POEDIT_NAME" ; then
			LNG_NAME="$LNG_POEDIT_NAME"
			break
		fi

		# Do not accept the default value "American English" for anything else than en_US.
		if test "$LNG_NAME" = "American English" -a "$LNG" != en_US ; then
			continue
		fi
		# Do not accept national names. We search for English name.
		if ! echo "$LNG_NAME" | iconv -f UTF-8 -t ASCII >/dev/null 2>&1 ; then
			continue
		fi
		# Errorneous cases.
		case "$LNG_NAME" in
		# nb
		# Do not accept company or tool name.
		# Do not accept underbar. It means that translator filled LANG variable name.
		# Do not accept e-mails.
		"Kjartan Maraas" | "Novell Language" | "AgreeYa Solutions" | linux* | *_* | *@* | */* )
			continue
			;;
		esac
		if test -n "$LNG_NAME" ; then
			break
		fi
	done

	LNG_NAMES[LNG_COUNT++]=$LNG_NAME
done

echo
echo "Please review following language names and fix them, if needed:"
LNG_COUNT=0
for LNG in $LNG_LIST ; do
	echo "$LNG: ${LNG_NAMES[LNG_COUNT++]}"
done

LNG_COUNT=0
for LNG in $LNG_LIST ; do
LNG_PKG=${LNG//@/-}
cat <<EOF
%package -n translation-update-$LNG_PKG
Summary:        Translation Updates for ${LNG_NAMES[LNG_COUNT]}
Group:          System/Localization
Provides:       locale(translation-update:$LNG)
Requires:       translation-update

%description -n translation-update-$LNG_PKG
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

EOF
let LNG_COUNT++
done >translation-update.spec.preamble.tmp

for LNG in $LNG_LIST ; do
LNG_PKG=${LNG//@/-}
cat <<EOF
%files -n translation-update-$LNG_PKG
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang($LNG) %{_datadir}/locale-langpack/$LNG
%doc COPYING

EOF
done >translation-update.spec.files.tmp

sed -i '
/^%prep$/{
r translation-update.spec.preamble.tmp
a %prep
/^%prep$/d
}
/^%changelog$/{
r translation-update.spec.files.tmp
a %changelog
/^%changelog$/d
}
' translation-update.spec
rm translation-update.spec.preamble.tmp translation-update.spec.files.tmp

grep %package *.spec | sed 's/%package -n //' | LANG=C sort -u >pkglist-post.lst

echo "Please add this to translation-update.spec with comments of version."

diff pkglist-pre.lst pkglist-post.lst | sed -n 's/< /Obsoletes:      /p'
