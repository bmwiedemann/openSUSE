#!/bin/bash
#YaST takes a certain time to show up, so we need to prevent calling it twice simultaneously
#snippet from man 1 flock
[ "${FLOCKER}" != "$0" ] && exec env FLOCKER="$0" flock -en "$0" "$0" "$@" || :

#Look like the DVD installer everywhere (if this is unset, it looks for X atoms)
export XDG_CURRENT_DESKTOP=DOESNOTMATTER

#Don't load the KDE platform theme, to avoid messing with accelerator mnemonics (boo#1045798)
export KDE_SESSION_VERSION=0

#The URL placeholder gets filled by live-net-installer.spec
cat >/etc/install.inf <<EOF
ZyppRepoURL: @URL@
InstMode: net
# disable self-update, it expects inst-sys environment and doesn't work from Live CD
SelfUpdate: 0
EOF

# Remove rd.live.*, root and kiwi_hybrid keys and strip everything before splash=silent
cmdline=$(sed -e 's,.*splash=silent,splash=silent,;s, rd.live\.[^ ]*,,g;s, root[^ ]*,,g;s, kiwi_hybrid=[^ ]*,,g' /proc/cmdline)
echo "Cmdline: $cmdline" >> /etc/install.inf
if [ -d /sys/firmware/efi/vars ]; then
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

/usr/lib/YaST2/startup/YaST2.call installation initial
