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
Before=systemd-growfs@${mnt_esc}.service

# growpart requires /tmp to operate
Requires=tmp.mount
After=tmp.mount

[Service]
Type=oneshot
RemainAfterExit=yes
# Exit code 1 means "NOCHANGE"
SuccessExitStatus=1
# Use sed to split /dev/foo42 into /dev/foo 42
ExecStart=/bin/sh -c "/usr/sbin/growpart $(echo ${dev} | sed 's/\([a-z/]*\)\(\d*\)/\1 \2/')"
TimeoutSec=0
EOF
	ln -sf "${UNIT_DIR}/growpart@${dev_esc}.service" "${UNIT_DIR}/${mnt_esc}.mount.wants/"
done
