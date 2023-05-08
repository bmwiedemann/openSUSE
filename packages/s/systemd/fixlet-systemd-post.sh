#! /bin/bash
#
# This script contains all the fixups run when systemd package is installed or
# updated.
#

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
# variables in /etc/sysconfig/language are supposed to be passed to the users'
# shell *only*. However it seems that there has been some confusion and they
# ended up configuring the system-wide locale as well.  The logic followed by
# systemd was implemented in commit 01c4b6f4f0d951d17f6873f68156ecd7763429c6,
# which was reverted. The code below follows the same logic to migrate content
# of /etc/sysconfig/language into locale.conf.
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

# Migrate old i18n settings previously configured in /etc/sysconfig to the new
# locations used by systemd (/etc/locale.conf, /etc/vconsole.conf, ...). Recent
# versions of systemd parse the new locations only.
#
# This is needed both at package updates and package installations because we
# might be upgrading from a system which was running SysV init (systemd package
# is being installed).
#
# It's run only once.
migrate_sysconfig_i18n() {
	local tagfile=/var/lib/systemd/rpm/systemd-i18n_migrated
	local -i rv=0

	if [ -e $tagfile ]; then
		return 0
	fi

	# The marker could have been incorrectly put in /usr/lib.
	mv /usr/lib/systemd/scripts/.migrate-sysconfig-i18n.sh~done $tagfile &>/dev/null
	# The tag files have been moved to /var/lib/systemd/rpm later.
	mv /var/lib/systemd/i18n-migrated $tagfile &>/dev/null

	if [ -e $tagfile ]; then
		return 0
	fi
	touch $tagfile

	migrate_locale;   rv+=$?
	migrate_keyboard; rv+=$?
	migrate_language; rv+=$?

	return $rv
}

#
# This function is supposed to be called from the %post section of the main
# package. It contains all the fixups needed when the system was running a
# version of systemd older than v210.
#
# All hacks can potentially break the admin settings since they work in /etc.
#
fix_pre_210() {
	local tagfile=/var/lib/systemd/rpm/systemd-pre_210_fixed

	if [ -e $tagfile ]; then
		return 0
	fi
	touch $tagfile

	#
	# During migration from sysvinit to systemd, we used to set the systemd
	# default target to one of the 'runlevel*.target' after reading the
	# default runlevel from /etc/inittab. We don't do that anymore because
	# in most cases using the graphical.target target, which is the default,
	# will do the right thing. Moreover the runlevel targets are considered
	# as deprecated, so we convert them into "true" systemd targets instead
	# here.
	#
	if target=$(readlink /etc/systemd/system/default.target); then
		target=$(basename $target)
		case "$target" in
		runlevel?.target)
			echo "Default target is '$target' but use of runlevels is deprecated, converting"
			systemctl --no-reload set-default $target
		esac
	fi

	#
	# Migrate any symlink which may refer to the old path (ie /lib/systemd).
	#
	for f in $(find /etc/systemd/system -type l -xtype l); do
		new_target="/usr$(readlink $f)"
		[ -f "$new_target" ] && ln -s -f "$new_target" "$f"
	done
}

r=0
fix_pre_210 || {
	r=1
}
migrate_sysconfig_i18n || {
	echo >&2 "Failed to migrate i18n settings from /etc/sysconfig, continuing..."
	r=1
}

exit $r
