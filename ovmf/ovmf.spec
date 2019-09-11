#
# spec file for package ovmf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
# needssslcertforbuild


%define secureboot_archs x86_64 aarch64

%undefine _build_create_debug
%global openssl_version 1.1.1b
%global softfloat_version b64af41c3276f

Name:           ovmf
Url:            http://sourceforge.net/apps/mediawiki/tianocore/index.php?title=EDK2
Summary:        Open Virtual Machine Firmware
License:        BSD-2-Clause-Patent
Group:          System/Emulators/PC
Version:        201905
Release:        0
Source0:        https://github.com/tianocore/edk2/archive/edk2-stable%{version}.tar.gz
Source1:        https://www.openssl.org/source/openssl-%{openssl_version}.tar.gz
Source111:      https://www.openssl.org/source/openssl-%{openssl_version}.tar.gz.asc
Source112:      openssl.keyring
Source2:        README
Source3:        SLES-UEFI-CA-Certificate-2048.crt
Source4:        openSUSE-UEFI-CA-Certificate-2048.crt
Source5:        openSUSE-UEFI-SIGN-Certificate-2048.crt
# berkeley-softfloat-3: https://github.com/ucb-bar/berkeley-softfloat-3
Source6:        berkeley-softfloat-3-%{softfloat_version}.tar.xz
Source100:      %{name}-rpmlintrc
Source101:      gdb_uefi.py.in
Source102:      gen-key-enrollment-iso.sh
Patch1:         %{name}-add-exclude-shell-flag.patch
Patch2:         %{name}-gdb-symbols.patch
Patch3:         %{name}-pie.patch
Patch4:         %{name}-disable-ia32-firmware-piepic.patch
Patch5:         %{name}-set-fixed-enroll-time.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bc
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  iasl
BuildRequires:  libuuid-devel
BuildRequires:  python3
%ifnarch %arm
BuildRequires:  nasm
%endif
%ifarch %{secureboot_archs}
BuildRequires:  dosfstools
BuildRequires:  mkisofs
BuildRequires:  mtools
BuildRequires:  openssl
%ifarch x86_64
BuildRequires:  qemu-x86 >= 3.0.0
%endif
%ifarch aarch64
BuildRequires:  qemu-arm >= 3.0.0
BuildRequires:  qemu-ipxe
%endif
BuildRequires:  unzip
%endif
ExclusiveArch:  %ix86 x86_64 aarch64 %arm

%description
The Open Virtual Machine Firmware (OVMF) project aims to support
firmware for Virtual Machines using the edk2 code base.

%package tools
Summary:        The BaseTools from edk2
Group:          System/Emulators/PC

%description tools
The Open Virtual Machine Firmware (OVMF) project aims to support
firmware for Virtual Machines using the edk2 code base.

This package contains the tools from edk2.

%ifarch %ix86
%package -n qemu-ovmf-ia32
Summary:        Open Virtual Machine Firmware - QEMU rom images (IA32)
Group:          System/Emulators/PC
BuildArch:      noarch
Requires:       qemu

%description -n qemu-ovmf-ia32
The Open Virtual Machine Firmware (OVMF) project aims to support
firmware for Virtual Machines using the edk2 code base.

This package contains UEFI rom images for exercising UEFI secure
boot in a qemu environment (IA32)
%endif

%ifarch x86_64
%package -n qemu-ovmf-x86_64
Summary:        Open Virtual Machine Firmware - QEMU rom images (x86_64)
Group:          System/Emulators/PC
BuildArch:      noarch
Requires:       qemu

%description -n qemu-ovmf-x86_64
The Open Virtual Machine Firmware (OVMF) project aims to support
firmware for Virtual Machines using the edk2 code base.

This package contains UEFI rom images for exercising UEFI secure
boot in a qemu environment (x86_64)

%package -n qemu-ovmf-x86_64-debug
Summary:        Open Virtual Machine Firmware - debug symbols (x86_64)
Group:          Development/Sources
Requires:       qemu

%description -n qemu-ovmf-x86_64-debug
The Open Virtual Machine Firmware (OVMF) project aims to support
firmware for Virtual Machines using the edk2 code base.

This package contains the debug symbols for UEFI rom images (x86_64)

%endif

