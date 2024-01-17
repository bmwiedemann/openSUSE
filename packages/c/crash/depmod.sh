# Need to call depmod when the list of modules changes
for kernelrelease in $KERNELRELEASES; do
    if [ -e /boot/System.map-$kernelrelease ]; then
	depmod -a -F /boot/System.map-$kernelrelease $kernelrelease
    fi
done
