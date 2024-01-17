#!/bin/bash
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.

set -e

GRUB_ONCE="/usr/sbin/grub2-once"
GRUB_ENV="/boot/grub2/grubenv"
GRUB_EDITENV="/usr/bin/grub2-editenv"
GRUB_CONF="/boot/grub2/grub.cfg"
GRUB_SETUP=
BLKID="/usr/sbin/blkid"
LSBLK="/usr/bin/lsblk"
ARCH=`uname -m`
VMLINUZ="vmlinuz"
case $ARCH in
    ppc*)   VMLINUZ="vmlinux" ;;
    s390*)  VMLINUZ="image"; GRUB_SETUP="/usr/sbin/grub2-zipl-setup" ;;
esac

error_quit()
{
	echo "$1" >&2
	exit 1
}

check-system()
{
	[ -x "${GRUB_ONCE}" ] || error_quit "ERROR: cannot find or execute ${GRUB_ONCE}"  
	[ -x "${GRUB_EDITENV}" ] || error_quit "ERROR: cannot find or execute ${GRUB_EDITENV}"
	[ -x "${BLKID}" ] || error_quit "ERROR: cannot find or execute ${BLKID}"
	[ -r "${GRUB_CONF}" ] || error_quit "ERROR: cannot find or read ${GRUB_CONF}"
}

compare-fsuuid()
{
	local uuids=($($LSBLK -n -o UUID $1 $2 2>/dev/null))
	if [ ${#uuids[@]} -eq 2 ] && [ "${uuids[0]}" = "${uuids[1]}" ]; then
		return 0
	fi
	return 1
}

#####################################################################
# gets a list of available kernels from /boot/grub2/grub.cfg
# kernels are in the array $KERNELS
get-kernels()
{
	local I DUMMY MNT ROOTDEV
	declare -i I=0

	# we need the root partition later to decide if this is the kernel to select
	while read ROOTDEV MNT DUMMY; do
	    [ "$ROOTDEV" = "rootfs" ] && continue # not what we are searching for
	    if [ "$MNT" = "/" ]; then
		break
	    fi
	done < /proc/mounts


	while read -r LINE; do
	    case $LINE in
	    menuentry\ *)
		local PATTERN="^\\s*menuentry\\s\\+\\(.\\+\\)\\s*{.*\$" 
		MENUENTRY_OPTS=`echo "$LINE" | sed -n -e "s/${PATTERN}/\\1/p"`
		MENU_ENTRIES[$I]=`eval "printf \"%s\n\" $MENUENTRY_OPTS | head -1"`
		;;
	    set\ default*)
	        local DEFAULT=${LINE#*default=}

		if echo $DEFAULT | grep -q saved_entry ; then
		    local SAVED=`$GRUB_EDITENV $GRUB_ENV list | sed -n s/^saved_entry=//p`
		    if [ -n "$SAVED" ]; then
			DEFAULT_BOOT=$($GRUB_ONCE --show-mapped "$SAVED")
		    fi
		fi

                ;;
	    linux*noresume*|module*xen*noresume*)
		echo "  Skipping ${MENU_ENTRIES[$I]}, because it has the noresume option" >&2
		;;
	    linux*root=*|module*xen*root=*)
		local ROOT
		ROOT=${LINE#*root=}
		DUMMY=($ROOT)
		ROOT=${DUMMY[0]}

		if [ x"${ROOT:0:5}" = "xUUID=" ]; then
		    UUID=${ROOT#UUID=}
		    if [ -n "$UUID" ]; then
			ROOT=$($BLKID -U $UUID || true)
			if [ -z "$ROOT" ]; then
			    echo "  Skipping ${MENU_ENTRIES[$I]}, because its root device $UUID is not found" >&2
			    continue
			fi
		    fi
		fi

		if [ "$(stat -Lc '%t:%T' $ROOT || true)" != "$(stat -Lc '%t:%T' $ROOTDEV || true)" ]; then
			if compare-fsuuid "$ROOT" "$ROOTDEV" ; then
				echo "  $ROOTDEV and $ROOT have the same filesystem UUID"
			else
				echo "  Skipping ${MENU_ENTRIES[$I]}, because its root= parameter ($ROOT)" >&2
				echo "    does not match the current root device ($ROOTDEV)." >&2
				continue
			fi
		fi

		DUMMY=($LINE) # kernel (hd0,1)/boot/vmlinuz-ABC root=/dev/hda2
		KERNELS[$I]=${DUMMY[1]##*/} # vmlinuz-ABC
		# DEBUG "Found kernel entry #${I}: '${DUMMY[1]##*/}'" INFO
		let ++I
		;;
	    linux*|module*xen*)
		# a kernel without "root="? We better skip that one...
		echo "  Skipping ${MENU_ENTRIES[$I]}, because it has no root= option" >&2
		;;
	    *)  ;;
	    esac
	done < "$GRUB_CONF"
}

#############################################################
# restore grub default after (eventually failed) resume
grub-once-restore()
{
	echo "INFO: Running grub-once-restore .."
	check-system
	$GRUB_EDITENV $GRUB_ENV unset next_entry
	echo "INFO: Done."
}

