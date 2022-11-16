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
if ! test -f "$file"; then
  file="/usr/share/langset/$Language"
fi

# Read all values of the langset data files
. "$file"

# Chop the extension off
KEYTABLE="${KEYTABLE%%.map*}"

# Apply all options
[ -n "$RC_LC_MESSAGES" ] || RC_LC_MESSAGES=$RC_LANG
[ -z "$RC_LANG" ] || localectl set-locale LANG=$RC_LANG LC_MESSAGES=$RC_LC_MESSAGES

# set_vconsole_option KEY value
set_vconsole_option() {
	# This sed command exits with 1 if no substitution was done
	sed -i"" -E "/^$1=.*\$/,\${s//$1=$2/;b};\$q1" /etc/vconsole.conf && return
	echo "$1=$2" >> /etc/vconsole.conf
}

[ -z "$CONSOLE_FONT" ] || set_vconsole_option FONT "$CONSOLE_FONT"
[ -z "$CONSOLE_SCREENMAP" ] || set_vconsole_option FONT_MAP "$CONSOLE_SCREENMAP"
[ -z "$CONSOLE_UNICODEMAP" ] || set_vconsole_option FONT_UNIMAP "$CONSOLE_UNICODEMAP"

# set_sysconfig_option KEY value
set_sysconfig_option() {
	sed -i -e "s#$1=\".*#$1=\"$2\"#" /etc/sysconfig/keyboard
	sed -i -e "s#$1=\".*#$1=\"$2\"#" /etc/sysconfig/console
}

# Set legacy sysconfig values for backwards-compat
[ -z "$CONSOLE_FONT" ] || set_sysconfig_option CONSOLE_FONT "$CONSOLE_FONT"
[ -z "$CONSOLE_SCREENMAP" ] || set_sysconfig_option CONSOLE_SCREENMAP "$CONSOLE_SCREENMAP"
[ -z "$CONSOLE_UNICODEMAP" ] || set_sysconfig_option CONSOLE_UNICODEMAP "$CONSOLE_UNICODEMAP"

[ -z "$KEYTABLE" ] || set_sysconfig_option KEYTABLE "$KEYTABLE"
[ -z "$COMPOSETABLE" ] || set_sysconfig_option COMPOSETABLE "$COMPOSETABLE"

# Try the lang-provided keytable first
[ -z "$KEYTABLE" ] || localectl set-keymap $KEYTABLE

[ -n "$TIMEZONE" ] && [ -f "/usr/share/zoneinfo/$TIMEZONE" ] && rm -f /etc/localtime && ln -s /usr/share/zoneinfo/$TIMEZONE /etc/localtime

# Override with the cmdline provided one, if possible
[ -z "$keytable" ] || localectl set-keymap -- "$keytable"

echo "$lang" > /var/lib/zypp/RequestedLocales