%ifarch aarch64
%package -n qemu-uefi-aarch64
Summary:        UEFI QEMU rom image (AArch64)
Group:          System/Emulators/PC
BuildArch:      noarch

%description -n qemu-uefi-aarch64
This package contains the UEFI rom image (AArch64) for QEMU cortex-a57
virt board.
%endif

%ifarch %arm
%package -n qemu-uefi-aarch32
Summary:        UEFI QEMU rom image (AArch32)
Group:          System/Emulators/PC
BuildArch:      noarch

%description -n qemu-uefi-aarch32
This package contains the UEFI rom image (AArch32) for QEMU cortex-a15
virt board.
%endif

%prep
%setup -q -n edk2-edk2-stable%{version}

# bsc#973038 Remove the packages we don't need to avoid any potential
# license issue. 
PKG_TO_REMOVE="AppPkg DuetPkg CorebootModulePkg CorebootPayloadPkg \
EmulatorPkg Nt32Pkg Omap35xxPkg QuarkPlatformPkg QuarkSocPkg StdLib \
StdLibPrivateInternalFiles UnixPkg Vlv2DeviceRefCodePkg Vlv2TbltDevicePkg"
rm -rf $PKG_TO_REMOVE

%ifarch x86_64
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# add openssl
pushd CryptoPkg/Library/OpensslLib/openssl
tar -xf %{SOURCE1} --strip 1
popd

# add berkeley-softfloat-3
pushd ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3
tar -xf %{SOURCE6} --strip 1
popd

chmod +x %{SOURCE102}

%build

# Enable python3 build
export PYTHON3_ENABLE=TRUE
export PYTHON_COMMAND=python3

OVMF_FLAGS="-D SECURE_BOOT_ENABLE -D TPM2_ENABLE -D TPM2_CONFIG_ENABLE\
 -D NETWORK_IP6_ENABLE -D NETWORK_HTTP_BOOT_ENABLE"

%if 0%{?suse_version} > 1320
TOOL_CHAIN_TAG=GCC5
%else
echo `gcc -dumpversion`
TOOL_CHAIN_TAG=GCC$(gcc -dumpversion|sed 's/\([0-9]\)\.\([0-9]\).*/\1\2/')
%endif

%ifarch %ix86
	# Flavors for x86
	FLAVORS=("ovmf-ia32")
	BUILD_ARCH="IA32"

	OVMF_FLAGS="$OVMF_FLAGS -D NETWORK_TLS_ENABLE -D FD_SIZE_2MB"
	BUILD_OPTIONS="$OVMF_FLAGS -a IA32 -p OvmfPkg/OvmfPkgIa32.dsc -b DEBUG -t $TOOL_CHAIN_TAG"
	make -C BaseTools
%else
%ifarch x86_64
	# Flavors for x86_64: 2MB, 4MB, and 4MB+SMM
	FLAVORS=("ovmf-x86_64" "ovmf-x86_64-4m" "ovmf-x86_64-smm")
	BUILD_ARCH="X64"

	BUILD_OPTIONS="$OVMF_FLAGS -a X64 -p OvmfPkg/OvmfPkgX64.dsc -b DEBUG -t $TOOL_CHAIN_TAG"
	make -C BaseTools
%else
%ifarch aarch64
	# Flavors for aarch64
	FLAVORS=("aavmf-aarch64")
	BUILD_ARCH="AARCH64"

	BUILD_OPTIONS="$OVMF_FLAGS -a AARCH64 -p ArmVirtPkg/ArmVirtQemu.dsc -b DEBUG -t $TOOL_CHAIN_TAG"
	ARCH=AARCH64 make -C BaseTools
%else
%ifarch %arm
	# Flavors for arm
	FLAVORS=("aavmf-aarch32")
	BUILD_ARCH="AARCH32"

	BUILD_OPTIONS="-a ARM -p ArmVirtPkg/ArmVirtQemu.dsc -b DEBUG -t $TOOL_CHAIN_TAG"
	ARCH=ARM make -C BaseTools
%else
	echo "ERROR: unsupported architecture"
	false
%endif #arm
%endif #aarch64
%endif #x86_64
%endif #ix86

. ./edksetup.sh

%ifarch %ix86
# Build the UEFI image
build $BUILD_OPTIONS

