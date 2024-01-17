#!/bin/bash -e
# The script to generate the key enrollment iso file
#  based on build_iso() in https://git.kraxel.org/cgit/jenkins/edk2/tree/edk2.git.spec

# Example: $0 X64 Shell.efi EnrollDefaultKeys.efi default key.iso

usage()
{
        PROG_NAME=$1
        echo "Usage: $PROG_NAME <Arch> <Shell> <Enroller> <Type> <ISO NAME>"
        echo "ex: $PROG_NAME X64 Shell.efi EnrollDefaultKeys.efi default key.iso"
}

ARCH=$(echo $1 | tr '[:lower:'] '[:upper:]')
UEFI_SHELL_BINARY="$2"
ENROLLER_BINARY="$3"
TYPE="$4"
ISO_NAME="$5"

# Check the arguments
if [ x$ARCH != xX64 ] && [ x$ARCH != xAARCH64 ]; then
        echo "Supported architecture: X64, AARCH64"
        usage $0
        exit 1
fi

if [ x$UEFI_SHELL_BINARY == x ] || [ ! -e "$UEFI_SHELL_BINARY" ]; then
        echo "Please specify the UEFI shell binary"
        usage $0
        exit 1
fi

if [ x$ENROLLER_BINARY == x ] || [ ! -e "$ENROLLER_BINARY" ]; then
        echo "Please specify the enroller binary"
        usage $0
        exit 1
fi

if [ x$TYPE == x ]; then
        echo "Please specify the type of image: default or no-default"
        usage $0
        exit 1
fi

if [ x$ISO_NAME == x ]; then
        echo "Please specify the name of output iso"
        usage $0
        exit 1
fi

ISO_PATH=$(realpath $ISO_NAME)

TMP_DIR=$(mktemp -d)

cp $UEFI_SHELL_BINARY $TMP_DIR/Shell.efi
cp $ENROLLER_BINARY   $TMP_DIR/EnrollDefaultKeys.efi

UEFI_BOOT_EFI=$(
	if [ $ARCH == "X64" ]; then
		echo bootx64.efi
	elif [ $ARCH == "AARCH64" ]; then
		echo bootaa64.efi
        else
                exit 1
	fi
)

UEFI_SHELL_SIZE=$(stat --format=%s -- "$UEFI_SHELL_BINARY")
ENROLLER_SIZE=$(stat --format=%s -- "$ENROLLER_BINARY")
START_SCRIPT=$TMP_DIR/"startup.nsh"

# Enter the first ESP
echo "fs0:" > $START_SCRIPT
# Enroll the keys
if [ $TYPE == "default" ]; then
	echo "EnrollDefaultKeys.efi" >> $START_SCRIPT
else
	echo "EnrollDefaultKeys.efi --no-default" >> $START_SCRIPT
fi
# Reset BootOrder
echo "setvar BootOrder -guid 8be4df61-93ca-11d2-aa0d-00e098032b8c -bs -rt -nv =" >> $START_SCRIPT
# Shutdown the system
echo "reset -s" >> $START_SCRIPT

UEFI_SHELL_IMAGE=uefi_shell_${ARCH}_${TYPE}.img
# Add 1MB then 10% for metadata
UEFI_SHELL_IMAGE_KB=$((
	(UEFI_SHELL_SIZE + ENROLLER_SIZE +
	 1 * 1024 * 1024) * 11 / 10 / 1024
))

pushd $TMP_DIR

# Create non-partitioned FAT image
rm -f -- "$UEFI_SHELL_IMAGE"
/usr/sbin/mkdosfs -C "$UEFI_SHELL_IMAGE" -n UEFI_SHELL -- "$UEFI_SHELL_IMAGE_KB"

export MTOOLS_SKIP_CHECK=1
mmd	-i "$UEFI_SHELL_IMAGE"				::efi
mmd	-i "$UEFI_SHELL_IMAGE"				::efi/boot
mcopy	-i "$UEFI_SHELL_IMAGE"	Shell.efi       	::efi/boot/$UEFI_BOOT_EFI
mcopy	-i "$UEFI_SHELL_IMAGE"	"$START_SCRIPT"		::efi/boot/startup.nsh
mcopy	-i "$UEFI_SHELL_IMAGE"	EnrollDefaultKeys.efi	::EnrollDefaultKeys.efi
mdir	-i "$UEFI_SHELL_IMAGE"	-/			::

# build ISO with FAT image file as El Torito EFI boot image
mkisofs -input-charset ASCII -J -rational-rock \
	-eltorito-platform efi -eltorito-boot "$UEFI_SHELL_IMAGE" \
	-no-emul-boot -o "$ISO_PATH" -- "$UEFI_SHELL_IMAGE"

popd

#rm -rf $TMP_DIR
