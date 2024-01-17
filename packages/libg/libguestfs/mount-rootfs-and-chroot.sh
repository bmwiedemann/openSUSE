#!/bin/bash
# Usage: $0 /dev/sda5
rootfs=$1
mnt=/sysroot
mounts=

if test -b "${rootfs}"
then

    mkdir -v -p "${mnt}"

    if mount -v "${rootfs}" "${mnt}"
    then

        for i in dev dev/pts proc sys selinux
        do
            if test -d /${i} && test -d "${mnt}/${i}" && test "`stat -c %D /`" != "`stat -c %D ${i}`"
            then
                mount -v --bind /${i} "${mnt}/${i}"
            fi
        done

        chroot "${mnt}" su -

        while read b m rest
        do
            case "${m}" in
                ${mnt}*)
                    mounts="${m} ${mounts}"
                ;;
            esac
        done <<-EOF
`
cat < /proc/mounts
`
EOF

        for i in ${mounts}
        do
            umount -v "${i}"
        done

    fi

fi