cp Build/OvmfIa32/DEBUG_*/FV/OVMF.fd ovmf-ia32.bin
cp Build/OvmfIa32/DEBUG_*/FV/OVMF_CODE.fd ovmf-ia32-code.bin
cp Build/OvmfIa32/DEBUG_*/FV/OVMF_VARS.fd ovmf-ia32-vars.bin
%else
%ifarch x86_64

collect_debug_files()
{
	target="$1"
	out_dir="debug/$target"
	abs_path="`pwd`/$out_dir/"
	source_path="`pwd`"
	gdb_src_path="/usr/src/debug/ovmf-x86_64"

	# copy the debug symbols
	mkdir -p $out_dir
	pushd Build/OvmfX64/DEBUG_GCC*/X64/
	find . -mindepth 2 -type f -name "*.debug" -exec cp --parents -a {} $abs_path \;
	cp --parents -a DebugPkg/GdbSyms/GdbSyms/DEBUG/GdbSyms.dll $abs_path
	build_path=`pwd`
	popd

	# Change the path in the python gdb script
	sed "s:__BUILD_PATH__:$build_path:;s:__SOURCE_PATH__:$source_path:;s:__GDB_SRC_PATH__:$gdb_src_path:;s/__FLAVOR__/$target/" \
	  %{SOURCE101} > gdb_uefi-$target.py
}

declare -A EXTRA_FLAGS
EXTRA_FLAGS=(
	[ovmf-x86_64]="-D FD_SIZE_2MB"
	[ovmf-x86_64-4m]="-D FD_SIZE_4MB -D NETWORK_TLS_ENABLE"
	[ovmf-x86_64-smm]="-D FD_SIZE_4MB -D NETWORK_TLS_ENABLE -D SMM_REQUIRE -D EXCLUDE_SHELL"
)

for flavor in ${FLAVORS[@]}; do
	build $BUILD_OPTIONS ${EXTRA_FLAGS[$flavor]}
	cp Build/OvmfX64/DEBUG_*/FV/OVMF.fd      $flavor.bin
	cp Build/OvmfX64/DEBUG_*/FV/OVMF_CODE.fd $flavor-code.bin
	cp Build/OvmfX64/DEBUG_*/FV/OVMF_VARS.fd $flavor-vars.bin

	collect_debug_files $flavor
done

# Copy Shell.efi and EnrollDefaultKeys.efi
cp Build/OvmfX64/DEBUG_*/X64/Shell.efi .
cp Build/OvmfX64/DEBUG_*/X64/EnrollDefaultKeys.efi .

# Collect the source
mkdir -p source/ovmf-x86_64
#   TODO get the source list from debug files
src_list=`find Build/OvmfX64/DEBUG_GCC*/X64/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \;`
find $src_list \( -name "*.c" -o -name "*.h" \) -type f -exec cp --parents -a {} source/ovmf-x86_64 \;
find source/ovmf-x86_64 -name *.c -type f -exec chmod 0644 {} \;

# Build with keys done later (shared between archs)

%else
%ifarch aarch64

# Build the UEFI image without keys
build $BUILD_OPTIONS

cp Build/ArmVirtQemu-AARCH64/DEBUG_GCC*/FV/QEMU_EFI.fd qemu-uefi-aarch64.bin
dd of="aavmf-aarch64-code.bin" if="/dev/zero" bs=1M count=64
dd of="aavmf-aarch64-code.bin" if="qemu-uefi-aarch64.bin" conv=notrunc
dd of="aavmf-aarch64-vars.bin" if="/dev/zero" bs=1M count=64

# Copy Shell.efi and EnrollDefaultKeys.efi
cp Build/ArmVirtQemu-AARCH64/DEBUG_*/AARCH64/Shell.efi .
cp Build/ArmVirtQemu-AARCH64/DEBUG_*/AARCH64/EnrollDefaultKeys.efi .

%else
%ifarch %arm

# Build the UEFI image
build $BUILD_OPTIONS

cp Build/ArmVirtQemu-ARM/DEBUG_GCC*/FV/QEMU_EFI.fd qemu-uefi-aarch32.bin
dd of="aavmf-aarch32-code.bin" if="/dev/zero" bs=1M count=64
dd of="aavmf-aarch32-code.bin" if="qemu-uefi-aarch32.bin" conv=notrunc
dd of="aavmf-aarch32-vars.bin" if="/dev/zero" bs=1M count=64
%endif #arm
%endif #aarch64
%endif #x86_64
%endif #ix86

