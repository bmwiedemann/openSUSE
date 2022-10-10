#!/bin/bash -xe

#KubeVirt provides LIBGUESTFS_PATH via the pod environemnt.
LIBGUESTFS_PATH=${LIBGUESTFS_PATH:-/tmp/guestfs}
LIBGUESTFS_APPLIANCE=/appliance.tar.xz

mkdir -p ${LIBGUESTFS_PATH}
tar -Jxf ${LIBGUESTFS_APPLIANCE} -C ${LIBGUESTFS_PATH} --strip-components=1
touch ${LIBGUESTFS_PATH}/done

/bin/bash