#############################################################################
# try to find a kernel image that matches the actually running kernel.
# We need this, if more than one kernel is installed. This works reasonably
# well with grub, if all kernels are named "vmlinuz-`uname -r`" and are
# located in /boot. If they are not, good luck ;-)
# for 2021-style usrmerged kernels, the location in /usr/lib/modules/ \
# `uname -r`/vmlinuz is resolved to match...
find-kernel-entry()
{
	NEXT_BOOT=""
	declare -i I=0
	# DEBUG "running kernel: $RUNNING" DIAG
	while [ -n "${KERNELS[$I]}" ]; do
		BOOTING="${KERNELS[$I]}"
		if IMAGE=$(readlink /boot/"$BOOTING"); then
			if [[ $IMAGE == */vmlinuz ]]; then # new usrmerged setup
				BOOTING=${IMAGE%/vmlinuz}  # the directory name is what counts
				BOOTING=${BOOTING##*/}
			elif [ -e "/boot/${IMAGE##*/}" ]; then
				# DEBUG "Found kernel symlink $BOOTING => $IMAGE" INFO
				BOOTING=$IMAGE
			fi
		fi
		BOOTING="${BOOTING#*${VMLINUZ}-}"
		if [ "$RUNNING" == "$BOOTING" -a -n "${MENU_ENTRIES[$I]}" ]; then
			NEXT_BOOT="${MENU_ENTRIES[$I]}"
			echo "  running kernel is grub menu entry $NEXT_BOOT (${KERNELS[$I]})"
			break
		fi
		let ++I
	done
	# if we have not found a kernel, issue a warning.
	# if we have found a kernel, we'll do "grub-once" later, after
	# prepare_suspend finished.
	if [ -z "$NEXT_BOOT" ]; then
		echo "WARNING: no kernelfile matching the running kernel found"
	fi
}

#############################################################################
# if we did not find a kernel (or BOOT_LOADER is not GRUB) check,
# if the running kernel is still the one that will (probably) be booted for
# resume (default entry in menu.lst or, if there is none, the kernel file
# /boot/${VMLINUZ} points to.)
# This will only work, if you use "original" SUSE kernels.
# you can always override with the config variable set to "yes"
prepare-grub()
{
	echo "INFO: Running prepare-grub .."
	check-system
	get-kernels
	RUNNING=`uname -r`
	find-kernel-entry

	if [ -z "$NEXT_BOOT" ]; then
		# which kernel is booted with the default entry?
		BOOTING="${KERNELS[$DEFAULT_BOOT]}"
		# if there is no default entry (no menu.lst?) we fall back to
		# the default of /boot/${VMLINUZ}.
		[ -z "$BOOTING" ] && BOOTING="${VMLINUZ}"
		if IMAGE=$(readlink /boot/"$BOOTING"); then
			if [[ $IMAGE == */vmlinuz ]]; then # new usrmerged setup
				BOOTING=${IMAGE%/vmlinuz}  # the directory name is what counts
				BOOTING=${BOOTING##*/}
			elif [ -e "/boot/${IMAGE##*/}" ]; then
				BOOTING=$IMAGE
			fi
		fi
		BOOTING="${BOOTING#*${VMLINUZ}-}"
		echo  "running kernel: '$RUNNING', probably booting kernel: '$BOOTING'"
		check-setup "$RUNNING"
		if [ "$BOOTING" != "$RUNNING" ]; then
			error_quit "ERROR: kernel version mismatch, cannot suspend to disk"
		fi
	else
		# set the bootloader to the running kernel
		echo "  preparing boot-loader: selecting entry $NEXT_BOOT, kernel /boot/$BOOTING"
		T1=`date +"%s%N"`
		sync; sync; sync # this is needed to speed up grub-once on reiserfs
		T2=`date +"%s%N"`
		check-setup "$RUNNING"
		echo "  running $GRUB_ONCE \"${NEXT_BOOT}\""
		${GRUB_ONCE} "$NEXT_BOOT"
		T3=`date +"%s%N"`
		S=$(((T2-T1)/100000000)); S="$((S/10)).${S:0-1}"
		G=$(((T3-T2)/100000000)); G="$((G/10)).${G:0-1}"
		echo "    time needed for sync: $S seconds, time needed for grub: $G seconds."
	fi

	echo "INFO: Done."
}

#############################################################################
check-setup()
{
	local WANT="$VMLINUZ-$1"

	[ -n "$GRUB_SETUP" ] || return 0
	# implementation below is s390x-only (for now)
	echo "INFO: check-setup \"$WANT\" .."
	HAVE="/boot/zipl/$VMLINUZ"
	[ -r "$HAVE" ] ||
		error_quit "ERROR: no zipl kernel, cannot suspend to disk"
	HAVE=$(readlink $HAVE) ||
		error_quit "ERROR: zipl kernel no sym-link, cannot suspend to disk"
	[ "$HAVE" != "$WANT" ] ||
		{ echo "  zipl kernel already in sync, nothing to do"; return; }
	echo "  running $GRUB_SETUP # (incl. dracut!)"  # no --image as running is preferred!
	${GRUB_SETUP} > /dev/null 2>&1
}

###### main()

eval `grep LOADER_TYPE= /etc/sysconfig/bootloader`

if [ x"$LOADER_TYPE" != "xgrub2" -a x"$LOADER_TYPE" != "xgrub2-efi" ]; then
	echo "INFO: Skip running $0 for bootloader: $LOADER_TYPE"
	exit 0
fi

if [ "$2" = suspend ]; then
	echo "INFO: Skip running $0 for $2"
	exit 0
else
	echo "INFO: running $0 for $2"
fi

if [ "$1" = pre ] ; then
	prepare-grub
fi
if [ "$1" = post ] ; then
	grub-once-restore
fi
