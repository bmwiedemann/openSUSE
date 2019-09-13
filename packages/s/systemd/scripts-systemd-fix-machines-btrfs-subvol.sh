#! /bin/bash
#
# This is used to initially create /var/lib/machines subvolume in case
# the system we're running on is using BTRFS with the specific layout
# used by snapper to perform snapshots, rollbacks, etc...
#
# Unfortunately some distros (TW) already shipped versions with
# systemd creating a plain subvolume which breaks snapper.
#
# If /var/lib/machines is already populated then it's going to be
# pretty ugly to convert the old subvolume into a new one specially
# since it can be in use.
#
# Hopefully not a lot of users are using machinectl to import
# container/VM images. So in most of the cases this directory should
# be empty and we can then simple delete the subvolume and create a
# new one respecting the snapper layout.
#
# In the rare case where /var/lib/machines is populated, we will warn
# the user and let him fix it manually.
#
# In order to avoid ugly dependencies added in systemd package, this
# script should only be called during package updates when
# mksubvolume(8) is available. During installation, /var/lib/machines
# is supposed to be created by the installer now.
#
# See bsc#992573
#

warn() {
	echo >&2 "warning: $@"
}

is_btrfs_subvolume() {
	# On btrfs subvolumes always have the inode 256
	test $(stat --format=%i "$1") -eq 256
}

# This assumes the directory/subvol is emptied by the caller.
rm_subvolume_or_directory() {
	is_btrfs_subvolume "$1" && {
		btrfs subvolume delete "$1"
		return
	}
	rmdir "$1"
}

on_exit() {
	# Simply print a common error message in case something went
	# wrong.
	if test $? -ne 0; then
		warn "Please fix /var/lib/machines manually."
		# FIXME: point to a documentation explaining how to do
		# that.
		exit 1
	fi
}

#
# If there's already an entry in fstab for /var/lib/machines, it
# means that:
#
#   - the installer initialized /var/lib/machines correctly (default)
#   - we already fixed it
#   - the sysadmin added it manually
#
# In any cases we should exit.
#
# Note: we can't simply check if /var/lib/machines has been mounted
# because an update through a chroot might be in progress (see
# bsc#1030290).
#
if mount --fake /var/lib/machines 2>/dev/null; then
	exit
fi

#
# If there is already an entry in fstab for /var, it means that:
#
#   - the system has a seperate /var subvolume (default from Feb 2018)
#   - the system has a seperate /var partition
#
# In any case we should exit
#
if mount --fake /var 2>/dev/null; then
	exit
fi

#
# If something is already mounted don't try to fix anything, it's been
# done manually by the sysadmin.
#
if mountpoint -q /var/lib/machines; then
	exit
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
	exit 0
esac

trap on_exit EXIT

if test -d /var/lib/machines; then
	#
	# Ok, we're on a system supporting rollbacks and
	# /var/lib/machines is not a subvolume remotely mounted so it
	# cannot be suitable for systems supporting rollback. Fix it.
	#
	echo "Making /var/lib/machines suitable for rollbacks..."

	type mksubvolume >/dev/null 2>&1 || {
		warn "mksubvolume(8) is not installed, aborting."
		exit 1
	}
	test "$(ls -A /var/lib/machines/)" && {
		warn "/var/lib/machines is not empty, aborting."
		exit 1
	}

	echo "Deleting empty /var/lib/machines directory/subvolume"
	rm_subvolume_or_directory /var/lib/machines || {
		warn "fail to delete /var/lib/machines"
		exit 1
	}
fi

# At this point /var/lib/machines shouldn't exist.
echo "Creating /var/lib/machines subvolume suitable for rollbacks."
mksubvolume /var/lib/machines
