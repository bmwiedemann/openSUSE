# If one of the modules in this package is in the initrd,
# we need to recreate the initrd.

if [ -e /etc/sysconfig/kernel -a -f /etc/fstab ]; then
    source /etc/sysconfig/kernel
    run_mkinitrd=
    for module in $INITRD_MODULES; do
	case " $MODULES " in
	*" $module "*)
	    run_mkinitrd=1
	    break ;;
	esac
    done
    if [ -n "$run_mkinitrd" ]; then
	for kernelrelease in $KERNELRELEASES; do
	    for image in vmlinuz image vmlinux linux bzImage; do
		if [ -f /boot/$image-$kernelrelease ]; then
		    /sbin/mkinitrd -k /boot/$image-$kernelrelease \
				   -i /boot/initrd-$kernelrelease \
		    || exit 1
		fi
	    done
	done
    fi
fi
