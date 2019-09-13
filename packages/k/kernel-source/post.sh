# Flag to trigger /etc/init.d/purge-kernels on next reboot (fate#312018)
touch /boot/do_purge_kernels

suffix=
if test "@FLAVOR@" = "vanilla"; then
    suffix=-@FLAVOR@
fi
for x in /boot/@IMAGE@ /boot/initrd; do
    rm -f $x$suffix
    ln -s ${x##*/}-@KERNELRELEASE@-@FLAVOR@ $x$suffix
done

# Add symlinks of compatible modules to /lib/modules/$krel/weak-updates/,
# run depmod and mkinitrd
wm2=/usr/lib/module-init-tools/weak-modules2
if [ -x $wm2 ]; then
    if [ @BASE_PACKAGE@ = 1 ]; then
        /bin/bash -${-/e/} $wm2 --add-kernel @KERNELRELEASE@-@FLAVOR@
    else
        nvr=@SUBPACKAGE@-@RPM_VERSION_RELEASE@
        rpm -ql $nvr | /bin/bash -${-/e/} $wm2 --add-kernel-modules @KERNELRELEASE@-@FLAVOR@
    fi
else
    echo "$wm2 does not exist, please run depmod and mkinitrd manually" >&2
fi

message_install_bl () {
	echo "You may need to setup and install the boot loader using the"
	echo "available bootloader for your platform (e.g. grub, lilo, zipl, ...)."
}

run_bootloader () {
    if [ -f /etc/sysconfig/bootloader ] &&
	    [ -f /boot/grub/menu.lst -o \
	      -f /etc/lilo.conf      -o \
	      -f /etc/elilo.conf     -o \
	      -f /etc/zipl.conf      -o \
	      -f /etc/default/grub    ]
    then
	return 0
    else
	return 1
    fi
}

if [ -f /etc/fstab -a ! -e /.buildenv ] ; then
    # only run the bootloader if the usual bootloader configuration
    # files are there -- this is different on every architecture
    initrd=initrd-@KERNELRELEASE@-@FLAVOR@
    if [ @FLAVOR@ = rt ]; then
	    default=force-default
    fi
    if [ -e /boot/$initrd -o ! -e /lib/modules/@KERNELRELEASE@-@FLAVOR@ ] && \
       run_bootloader ; then
       [ -e /boot/$initrd ] || initrd=
	if [ -x /usr/lib/bootloader/bootloader_entry ]; then
	    /usr/lib/bootloader/bootloader_entry \
		add \
		@FLAVOR@ \
		@KERNELRELEASE@-@FLAVOR@ \
		@IMAGE@-@KERNELRELEASE@-@FLAVOR@ \
		$initrd \
		$default
	else
	    message_install_bl
	fi
    fi
else
    message_install_bl
fi

# vim: set sts=4 sw=4 ts=8 noet:
