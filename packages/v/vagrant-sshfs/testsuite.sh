#!/bin/bash

set -euo pipefail

function cleanup {
    pushd "${OTHER_MACHINE_DIR}"
    vagrant destroy -f || true
    popd

    fusermount -uz /tmp/reverse_mount_etc_uid_gid || true

    vagrant destroy -f || true

    rmdir /tmp/reverse_mount_etc_uid_gid/
    rm -rf .vagrant "${OTHER_MACHINE_DIR}"
}

trap cleanup EXIT

mkdir /tmp/reverse_mount_etc_uid_gid 2>/dev/null
if [ $? -ne 0 ]; then
    OWNER=$(stat -c '%U' /tmp/reverse_mount_etc_uid_gid)
    if [ "$OWNER" != "$USER" ]; then
        echo "/tmp/reverse_mount_etc_uid_gid already exists and is owned by a different user. refusing to continue" 1>&2
        exit 1
    fi
fi

mkdir other_machine && pushd other_machine
vagrant init "opensuse/Tumbleweed.$(uname -m)"
vagrant up
export THIRD_PARTY_HOST=$(vagrant ssh-config|grep HostName|awk '{print $2}')
export OTHER_MACHINE_ID=$(vagrant ssh -- cat /etc/machine-id)
export OTHER_MACHINE_DIR=$(realpath .)
popd

export THIRD_PARTY_HOST_USER='vagrant'
export THIRD_PARTY_HOST_PASS='vagrant'

vagrant up

SLAVE_MACHINE_ID=$(vagrant ssh -- cat /etc/machine-id)

# extracted from dotests.sh:
SLAVE_FORWARD_MACHINE_ID=$(vagrant ssh -- cat /tmp/forward_slave_mount_etc/machine-id)
SLAVE_FORWARD_SYMLINK_MACHINE_ID=$(vagrant ssh -- cat /run/forward_slave_mount_sym_link_test/machine-id)

FORWARD_MACHINE_ID=$(vagrant ssh -- cat /tmp/forward_normal_mount_etc/machine-id)

REVERSE_MACHINE_ID=$(cat /tmp/reverse_mount_etc_uid_gid/machine-id)

vagrant destroy -f

pushd other_machine
vagrant destroy -f
popd

if [[ ("${SLAVE_FORWARD_MACHINE_ID}" != "$(cat /etc/machine-id)") || ("${SLAVE_FORWARD_SYMLINK_MACHINE_ID}" != $(cat /etc/machine-id)) || ("${FORWARD_MACHINE_ID}" != "${OTHER_MACHINE_ID}") || ("${REVERSE_MACHINE_ID}" != "${SLAVE_MACHINE_ID}") ]]; then
    echo "mismatch in machine IDs"
    exit 1
fi
