#!/bin/bash

set -euo pipefail

function cleanup {
    pushd "${OTHER_MACHINE_DIR}"
    vagrant destroy -f
    popd

    fusermount -uz /tmp/reverse_mount_etc || true

    vagrant destroy -f

    rmdir /tmp/reverse_mount_etc
    rm -rf .vagrant "${OTHER_MACHINE_DIR}"
}

trap cleanup EXIT

mkdir -p /tmp/reverse_mount_etc

mkdir other_machine && pushd other_machine
vagrant init opensuse/openSUSE-Tumbleweed-Vagrant.x86_64
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
SLAVE_FORWARD_SYMLINK_MACHINE_ID=$(vagrant ssh -- cat /usr/sbin/forward_slave_mount_sym_link_test/machine-id)

FORWARD_MACHINE_ID=$(vagrant ssh -- cat /tmp/forward_normal_mount_etc/machine-id)

REVERSE_MACHINE_ID=$(cat /tmp/reverse_mount_etc/machine-id)

vagrant destroy -f

pushd other_machine
vagrant destroy -f
popd

if [[ ("${SLAVE_FORWARD_MACHINE_ID}" != "$(cat /etc/machine-id)") || ("${SLAVE_FORWARD_SYMLINK_MACHINE_ID}" != $(cat /etc/machine-id)) || ("${FORWARD_MACHINE_ID}" != "${OTHER_MACHINE_ID}") || ("${REVERSE_MACHINE_ID}" != "${SLAVE_MACHINE_ID}") ]]; then
    echo "mismatch in machine IDs"
    exit 1
fi
