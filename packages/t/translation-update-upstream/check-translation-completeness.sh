#!/bin/bash

set -o errexit
# We need stable text format
export LANG=C

if ! test -d po-full ; then
	echo >&2 "$0: You need \"po-full\" directory. Call this script only after ./upstream-collect.sh"
	exit 1
fi

cd po-full
ALL_LNG="$(
	for PO in */*.po ; do
		LNG=${PO%.po}
		LNG=${LNG##*/}
		echo "$LNG"
	done |
	sort -u |
	tr '\n' ' '
)"
#echo >&2 "$0 DBG: ALL_LNG=\"$ALL_LNG\""

for DOMAIN in * ; do
	for LNG in $ALL_LNG ; do
		# Sanitize to not contain "," or ".":
		LNG_SN=${LNG//,/__COMMA__}
		LNG_SN=${LNG_SN//./__PERIOD__}
		DOMAIN_SN=${DOMAIN//,/__COMMA__}
		DOMAIN_SN=${DOMAIN_SN//./__PERIOD__}
		echo -n "$LNG_SN,$DOMAIN_SN,"
		PO=$DOMAIN/$LNG.po
		if test -f "$PO" ; then
			msgfmt --statistics -o /dev/null $PO 2>&1
		else
			msgfmt --statistics -o /dev/null ../pot/$DOMAIN.pot 2>&1
		fi
	done
done |
#tee ../check-translation-completeness-DBG1.log |
(
# "F1 translated messages, F2 fuzzy translations, F3 untranslated messages." Some fields can be missing
	IFS=,.
	while read LNG DOMAIN F1 F2 F3 F4 ; do
		LNG=${LNG//__COMMA__/,}
		LNG=${LNG//__PERIOD__/.}
		DOMAIN=${DOMAIN//__COMMA__/,}
		DOMAIN=${DOMAIN//__PERIOD__/.}
		TRANSLATED=0
		UNTRANSLATED=0
		FUZZY=0
		if test -n "$F4" ; then
			echo >&2 "$0: Too long output of \"msgfmt --statistics -o /dev/null po-full/$DOMAIN/$LNG.po\": \"$F4\""
			exit 1
		fi
		for STRING in "$F1" "$F2" "$F3" "$F4" ; do
			STRING=${STRING# }
			case "$STRING" in
			*" translated message" )
				TRANSLATED=${STRING% translated message}
				;;
			*" translated messages" )
				TRANSLATED=${STRING% translated messages}
				;;
			*" fuzzy translation" )
				FUZZY=${STRING% fuzzy translation}
				;;
			*" fuzzy translations" )
				FUZZY=${STRING% fuzzy translations}
				;;
			*" untranslated message" )
				UNTRANSLATED=${STRING% untranslated message}
				;;
			*" untranslated messages" )
				UNTRANSLATED=${STRING% untranslated messages}
				;;
			"" )
				;;
			* )
				echo >&2 "$0: Unknown format of \"msgfmt --statistics -o /dev/null po-full/$DOMAIN/$LNG.po\": \"$STRING\""
				exit 1
				;;
			esac
		done
		#echo >&2 -n "$0 DBG: LNG=$LNG DOMAIN=$DOMAIN F1=\"$F1\" F2=\"$F2\" F3=\"$F3\" F4=\"$F4\" TRANSLATED=$TRANSLATED UNTRANSLATED=$UNTRANSLATED FUZZY=$FUZZY"
		let UNTRANSLATED+=FUZZY || :
		let ALL=TRANSLATED+UNTRANSLATED || :
		#echo >&2 " DBG: ALL=$ALL all_UNTRANSLATED=$UNTRANSLATED"
		let PERCENTAGE=100"*"TRANSLATED/ALL || :
		echo "\"$LNG\",\"$DOMAIN\",$PERCENTAGE,$UNTRANSLATED,$ALL"
	done
) |
#tee ../check-translation-completeness-DBG2.log |
(
	echo >../check-translation-completeness-by-domain.csv "\"Language\",\"Domain\",\"Translated %\",\"Untranslated #\",\"All #\""
	tee -a ../check-translation-completeness-by-domain.csv
) |
sort |
(
	echo >../check-translation-completeness-by-language.csv "\"Language\",\"Domain\",\"Translated %\",\"Untranslated #\",\"All #\""
	tee -a ../check-translation-completeness-by-language.csv
) |
(
	IFS=","
	while read LNG DOMAIN PERCENTAGE UNTRANSLATED ALL ; do
		LNG=${LNG//\"}
		case $LNG in
		ar )
			LNG_NAME="Arabic"
			;;
		pt_BR )
			LNG_NAME="Brazilian Portuguese"
			;;
		zh_CN )
			LNG_NAME="Chinese Simplified"
			;;
		zh_TW )
			LNG_NAME="Chinese Traditional"
			;;
		cs )
			LNG_NAME="Czech"
			;;
		nl )
			LNG_NAME="Dutch"
			;;
		fr )
			LNG_NAME="French"
			;;
		de )
			LNG_NAME="German"
			;;
		hu )
			LNG_NAME="Hungarian"
			;;
		it )
			LNG_NAME="Italian"
			;;
		ja )
			LNG_NAME="Japanese"
			;;
		ko )
			LNG_NAME="Korean"
			;;
		pl )
			LNG_NAME="Polish"
			;;
		ru )
			LNG_NAME="Russian"
			;;
		es )
			LNG_NAME="Spanish"
			;;
		sv )
			LNG_NAME="Swedish"
			;;
		* )
			continue
			;;
		esac
		echo "\"$LNG_NAME\",$DOMAIN,$PERCENTAGE,$UNTRANSLATED,$ALL"
	done
) |
sort |
(
	echo >../check-translation-completeness-supported.csv "\"Language\",\"Domain\",\"Translated %\",\"Untranslated #\",\"All #\""
	cat >../check-translation-completeness-supported.csv
)

cd ..
zip check-translation-completeness.zip check-translation-completeness*.csv
