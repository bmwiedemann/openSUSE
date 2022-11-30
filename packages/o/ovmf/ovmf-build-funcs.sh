#!/bin/bash

# Generate PK/KEK OEM strings
pkkek_oemstr()
{
	local CERT_FILE=$1
	sed \
		-e 's/^-----BEGIN CERTIFICATE-----$/4e32566d-8e9e-4f52-81d3-5bb9715f9727:/' \
		-e '/^-----END CERTIFICATE-----$/d' \
		$CERT_FILE \
		| tr -d '\n'
}

# Build the varstore template
build_template()
{
	local ARCH=$(echo $1 | tr '[:lower:'] '[:upper:]')
	local PREFIX="$2"
	local KEY="$3"
	local PKKEK_FILE="$4"
	local ISO_FILE="$5"
	local TYPE="$6"

	# QEMU parameters
	#  pflash parameters
	local PFLASH=""
	if [ $TYPE == "separate" ]; then
		local FW_CODE_ORIG="${PREFIX}-code.bin"
		local FW_VARS_ORIG="${PREFIX}-vars.bin"
		local FW_CODE="${PREFIX}-${KEY}-code.bin"
		local FW_VARS="${PREFIX}-${KEY}-vars.bin"
		local PFLASH_CODE="-drive if=pflash,format=raw,unit=0,readonly=on,file=$FW_CODE"
		local PFLASH_VARS="-drive if=pflash,format=raw,unit=1,file=$FW_VARS"

		ln -s "$FW_CODE_ORIG" "$FW_CODE"
		cp "$FW_VARS_ORIG" "$FW_VARS"

		PFLASH="$PFLASH_CODE $PFLASH_VARS"
	elif [ $TYPE == "unified" ]; then
		local UNIFIED_FW_ORIG="${PREFIX}.bin"
		local UNIFIED_FW="${PREFIX}-${KEY}.bin"

		cp "$UNIFIED_FW_ORIG" "$UNIFIED_FW"

		PFLASH="-drive if=pflash,format=raw,unit=0,file=$UNIFIED_FW"
	fi

	#  smbios parameters for PK and KEK
	local SMBIOS="-smbios type=11,value=$(pkkek_oemstr $PKKEK_FILE)"

	#  memory: 256MB
	local MEMORY="-m 256"

	#  redirect display to stdio and disable network
	local MISC="-display none -no-user-config -nodefaults -smp 1"
	MISC="$MISC -serial stdio"

	#  set cdrom device
	local CDROM="-device virtio-scsi-pci,id=scsi0"
	CDROM="$CDROM -device scsi-cd,drive=cd0,bus=scsi0.0,bootindex=0"
	CDROM="$CDROM -drive media=cdrom,if=none,id=cd0,format=raw,readonly=on"
	CDROM="$CDROM,file=${ISO_FILE}"

	if [ $ARCH == "X64" ]; then
		# qemu command
		local QEMU="qemu-system-x86_64"

		# machine parameters
		local MACHINE="-machine q35"
		if [[ "$PREFIX" == *"-smm" ]]; then
			MACHINE="$MACHINE,smm=on,accel=tcg"
			MACHINE="$MACHINE -global driver=cfi.pflash01,property=secure,value=on"
			MACHINE="$MACHINE -global ICH9-LPC.disable_s3=1"
		fi
		MACHINE="$MACHINE -chardev pty,id=charserial1"
		MACHINE="$MACHINE -device isa-serial,chardev=charserial1,id=serial1"
	elif [ $ARCH == "AARCH64" ]; then
		# qemu command
		local QEMU="qemu-system-aarch64"

		# machine parameters
		local MACHINE="-cpu cortex-a57 -machine virt"
	fi

	# Launch the VM
	$QEMU $MACHINE $MEMORY $PFLASH $SMBIOS $CDROM $MISC
}
