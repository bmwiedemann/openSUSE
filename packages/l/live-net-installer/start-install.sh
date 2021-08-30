#!/bin/bash
#YaST takes a certain time to show up, so we need to prevent calling it twice simultaneously
#snippet from man 1 flock
[ "${FLOCKER}" != "$0" ] && exec env FLOCKER="$0" flock -en "$0" "$0" "$@" || :

#Look like the DVD installer everywhere (if this is unset, it looks for X atoms)
export XDG_CURRENT_DESKTOP=DOESNOTMATTER

#Don't load the KDE platform theme, to avoid messing with accelerator mnemonics (boo#1045798)
export KDE_SESSION_VERSION=0

# boo#1155687
systemctl stop nscd.service

# boo#1181606
if systemctl -q is-active packagekit.service; then
	systemctl stop packagekit.service
fi

# The URL placeholder gets filled by live-net-installer.spec
# Disable self-update, it expects inst-sys environment and doesn't work from Live CD
cat >/etc/install.inf <<EOF
ZyppRepoURL: @URL@
InstMode: net
SelfUpdate: 0
EOF

# Remove rd.live.*, root and kiwi_hybrid keys and strip everything before splash=silent
cmdline=$(sed -e 's,.*splash=silent,splash=silent,;s, rd.live\.[^ ]*,,g;s, root[^ ]*,,g;s, kiwi_hybrid=[^ ]*,,g' /proc/cmdline)
echo "Cmdline: $cmdline" >> /etc/install.inf
if [ -d /sys/firmware/efi ]; then
	echo "EFI: 1" >> /etc/install.inf
else
	echo "EFI: 0" >> /etc/install.inf
fi

# Run the installer in update mode if the argument "upgrade" is provided
for i in "$@"; do
	if [[ $i == "upgrade" ]]; then
		echo "Upgrade: 1" >> /etc/install.inf
		break
	fi
done

# gnomesu does not add sbin to $PATH, so do it manually.
export PATH=/sbin:/usr/sbin:$PATH

# YaST bind mounts /run/ all the way into the target system, which can break
# the running system through various ways. It's not (easily) possible to
# pass YaST its own /run/, so for now just protect /run/utmp. That's especially
# important because upgrades from 42.3's aaa_base delete /run/utmp, which causes
# logind to crash for some reason (boo#1187971).
mountpoint -q /run/utmp || mount --bind /run/utmp /run/utmp

# Run YaST in a separate mount namespace to avoid that it messes with the
# running system.
# Mount an empty tmpfs on top of repos.d inside. This avoids that YaST modifies
# the running system's configuration, and also avoids that preexisting repos are
# copied into the target system, causing duplicates.
unshare -m sh -c 'mount -t tmpfs tmpfs /etc/zypp/repos.d && /usr/lib/YaST2/startup/YaST2.call installation initial'

# YaST replaces this with a symlink into the destination, fix it up manually
if [ -L /var/cache/zypp ]; then
	rm /var/cache/zypp
fi
