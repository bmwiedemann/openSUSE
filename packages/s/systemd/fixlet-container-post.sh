#! /bin/bash
#
# This script contains all the fixups run when systemd-container package is
# installed or updated.
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

# On systems using BTRFS, convert /var/lib/machines into a subvolume suitable
# for snapper to perform snapshots, rollbacks.. in case it was not properly set
# up, see bsc#992573. The installer has been fixed to properly initialize it at
# installation time.
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
# See bsc#992573
#
fix_machines_subvol() {
	local tagfile=/var/lib/systemd/rpm/container-machines_subvol

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
	# because an update through a chroot might be in progress (see
	# bsc#1030290).
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
if [ $1 -gt 1 ]; then
	# During upgrade
	fix_machines_subvol || {
		warn "Please fix /var/lib/machines manually."
		r=1
	}
fi

exit $r
