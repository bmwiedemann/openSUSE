#! /bin/bash
#
# This script contains all the fixups run when systemd package is installed or
# updated.
#

warn() {
	echo >&2 "warning: $@"
}

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

#
# Migrate old i18n settings previously configured in /etc/sysconfig to the new
# locations used by systemd (/etc/locale.conf, /etc/vconsole.conf, ...). Recent
# versions of systemd parse the new locations only.
#
# This is needed both at package updates and package installations because we
# might be upgrading from a system which was running SysV init (systemd package
# is being installed).
#
# Note: run only once.
#
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

	if [ $rv -gt 0 ]; then
		echo >&2 "Failed to migrate i18n settings from /etc/sysconfig, ignoring."
	fi

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

#
# /etc/machine-id might have been created writeable incorrectly (boo#1092269).
#
# Note: run at each package update.
#
fix_machine_id_perms() {
	if [ "$(stat -c%a /etc/machine-id)" != 444 ]; then
		echo "Incorrect file mode bits for /etc/machine-id which should be 0444, fixing..."
		chmod 444 /etc/machine-id
	fi
}

#
# v228 wrongly set world writable suid root permissions on timestamp files used
# by permanent timers. Fix the timestamps that might have been created by the
# affected versions of systemd (bsc#1020601).
#
# Note: run at each package update.
#
fix_bsc_1020601() {
	for stamp in $(ls /var/lib/systemd/timers/stamp-*.timer 2>/dev/null); do
		chmod 0644 $stamp
	done

	# Same for user lingering created by logind.
	for username in $(ls /var/lib/systemd/linger/* 2>/dev/null); do
		chmod 0644 $username
	done
}

#
# Due to the fact that DynamicUser= was turned ON during v235 and then switched
# back to off in v240, /var/lib/systemd/timesync might be a symlink pointing to
# /var/lib/private/systemd/timesync, which is inaccessible for systemd-timesync
# user as /var/lib/private is 0700 root:root, see
# https://github.com/systemd/systemd/issues/11329 for details.
#
# Note: only TW might be affected by this bug.
# Note: run at each package update.
#
fix_issue_11329() {
	if [ -L /var/lib/systemd/timesync ]; then
		rm /var/lib/systemd/timesync
		mv /var/lib/private/systemd/timesync /var/lib/systemd/timesync
	fi
}

#
# We don't ship after-local.service anymore however as a courtesy we install a
# copy in /etc for users who are relying on it.
#
# Note: should run only once since it is conditionalized on the presence of
# %{_unitdir}/after-local.service
#
drop_after_local_support() {
	if [ -x /etc/init.d/after.local ] &&
	   [ -f /usr/lib/systemd/system/after-local.service ]; then
		echo "after-local.service is no more provided by systemd but a copy has been installed in /etc"
		cp /usr/lib/systemd/system/after-local.service /etc/systemd/system/
		ln -s ../after-local.service /etc/systemd/system/multi-user.target.wants/after-local.service
	fi
}

#
# We have stopped shipping the main config files in /etc but we don't try to
# clean them up automatically as it can have unexepected side effects
# (bsc#1226415). Instead we simply suggest users to convert them (if they exist)
# into drop-ins.
#
# Note: run at each package update
#
check_config_files () {
	config_files=(systemd/journald.conf systemd/logind.conf systemd/system.conf systemd/user.conf
		      systemd/pstore.conf systemd/sleep.conf systemd/timesyncd.conf systemd/coredump.conf
		      systemd/journal-remote.conf systemd/journal-upload.conf systemd/networkd.conf
		      systemd/resolved.conf systemd/oomd.conf udev/iocost.conf udev/udev.conf)

	for f in ${config_files[*]}; do
		[ -e /etc/$f ] || continue

		cat >&2 <<EOF
Main configuration files are deprecated in favor of drop-ins.
Hence, we suggest that you remove /etc/$f if it doesn't contain any customization, or convert it into drop-in otherwise.
For more details, please visit https://en.opensuse.org/Systemd#Configuration.
EOF
	done
}

# On systems using the old btrfs layout, where /var was not a separate
# subvolume, convert /var/lib/machines into a subvolume suitable for snapper to
# perform snapshots, rollbacks, see bsc#992573.
#
# The conversion might only be problematic for openSUSE distros (TW/Factory)
# where the subvolume was created at the wrong place (via tmpfiles for example)
# and it got populated before we had time to fix it. In this case we'll let the
# user fix it manually.
#
# On SLE12 this subvolume was only introduced during the upgrade from v210 to
# v228 (ie SLE12-SP[01] -> SLE12-SP2+ when we added this workaround hence no
# user should had time to populate it. Note that the subvolume is still created
# at the wrong place due to the call to tmpfiles_create macro in the %post
# section however it's empty so again we shouldn't face any issue to convert it.
#
# In order to avoid ugly dependencies added in systemd package, this function
# should only be called during package updates when mksubvolume(8) is
# available. During installation, /var/lib/machines is supposed to be created by
# the installer now.
#
# See bsc#992573.
#
is_btrfs_subvolume() {
	# On btrfs subvolumes always have the inode 256
	test $(stat --format=%i "$1") -eq 256
}

# This assumes the directory/subvol to remove is empty.
rm_subvolume_or_directory() {
	is_btrfs_subvolume "$1" && {
		btrfs subvolume delete "$1"
		return
	}
	rmdir "$1"
}

fix_machines_subvol() {
	local tagfile=/var/lib/systemd/rpm/container-machines_subvol

	#
	# This test is probably redundant with the ones below but we don't want
	# to run this on transactional systems since /var has always been a
	# separate subvolume on such systems.
	#
	if [ -n "${TRANSACTIONAL_UPDATE}" ]; then
		return 0
	fi

	if [ -e $tagfile ]; then
		return 0
	fi
	touch $tagfile

	#
	# If there's already an entry in fstab for /var/lib/machines, it
	# means that:
	#
	#   - the installer initialized /var/lib/machines correctly (default)
	#   - we already fixed it
	#   - the sysadmin added it manually
	#
	# In any cases we should return.
	#
	# Note: we can't simply check if /var/lib/machines has been mounted
	# because an offline update might be in progress (see bsc#1030290).
	#
	if mount --fake /var/lib/machines 2>/dev/null; then
		return
	fi

	#
	# If there is already an entry in fstab for /var, it means that:
	#
	#   - the system has a seperate /var subvolume (default from Feb 2018)
	#   - the system has a seperate /var partition
	#
	# In any case we should return.
	#
	if mount --fake /var 2>/dev/null; then
		return
	fi

	#
	# If something is already mounted don't try to fix anything, it's been
	# done manually by the sysadmin.
	#
	if mountpoint -q /var/lib/machines; then
		return
	fi

	#
	# Let's try to figure out if the current filesystem uses a Snapper
	# BTRFS specific layout. Note that TW uses a different layout than
	# SLE...
	#
	# FIXME: not sure if it's correct, reliable or optimal.
	#
	case $(findmnt -nr -t btrfs -o FSROOT / 2>/dev/null) in
	*.snapshots/*/snapshot*)
		;;
	*)
		return 0
	esac

	if test -d /var/lib/machines; then
		#
		# Ok, we're on a system supporting rollbacks and
		# /var/lib/machines is not a subvolume remotely mounted so it
		# cannot be suitable for systems supporting rollback. Fix it.
		#
		echo "Making /var/lib/machines suitable for rollbacks..."

		type mksubvolume >/dev/null 2>&1 || {
			warn "mksubvolume(8) is not installed, aborting."
			return 1
		}
		test "$(ls -A /var/lib/machines/)" && {
			warn "/var/lib/machines is not empty, aborting."
			return 1
		}

		echo "Deleting empty /var/lib/machines directory/subvolume"
		rm_subvolume_or_directory /var/lib/machines || {
			warn "fail to delete /var/lib/machines"
			return 1
		}
	fi

	# At this point /var/lib/machines shouldn't exist.
	echo "Creating /var/lib/machines subvolume suitable for rollbacks."
	mksubvolume /var/lib/machines
}


r=0
fix_machine_id_perms || r=1
fix_pre_210 || r=1
migrate_sysconfig_i18n || r=1
fix_bsc_1020601 || r=1
fix_issue_11329 || r=1
drop_after_local_support || r=1

if [ $1 -gt 1 ]; then
	# During upgrade
	fix_machines_subvol || {
		warn "Please fix the initialization of /var/lib/machines manually."
		r=1
	}
fi

exit $r
