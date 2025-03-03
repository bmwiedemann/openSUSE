#!/bin/sh

# Support two methods of invocation:
# a) Called without arguments, use /proc/cmdline (lang= and keytable=)
# b) Called with arguments, use $1 as lang and $2 as keytable

if [ $# != 0 ]; then
	lang=$1
	keytable=$2
else
	lang=en_US
	keytable=
	for o in $(cat /proc/cmdline); do
		case $o in
		lang=*)
			lang="${o#*=}"
			;;
		keytable=*)
			keytable="${o#*=}"
			;;
		esac
	done
fi

# Avoid directory traversal through /
lang="${lang//\/}"
keytable="${keytable//\/}"

# Strip potential .UTF-8 suffix
lang="${lang%%.*}"

Country=$(echo "$lang" | cut -d_ -f2)
Language=$(echo "$lang" | cut -d_ -f1)

file="/usr/share/langset/$Language""_$Country"
if ! [ -f "$file" ]; then
	file="/usr/share/langset/$Language"
fi

if ! [ -f "$file" ]; then
	echo "Locale not found"
	exit 1
fi

# Read all values of the langset data files
. "$file"

# Apply all options
[ -z "$RC_LANG" ] || localectl set-locale LANG=$RC_LANG

# set_vconsole_option KEY value
set_vconsole_option() {
	# If the file exists, try to change the value. The sed command exits with 1 if no substitution was done.
	[ -e /etc/vconsole.conf ] && sed -i"" -E "/^$1=.*\$/,\${s//$1=$2/;b};\$q1" /etc/vconsole.conf && return
	# Otherwise, add a new assignment.
	echo "$1=$2" >> /etc/vconsole.conf
}

[ -z "$CONSOLE_FONT" ] || set_vconsole_option FONT "$CONSOLE_FONT"

# Try the lang-provided keytable first
[ -z "$KEYTABLE" ] || localectl set-keymap $KEYTABLE

[ -n "$TIMEZONE" ] && [ -f "/usr/share/zoneinfo/$TIMEZONE" ] && rm -f /etc/localtime && ln -s /usr/share/zoneinfo/$TIMEZONE /etc/localtime

# Override with the cmdline provided one, if possible
[ -z "$keytable" ] || localectl set-keymap -- "$keytable"

echo "$lang" > /var/lib/zypp/RequestedLocales
