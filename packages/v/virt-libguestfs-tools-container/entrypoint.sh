#!/bin/bash -xe

#KubeVirt provides LIBGUESTFS_PATH via the pod environemnt.
DIR=/usr/local/lib/guestfs
LIBGUESTFS_VERSION=$(rpm -q --queryformat=%{version} libguestfs)
LIBGUESTFS_APPLIANCE=/appliance-${LIBGUESTFS_VERSION}.tar.xz

mkdir -p ${DIR}
tar -Jxf ${LIBGUESTFS_APPLIANCE} -C ${DIR}
touch ${DIR}/done

/bin/bash
