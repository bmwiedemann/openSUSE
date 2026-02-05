#! /bin/bash
#
# This script contains all the fixups run when systemd package is installed or
# updated.
#

warn() {
	echo >&2 "warning: $@"
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

check_config_files
