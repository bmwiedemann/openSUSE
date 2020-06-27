#! /bin/bash

# /etc/sysconfig/console   | /etc/vconsole.conf
# -------------------------+---------------------
# CONSOLE_FONT             | FONT
# CONSOLE_SCREENMAP        | FONT_MAP
# CONSOLE_UNICODEMAP       | FONT_UNIMAP
migrate_locale () {
	local migrated=""

	if ! test -f /etc/sysconfig/console; then
		return
	fi
	source /etc/sysconfig/console || return

	if test -f /etc/vconsole.conf; then
		source /etc/vconsole.conf || return
	fi

	if test -n "$CONSOLE_FONT" && test -z "$FONT"; then
		echo "FONT=$CONSOLE_FONT" >>/etc/vconsole.conf
		migrated+="CONSOLE_FONT "
	fi
	if test -n "$CONSOLE_SCREENMAP" && test -z "$FONT_MAP"; then
		echo "FONT_MAP=$CONSOLE_SCREENMAP" >>/etc/vconsole.conf
		migrated+="CONSOLE_SCREENMAP "
	fi
	if test -n "$CONSOLE_UNICODEMAP" && test -z "$FONT_UNIMAP"; then
		echo "FONT_UNIMAP=$CONSOLE_UNICODEMAP" >>/etc/vconsole.conf
		migrated+="CONSOLE_UNICODEMAP "
	fi

	if test -n "$migrated"; then
		echo >&2 "The following variables from /etc/sysconfig/console have been migrated"
		echo >&2 "into /etc/vconsole.conf:"
		echo >&2
		for v in $migrated; do echo "  - $v=${!v}"; done
		echo >&2
		echo >&2 "Please edit /etc/vconsole.conf if you need to tune these settings"
		echo >&2 "as /etc/sysconfig/console won't be considered anymore."
		echo >&2
	fi
}

# /etc/sysconfig/keyboard  | /etc/vconsole.conf
# -------------------------+---------------------
# KEYTABLE                 | KEYMAP
migrate_keyboard () {
	local migrated=""

	if ! test -f /etc/sysconfig/keyboard; then
		return
	fi
	source /etc/sysconfig/keyboard || return

	if test -f /etc/vconsole.conf; then
		source /etc/vconsole.conf || return
	fi

	if test -n "$KEYTABLE" && test -z "$KEYMAP"; then
		echo "KEYMAP=$KEYTABLE" >>/etc/vconsole.conf
		migrated+="KEYTABLE "
	fi

	if test -n "$migrated"; then
		echo >&2 "The following variables from /etc/sysconfig/keyboard have been migrated"
		echo >&2 "into /etc/vconsole.conf:"
		echo >&2
		for v in $migrated; do echo "  - $v=${!v}"; done
		echo >&2
		echo >&2 "Please use localectl(1) if you need to tune these settings since"
		echo >&2 "/etc/sysconfig/keyboard won't be considered anymore."
		echo >&2
	fi
}

# According to
# https://www.suse.com/documentation/sles-12/book_sle_admin/data/sec_suse_l10n.html,
# variables in /etc/sysconfig/language are supposed to be passed to
# the users' shell *only*. However it seems that there has been some
# confusion and they ended up configuring the system-wide locale as
# well.  The logic followed by systemd was implemented in commit
# 01c4b6f4f0d951d17f6873f68156ecd7763429c6, which was reverted. The
# code below follows the same logic to migrate content of
# /etc/sysconfig/language into locale.conf.
migrate_language () {
	local lang=
	local migrated=false

	if ! test -f /etc/sysconfig/language; then
		return
	fi
	source /etc/sysconfig/language || return

	lang=$(grep ^LANG= /etc/locale.conf 2>/dev/null)
	lang=${lang#LANG=}

	case "$ROOT_USES_LANG" in
        yes)
		if test -z "$lang" && test -n "$RC_LANG"; then
			echo "LANG=$RC_LANG" >>/etc/locale.conf
			migrated=true
		fi
		;;
	ctype)
		if ! grep -q ^LC_CTYPE= /etc/locale.conf 2>/dev/null; then

			: ${lc_ctype:="$lang"}
			: ${lc_ctype:="$RC_LC_CTYPE"}
			: ${lc_ctype:="$RC_LANG"}

			if test -n "$lc_ctype"; then
				echo "LC_CTYPE=$lc_ctype" >>/etc/locale.conf
				migrated=true
			fi
		fi
		;;
	esac

	if $migrated; then
		echo >&2 "The content of /etc/sysconfig/language has been migrated into"
		echo >&2 "/etc/locale.conf. The former file is now only used for setting"
		echo >&2 "the locale used by user's shells. The system-wide locale is"
		echo >&2 "only read from /etc/locale.conf since now."
		echo >&2
		echo >&2 "Please only use localectl(1) or YaST if you need to change the"
		echo >&2 "settings of the *system-wide* locale from now."
	fi
}


# The marker could have been incorrectly put in /usr/lib. In this case
# move it to its new place.
mv /usr/lib/systemd/scripts/.migrate-sysconfig-i18n.sh~done \
   /var/lib/systemd/i18n-migrated &>/dev/null

if ! test -e /var/lib/systemd/i18n-migrated; then
	declare -i rv=0

	migrate_locale;   rv+=$?
	migrate_keyboard; rv+=$?
	migrate_language; rv+=$?

	test $rv -eq 0 && touch /var/lib/systemd/i18n-migrated
fi