# Builds with keys is shared between archs
%ifarch %{secureboot_archs}

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

	local FW_CODE_ORIG="${PREFIX}-code.bin"
	local FW_VARS_ORIG="${PREFIX}-vars.bin"
	local FW_CODE="${PREFIX}-${KEY}-code.bin"
	local FW_VARS="${PREFIX}-${KEY}-vars.bin"

	ln -s "$FW_CODE_ORIG" "$FW_CODE"
	cp "$FW_VARS_ORIG" "$FW_VARS"

	# QEMU parameters
	#  pflash parameters
	local PFLASH_CODE="-drive if=pflash,format=raw,unit=0,readonly,file=$FW_CODE"
	local PFLASH_VARS="-drive if=pflash,format=raw,unit=1,file=$FW_VARS"

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
	$QEMU $MACHINE $MEMORY $PFLASH_CODE $PFLASH_VARS $SMBIOS $CDROM $MISC
}

# Assign the default PK/KEK
declare -A PKKEK
PKKEK=(
	[ms]=%{SOURCE3}
	[suse]=%{SOURCE3}
	[opensuse]=%{SOURCE4}
	[devel]=%{_sourcedir}/_projectcert.crt
)

# Assign the key iso file
MS_ISO_FILE=ms-keys.iso
NOMS_ISO_FILE=no-ms-keys.iso
declare -A KEY_ISO_FILES
KEY_ISO_FILES=(
	[ms]=$MS_ISO_FILE
	[suse]=$NOMS_ISO_FILE
	[opensuse]=$NOMS_ISO_FILE
	[devel]=$NOMS_ISO_FILE
)

# Default key sources: ms suse opensuse
KEY_SOURCES=(ms suse opensuse)

#   Add 'devel' if necessary
if [ -e %{_sourcedir}/_projectcert.crt ]; then
	prjissuer=$(openssl x509 -in %{_sourcedir}/_projectcert.crt -noout -issuer_hash)
	opensusesubject=$(openssl x509 -in %{SOURCE4} -noout -subject_hash)
	slessubject=$(openssl x509 -in %{SOURCE3} -noout -subject_hash)
	if [ "$prjissuer" != "$opensusesubject" -a "$prjissuer" != "$slessubject" ]; then
		KEY_SOURCES+=(devel)
	fi
fi

# Create the iso images
GEN_ISO=%{SOURCE102}
SHELL=Shell.efi
ENROLLER=EnrollDefaultKeys.efi
$GEN_ISO $BUILD_ARCH $SHELL $ENROLLER default    $MS_ISO_FILE
$GEN_ISO $BUILD_ARCH $SHELL $ENROLLER no-default $NOMS_ISO_FILE

# Generate the varstore templates
for flavor in ${FLAVORS[@]}; do
	for key in ${KEY_SOURCES[@]}; do
		build_template "$BUILD_ARCH" "$flavor" "$key" \
			"${PKKEK[$key]}" "${KEY_ISO_FILES[$key]}"
	done
done

%endif #secureboot_archs

%install
rm -rf %{buildroot}
cp %{SOURCE2} README

sed -i s/'\r'// License.txt

# Install BaseTools
install -d %{buildroot}/%{_bindir}
install -m 0755 --strip BaseTools/Source/C/bin/EfiRom %{buildroot}/%{_bindir}

%ifarch %ix86
tr -d '\r' < OvmfPkg/License.txt > License-ovmf.txt
install -m 0644 -D ovmf-ia32.bin %{buildroot}/%{_datadir}/qemu/ovmf-ia32.bin
install -m 0644 -D ovmf-ia32-code.bin %{buildroot}/%{_datadir}/qemu/ovmf-ia32-code.bin
install -m 0644 -D ovmf-ia32-vars.bin %{buildroot}/%{_datadir}/qemu/ovmf-ia32-vars.bin
%else
%ifarch x86_64
tr -d '\r' < OvmfPkg/License.txt > License-ovmf.txt

# Install firmware files
install -m 0644 -D ovmf-x86_64.bin %{buildroot}/%{_datadir}/qemu/ovmf-x86_64.bin
install -m 0644 ovmf-x86_64-*.bin %{buildroot}/%{_datadir}/qemu/
%fdupes %{buildroot}/%{_datadir}/qemu/

