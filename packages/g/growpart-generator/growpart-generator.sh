#!/bin/sh
set -euo pipefail

UNIT_DIR="${1:-/tmp}"

# For the heredoc below bash needs to create a file in $TMPDIR.
# /tmp might not be mounted this early, but /run is.
TMPDIR=/run

for mnt in $(findmnt --fstab --options x-growpart.grow --output TARGET --noheadings); do
	dev="$(findmnt --fstab --target ${mnt} --evaluate --real --output SOURCE --noheadings)"
	mnt_esc="$(systemd-escape --path "${mnt}")"
	dev_esc="$(systemd-escape --path "${dev}")"

	# /dev/sda3 -> /dev/sda, /dev/nvme0n1p3 -> /dev/nvme0n1
	parent_dev="/dev/$(lsblk --nodeps -rno PKNAME "${dev}")"
	# Last number in the device name: /dev/nvme0n1p42 -> 42
	partnum="$(echo "${dev}" | sed 's/^.*[^0-9]\([0-9]\+\)$/\1/')"

	# systemd uses a different unit name for growfs for /...
	if [ "$mnt" = "/" ]; then
		growfs_unit="systemd-growfs-root.service"
	else
		growfs_unit="systemd-growfs@${mnt_esc}.service"
	fi

	mkdir -p "${UNIT_DIR}/${mnt_esc}.mount.wants"
	cat > "${UNIT_DIR}/growpart@${dev_esc}.service" <<EOF
[Unit]
Description=Grow Partition Size of ${dev} 
DefaultDependencies=no
BindsTo=${mnt_esc}.mount
Conflicts=shutdown.target
After=${mnt_esc}.mount
Before=shutdown.target local-fs.target

# Resize the partition before (possibly) resizing the file system
Before=${growfs_unit}

# growpart requires /tmp to operate
Requires=tmp.mount
After=tmp.mount

[Service]
Type=oneshot
RemainAfterExit=yes
# Exit code 1 means "NOCHANGE"
SuccessExitStatus=1
ExecStart=/usr/sbin/growpart ${parent_dev} ${partnum}
TimeoutSec=0
EOF
	ln -sf "${UNIT_DIR}/growpart@${dev_esc}.service" "${UNIT_DIR}/${mnt_esc}.mount.wants/"
done