# Install debug symbols, gdb-uefi.py
install -d %{buildroot}/%{_datadir}/ovmf-x86_64/
install -m 0644 gdb_uefi-*.py %{buildroot}/%{_datadir}/ovmf-x86_64/
mkdir -p %{buildroot}/usr/lib/debug
mv debug/ovmf-x86_64* %{buildroot}/usr/lib/debug
%fdupes %{buildroot}/usr/lib/debug/ovmf-x86_64*
mkdir -p %{buildroot}/usr/src/debug
mv source/ovmf-x86_64* %{buildroot}/usr/src/debug
%fdupes -s %{buildroot}/usr/src/debug/ovmf-x86_64

%else
%ifarch aarch64
# Install firmware files
install -d %{buildroot}/%{_datadir}/qemu/
install -m 0644 -D qemu-uefi-aarch64*.bin %{buildroot}/%{_datadir}/qemu/
install -m 0644 -D aavmf-aarch64-*code.bin %{buildroot}/%{_datadir}/qemu/
install -m 0644 -D aavmf-aarch64-*vars.bin %{buildroot}/%{_datadir}/qemu/
%fdupes %{buildroot}/%{_datadir}/qemu/

%else
%ifarch %arm
install -m 0644 -D qemu-uefi-aarch32.bin %{buildroot}/%{_datadir}/qemu/qemu-uefi-aarch32.bin
install -m 0644 -D aavmf-aarch32-code.bin %{buildroot}/%{_datadir}/qemu/aavmf-aarch32-code.bin
install -m 0644 -D aavmf-aarch32-vars.bin %{buildroot}/%{_datadir}/qemu/aavmf-aarch32-vars.bin
%endif #arm
%endif #aarch64
%endif #x86_64
%endif #ix86

%ifarch %{secureboot_archs}
# Install EnrollDefaultKeys.efi
mkdir -p %{buildroot}/%{_datadir}/ovmf/
install -m 0644 Shell.efi %{buildroot}/%{_datadir}/ovmf/
install -m 0644 EnrollDefaultKeys.efi %{buildroot}/%{_datadir}/ovmf/
install -m 0755 %{SOURCE102} %{buildroot}/%{_datadir}/ovmf/
%endif

%files
%defattr(-,root,root)
%doc README
%ifarch %{secureboot_archs}
%dir %{_datadir}/ovmf/
%{_datadir}/ovmf/*.efi
%{_datadir}/ovmf/*.sh
%endif

%files tools
%defattr(-,root,root)
%doc BaseTools/UserManuals/EfiRom_Utility_Man_Page.rtf
%{_bindir}/EfiRom

%ifarch %ix86
%files -n qemu-ovmf-ia32
%defattr(-,root,root)
%license License.txt License-ovmf.txt 
%dir %{_datadir}/qemu/
%{_datadir}/qemu/ovmf-ia32*.bin
%endif

%ifarch x86_64
%files -n qemu-ovmf-x86_64
%defattr(-,root,root)
%license License.txt License-ovmf.txt
%dir %{_datadir}/qemu/
%{_datadir}/qemu/ovmf-x86_64*.bin

%files -n qemu-ovmf-x86_64-debug
%defattr(-,root,root)
%{_datadir}/ovmf-x86_64/
%dir /usr/lib/debug/
/usr/lib/debug/ovmf-x86_64*
%dir /usr/src/debug/
/usr/src/debug/ovmf-x86_64*
%endif

%ifarch aarch64
%files -n qemu-uefi-aarch64
%defattr(-,root,root)
%license License.txt
%dir %{_datadir}/qemu/
%{_datadir}/qemu/qemu-uefi-aarch64*.bin
%{_datadir}/qemu/aavmf-aarch64-*code.bin
%{_datadir}/qemu/aavmf-aarch64-*vars.bin
%endif

%ifarch %arm
%files -n qemu-uefi-aarch32
%defattr(-,root,root)
%license License.txt
%dir %{_datadir}/qemu/
%{_datadir}/qemu/qemu-uefi-aarch32.bin
%{_datadir}/qemu/aavmf-aarch32-code.bin
%{_datadir}/qemu/aavmf-aarch32-vars.bin
%endif

%changelog
