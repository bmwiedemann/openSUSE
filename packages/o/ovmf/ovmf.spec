#
# spec file for package ovmf
#
# Copyright (c) 2022 SUSE LLC
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


%undefine _build_create_debug
%global openssl_version 1.1.1n
%global softfloat_version b64af41c3276f

Name:           ovmf
Version:        202211
Release:        0
Summary:        Open Virtual Machine Firmware
License:        BSD-2-Clause-Patent
Group:          System/Emulators/PC
URL:            https://github.com/tianocore/edk2
Source0:        edk2-edk2-stable%{version}.tar.gz
Source1:        https://www.openssl.org/source/openssl-%{openssl_version}.tar.gz
Source111:      https://www.openssl.org/source/openssl-%{openssl_version}.tar.gz.asc
Source112:      openssl.keyring
Source2:        README
Source3:        SLES-UEFI-CA-Certificate-2048.crt
Source4:        openSUSE-UEFI-CA-Certificate-2048.crt
Source5:        openSUSE-UEFI-SIGN-Certificate-2048.crt
# berkeley-softfloat-3: https://github.com/ucb-bar/berkeley-softfloat-3
Source6:        berkeley-softfloat-3-%{softfloat_version}.tar.xz
Source7:        descriptors.tar.xz
# oniguruma: https://github.com/kkos/oniguruma,  "src" directory only
Source8:        oniguruma-v6.9.4_mark1-src.tar.xz
Source100:      %{name}-rpmlintrc
Source101:      gdb_uefi.py.in
Source102:      gen-key-enrollment-iso.sh
Source103:      ovmf-build-funcs.sh
Patch1:         %{name}-gdb-symbols.patch
Patch2:         %{name}-pie.patch
Patch3:         %{name}-disable-ia32-firmware-piepic.patch
Patch4:         %{name}-set-fixed-enroll-time.patch
Patch5:         %{name}-disable-brotli.patch
Patch6:         %{name}-ignore-spurious-GCC-12-warning.patch
Patch7:         %{name}-tools_def-add-fno-omit-frame-pointer-to-GCC48_-IA32-.patch
# PED-1359, because nasm-2.14 doesn't support corresponding instructions.
Patch8:         %{name}-Revert-MdePkg-Remove-the-macro-definitions-regarding.patch
Patch9:         %{name}-Revert-UefiCpuPkg-Replace-Opcode-with-the-correspond.patch
Patch10:        %{name}-Revert-SourceLevelDebugPkg-Replace-Opcode-with-the-c.patch
Patch11:        %{name}-Revert-MdePkg-Replace-Opcode-with-the-corresponding-.patch
Patch12:        %{name}-Revert-MdeModulePkg-Replace-Opcode-with-the-correspo.patch
# Bug 1205978 - Got Page-Fault exception when VM is booting with edk2-stable202211 ovmf
Patch13:        %{name}-Revert-OvmfPkg-PlatformInitLib-dynamic-mmio-window-s.patch
BuildRequires:  bc
BuildRequires:  cross-arm-binutils
BuildRequires:  cross-arm-gcc%{gcc_version}
BuildRequires:  dosfstools
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  iasl
BuildRequires:  libuuid-devel
BuildRequires:  mkisofs
BuildRequires:  mtools
BuildRequires:  nasm
BuildRequires:  openssl
BuildRequires:  python3
BuildRequires:  qemu-arm >= 3.0.0
BuildRequires:  qemu-ipxe
BuildRequires:  qemu-x86 >= 3.0.0
BuildRequires:  unzip
%ifarch x86_64
BuildRequires:  cross-aarch64-binutils
BuildRequires:  cross-aarch64-gcc%{gcc_version}
%endif
%ifarch aarch64
BuildRequires:  cross-x86_64-binutils
BuildRequires:  cross-x86_64-gcc%{gcc_version}
%endif
# Only build on the architectures with
#  1. cross-compilers, 2. iasl, 3. qemu-arm and qemu-x86
ExclusiveArch:  x86_64 aarch64

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

%package -n qemu-ovmf-ia32
Summary:        Open Virtual Machine Firmware - QEMU rom images (IA32)
Group:          System/Emulators/PC
Requires:       qemu
BuildArch:      noarch

%description -n qemu-ovmf-ia32
The Open Virtual Machine Firmware (OVMF) project aims to support
firmware for Virtual Machines using the edk2 code base.

This package contains UEFI rom images for exercising UEFI secure
boot in a qemu environment (IA32)

%package -n qemu-ovmf-x86_64
Summary:        Open Virtual Machine Firmware - QEMU rom images (x86_64)
Group:          System/Emulators/PC
Requires:       qemu
BuildArch:      noarch

%description -n qemu-ovmf-x86_64
The Open Virtual Machine Firmware (OVMF) project aims to support
firmware for Virtual Machines using the edk2 code base.

This package contains UEFI rom images for exercising UEFI secure
boot in a qemu environment (x86_64)

%ifarch x86_64
%package -n qemu-ovmf-x86_64-debug
Summary:        Open Virtual Machine Firmware - debug symbols (x86_64)
Group:          Development/Sources
Requires:       qemu

%description -n qemu-ovmf-x86_64-debug
The Open Virtual Machine Firmware (OVMF) project aims to support
firmware for Virtual Machines using the edk2 code base.

This package contains the debug symbols for UEFI rom images (x86_64)
%endif

%package -n qemu-uefi-aarch64
Summary:        UEFI QEMU rom image (AArch64)
Group:          System/Emulators/PC
BuildArch:      noarch

%description -n qemu-uefi-aarch64
This package contains the UEFI rom image (AArch64) for QEMU cortex-a57
virt board.

%package -n qemu-uefi-aarch32
Summary:        UEFI QEMU rom image (AArch32)
Group:          System/Emulators/PC
BuildArch:      noarch

%description -n qemu-uefi-aarch32
This package contains the UEFI rom image (AArch32) for QEMU cortex-a15
virt board.

%prep
%setup -q -n edk2-edk2-stable%{version}

# bsc#973038 Remove the packages we don't need to avoid any potential
# license issue.
PKG_TO_REMOVE="EmulatorPkg"
rm -rf $PKG_TO_REMOVE

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150500
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%endif
%patch13 -p1

# add openssl
pushd CryptoPkg/Library/OpensslLib/openssl
tar -xf %{SOURCE1} --strip 1
popd

# add berkeley-softfloat-3
pushd ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3
tar -xf %{SOURCE6} --strip 1
popd

# prepare the firmware descriptors for qemu
tar -xf %{SOURCE7}

# add oniguruma
pushd MdeModulePkg/Universal/RegularExpressionDxe/oniguruma
tar -xf %{SOURCE8} --strip 1
popd

chmod +x %{SOURCE102}

%build

# Enable python3 build
export PYTHON3_ENABLE=TRUE
export PYTHON_COMMAND=python3

# For some reason ARM still uses TPM2_CONFIG_ENABLE
OVMF_FLAGS=" \
	-D SECURE_BOOT_ENABLE \
	-D TPM2_ENABLE \
	-D TPM2_CONFIG_ENABLE \
	-D NETWORK_IP6_ENABLE \
	-D NETWORK_HTTP_BOOT_ENABLE \
"

%if 0%{?suse_version} > 1320
TOOL_CHAIN=GCC5
%else
echo `gcc -dumpversion`
TOOL_CHAIN=GCC$(gcc -dumpversion|sed 's/\([0-9]\)\.\([0-9]\).*/\1\2/')
%endif

# Flavors for x86
FLAVORS_X86=("ovmf-ia32")
BUILD_OPTIONS_X86=" \
	$OVMF_FLAGS \
	-D FD_SIZE_2MB \
	-a IA32 \
	-p OvmfPkg/OvmfPkgIa32.dsc \
	-b DEBUG \
	-t $TOOL_CHAIN \
"

# Flavors for x86_64: 2MB, 4MB, and 4MB+SMM
FLAVORS_X64=("ovmf-x86_64" "ovmf-x86_64-4m" "ovmf-x86_64-smm")
BUILD_OPTIONS_X64=" \
	$OVMF_FLAGS \
	-a X64 \
	-b DEBUG \
	-t $TOOL_CHAIN \
"

# Flavors for aarch64
FLAVORS_AA64=("aavmf-aarch64")
BUILD_OPTIONS_AA64=" \
	$OVMF_FLAGS \
	-D NETWORK_TLS_ENABLE \
	-a AARCH64 \
	-p ArmVirtPkg/ArmVirtQemu.dsc \
	-b DEBUG \
	-t $TOOL_CHAIN \
"

# Flavors for arm
FLAVORS_AA32=("aavmf-aarch32")
BUILD_OPTIONS_AA32=" \
	-a ARM \
	-p ArmVirtPkg/ArmVirtQemu.dsc \
	-b DEBUG \
	-t $TOOL_CHAIN \
"

# Build BaseTools
%ifarch x86_64
	make -C BaseTools
%endif
%ifarch aarch64
	ARCH=AARCH64 make -C BaseTools
%endif

# Import the build functions
source %{SOURCE103}
source ./edksetup.sh

### Build x86 UEFI Images ###
%ifnarch %{ix86} x86_64
# Assign the cross-compiler prefix
export ${TOOL_CHAIN}_BIN="x86_64-suse-linux-"
%endif
build $BUILD_OPTIONS_X86

cp Build/OvmfIa32/DEBUG_*/FV/OVMF.fd ovmf-ia32.bin
cp Build/OvmfIa32/DEBUG_*/FV/OVMF_CODE.fd ovmf-ia32-code.bin
cp Build/OvmfIa32/DEBUG_*/FV/OVMF_VARS.fd ovmf-ia32-vars.bin

# Remove the temporary build files to reduce the disk usage (bsc#1178244)
rm -rf Build/OvmfIa32/

### Build x86_64 UEFI Images ###
%ifarch x86_64
collect_x86_64_debug_files()
{
	local target="$1"
	local out_dir="debug/$target"
	local abs_path="`pwd`/$out_dir/"
	local source_path="`pwd`"
	local gdb_src_path="%{_prefix}/src/debug/ovmf-x86_64"

	# copy the debug symbols
	mkdir -p $out_dir
	pushd Build/OvmfX64/DEBUG_GCC*/X64/
	find . -mindepth 2 -type f -name "*.debug" -print0 | sort -z | xargs -i -0 cp --parents -a {} $abs_path
	cp --parents -a DebugPkg/GdbSyms/GdbSyms/DEBUG/GdbSyms.dll $abs_path
	build_path=`pwd`
	popd

	# Change the path in the python gdb script
	sed "s:__BUILD_PATH__:$build_path:;s:__SOURCE_PATH__:$source_path:;s:__GDB_SRC_PATH__:$gdb_src_path:;s/__FLAVOR__/$target/" \
	  %{SOURCE101} > gdb_uefi-$target.py
}
%endif

declare -A EXTRA_FLAGS_X64
EXTRA_FLAGS_X64=(
	[ovmf-x86_64]="-p OvmfPkg/OvmfPkgX64.dsc -D FD_SIZE_2MB -D BUILD_SHELL=FALSE"
	[ovmf-x86_64-4m]="-p OvmfPkg/OvmfPkgX64.dsc -D FD_SIZE_4MB -D NETWORK_TLS_ENABLE"
	[ovmf-x86_64-smm]="-a IA32 -p OvmfPkg/OvmfPkgIa32X64.dsc -D FD_SIZE_4MB -D NETWORK_TLS_ENABLE -D SMM_REQUIRE -D BUILD_SHELL=FALSE"
)
declare -A OUTDIR_X64
OUTDIR_X64=(
	[ovmf-x86_64]="OvmfX64"
	[ovmf-x86_64-4m]="OvmfX64"
	[ovmf-x86_64-smm]="Ovmf3264"
)

%ifnarch x86_64
# Assign the cross-compiler prefix
export ${TOOL_CHAIN}_BIN="x86_64-suse-linux-"
%endif
for flavor in ${FLAVORS_X64[@]}; do
	build $BUILD_OPTIONS_X64 ${EXTRA_FLAGS_X64[$flavor]}
	cp Build/${OUTDIR_X64[$flavor]}/DEBUG_*/FV/OVMF.fd      $flavor.bin
	cp Build/${OUTDIR_X64[$flavor]}/DEBUG_*/FV/OVMF_CODE.fd $flavor-code.bin
	cp Build/${OUTDIR_X64[$flavor]}/DEBUG_*/FV/OVMF_VARS.fd $flavor-vars.bin

%ifarch x86_64
	collect_x86_64_debug_files $flavor
%endif
done

# Copy Shell.efi and EnrollDefaultKeys.efi
mkdir X64
cp Build/OvmfX64/DEBUG_*/X64/Shell.efi X64
cp Build/OvmfX64/DEBUG_*/X64/EnrollDefaultKeys.efi X64

%ifarch x86_64
# Collect the source
mkdir -p source/ovmf-x86_64
#   TODO get the source list from debug files
src_list=`find Build/OvmfX64/DEBUG_GCC*/X64/ -mindepth 1 -maxdepth 1 -type d -print0 | sort -z | xargs -0 -i basename {}`
find $src_list \( -name "*.c" -o -name "*.h" \) -type f -print0 | sort -z | xargs -0 -i cp --parents -a {} source/ovmf-x86_64
find source/ovmf-x86_64 -name *.c -type f -exec chmod 0644 {} \;
%endif

# The extra Xen flavor for x86_64
BUILD_OPTION_X64_XEN=" \
	-p OvmfPkg/OvmfXen.dsc \
	-a X64 \
	-b DEBUG \
	-t $TOOL_CHAIN \
"
#  Build the 2MB Xen flavor
build $BUILD_OPTION_X64_XEN -D FD_SIZE_2MB
cp Build/OvmfXen/DEBUG_*/FV/OVMF.fd ovmf-x86_64-xen.bin
#  Build the 4MB Xen flavor
build $BUILD_OPTION_X64_XEN -D FD_SIZE_4MB
cp Build/OvmfXen/DEBUG_*/FV/OVMF.fd ovmf-x86_64-xen-4m.bin

# Remove the temporary build files to reduce the disk usage (bsc#1178244)
rm -rf Build/OvmfX64/ Build/Ovmf3264/ Build/OvmfXen/

# Build with keys done later (shared between archs)

### Build AARCH64 UEFI Images ###
%ifnarch aarch64
# Assign the cross-compiler prefix
export ${TOOL_CHAIN}_AARCH64_PREFIX="aarch64-suse-linux-"
%endif
# Build the UEFI image without keys
build $BUILD_OPTIONS_AA64

cp Build/ArmVirtQemu-AARCH64/DEBUG_GCC*/FV/QEMU_EFI.fd qemu-uefi-aarch64.bin
dd of="aavmf-aarch64-code.bin" if="/dev/zero" bs=1M count=64
dd of="aavmf-aarch64-code.bin" if="qemu-uefi-aarch64.bin" conv=notrunc
dd of="aavmf-aarch64-vars.bin" if="/dev/zero" bs=1M count=64

# Copy Shell.efi and EnrollDefaultKeys.efi
mkdir AARCH64
cp Build/ArmVirtQemu-AARCH64/DEBUG_*/AARCH64/Shell.efi AARCH64
cp Build/ArmVirtQemu-AARCH64/DEBUG_*/AARCH64/EnrollDefaultKeys.efi AARCH64

# Remove the temporary build files to reduce the disk usage (bsc#1178244)
rm -rf Build/ArmVirtQemu-AARCH64/

# Build with keys done later (shared between archs)

### Build AARCH32 UEFI Images ###
%ifnarch armv7hl
# Assign the cross-compiler prefix
export ${TOOL_CHAIN}_ARM_PREFIX="arm-suse-linux-gnueabi-"
%endif
# Build the UEFI image
build $BUILD_OPTIONS_AA32

cp Build/ArmVirtQemu-ARM/DEBUG_GCC*/FV/QEMU_EFI.fd qemu-uefi-aarch32.bin
dd of="aavmf-aarch32-code.bin" if="/dev/zero" bs=1M count=64
dd of="aavmf-aarch32-code.bin" if="qemu-uefi-aarch32.bin" conv=notrunc
dd of="aavmf-aarch32-vars.bin" if="/dev/zero" bs=1M count=64

# Remove the temporary build files to reduce the disk usage (bsc#1178244)
rm -rf Build/ArmVirtQemu-ARM/

### Build the variable store templates ###

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

# Assign the default PK/KEK
declare -A PKKEK
PKKEK=(
	[ms]=%{SOURCE3}
	[suse]=%{SOURCE3}
	[opensuse]=%{SOURCE4}
	[devel]=%{_sourcedir}/_projectcert.crt
)

generate_sb_var_templates()
{
	local ARCH=$1

	# Assign the key iso file
	local MS_ISO_FILE=ms-keys-${ARCH}.iso
	local NOMS_ISO_FILE=no-ms-keys-${ARCH}.iso
	declare -A KEY_ISO_FILES
	KEY_ISO_FILES=(
		[ms]=$MS_ISO_FILE
		[suse]=$NOMS_ISO_FILE
		[opensuse]=$NOMS_ISO_FILE
		[devel]=$NOMS_ISO_FILE
	)

	# Create the iso images
	local GEN_ISO=%{SOURCE102}
	local SHELL=${ARCH}/Shell.efi
	local ENROLLER=${ARCH}/EnrollDefaultKeys.efi
	$GEN_ISO $ARCH $SHELL $ENROLLER default    $MS_ISO_FILE
	$GEN_ISO $ARCH $SHELL $ENROLLER no-default $NOMS_ISO_FILE

	# We only build the variable templates for X64 and AARCH64
	if [ "$ARCH" == "X64" ]; then
		FLAVORS=${FLAVORS_X64[@]}
	elif [ "$ARCH" == "AARCH64" ]; then
		FLAVORS=${FLAVORS_AA64[@]}
	fi

	# Generate the varstore templates
	for flavor in ${FLAVORS[@]}; do
		for key in ${KEY_SOURCES[@]}; do
			build_template "$ARCH" "$flavor" "$key" \
				"${PKKEK[$key]}" "${KEY_ISO_FILES[$key]}" \
				"separate"
		done
	done

	if [ "$ARCH" == "X64" ]; then
		# Generate the unified firmware with preloaded keys for
		# backward compatibility. (bsc#1159793)
		for flavor in ${FLAVORS[@]}; do
			for key in ${KEY_SOURCES[@]}; do
				build_template "$ARCH" "$flavor" "$key" \
					"${PKKEK[$key]}" "${KEY_ISO_FILES[$key]}" \
					"unified"
			done
		done
	fi
}

# Generate the variable stores with default Secure Boot keys
generate_sb_var_templates X64
generate_sb_var_templates AARCH64

# Rename the x86_64 4MB firmware
#  We use ovmf-x86_64-$key-4m instead of ovmf-x86_64-4m-$key in the
#  version < stable201905. Rename the 4MB firmware files for backward
#  compatibility.
for key in ${KEY_SOURCES[@]}; do
	rename "4m-$key" "$key-4m" *"4m-$key"*.bin
done

%install
cp %{SOURCE2} README

sed -i s/'\r'// License.txt

# Install BaseTools
install -d %{buildroot}/%{_bindir}
install -m 0755 --strip BaseTools/Source/C/bin/EfiRom %{buildroot}/%{_bindir}

# Replace @DATADIR@ in the firmware descriptors
sed -i "s:@DATADIR@:%{_datadir}/qemu:" descriptors/*.json

tr -d '\r' < OvmfPkg/License.txt > License-ovmf.txt

install -m 0644 -D ovmf-*.bin -t %{buildroot}/%{_datadir}/qemu/
install -m 0644 -D qemu-uefi-*.bin -t %{buildroot}/%{_datadir}/qemu/
install -m 0644 -D aavmf-*.bin -t %{buildroot}/%{_datadir}/qemu/
install -m 0644 -D descriptors/*.json \
	-t %{buildroot}/%{_datadir}/qemu/firmware
%fdupes %{buildroot}/%{_datadir}/qemu/

%ifarch x86_64
# Install debug symbols, gdb-uefi.py
install -d %{buildroot}/%{_datadir}/ovmf-x86_64/
install -m 0644 gdb_uefi-*.py %{buildroot}/%{_datadir}/ovmf-x86_64/
mkdir -p %{buildroot}%{_prefix}/lib/debug
mv debug/ovmf-x86_64* %{buildroot}%{_prefix}/lib/debug
%fdupes %{buildroot}%{_prefix}/lib/debug/ovmf-x86_64*
mkdir -p %{buildroot}%{_prefix}/src/debug
mv source/ovmf-x86_64* %{buildroot}%{_prefix}/src/debug
%fdupes -s %{buildroot}%{_prefix}/src/debug/ovmf-x86_64
%endif

# Install Secure Boot key enroller
mkdir -p %{buildroot}/%{_datadir}/ovmf/
install -m 0755 %{SOURCE102} %{buildroot}/%{_datadir}/ovmf/
%ifarch x86_64
install -m 0644 X64/*.efi %{buildroot}/%{_datadir}/ovmf/
%endif
%ifarch aarch64
install -m 0644 AARCH64/*.efi %{buildroot}/%{_datadir}/ovmf/
%endif

%files
%doc README
%dir %{_datadir}/ovmf/
%{_datadir}/ovmf/*.efi
%{_datadir}/ovmf/*.sh

%files tools
%doc BaseTools/UserManuals/EfiRom_Utility_Man_Page.rtf
%{_bindir}/EfiRom

%files -n qemu-ovmf-ia32
%license License.txt License-ovmf.txt
%dir %{_datadir}/qemu/
%{_datadir}/qemu/ovmf-ia32*.bin
%dir %{_datadir}/qemu/firmware
%{_datadir}/qemu/firmware/*-ia32*.json

%files -n qemu-ovmf-x86_64
%license License.txt License-ovmf.txt
%dir %{_datadir}/qemu/
%{_datadir}/qemu/ovmf-x86_64*.bin
%dir %{_datadir}/qemu/firmware
%{_datadir}/qemu/firmware/*-x86_64*.json

%ifarch x86_64
%files -n qemu-ovmf-x86_64-debug
%{_datadir}/ovmf-x86_64/
%dir %{_prefix}/lib/debug/
%{_prefix}/lib/debug/ovmf-x86_64*
%dir %{_prefix}/src/debug/
%{_prefix}/src/debug/ovmf-x86_64*
%endif

%files -n qemu-uefi-aarch64
%license License.txt
%dir %{_datadir}/qemu/
%{_datadir}/qemu/qemu-uefi-aarch64*.bin
%{_datadir}/qemu/aavmf-aarch64-*code.bin
%{_datadir}/qemu/aavmf-aarch64-*vars.bin
%dir %{_datadir}/qemu/firmware
%{_datadir}/qemu/firmware/*-aarch64*.json

%files -n qemu-uefi-aarch32
%license License.txt
%dir %{_datadir}/qemu/
%{_datadir}/qemu/qemu-uefi-aarch32.bin
%{_datadir}/qemu/aavmf-aarch32-code.bin
%{_datadir}/qemu/aavmf-aarch32-vars.bin
%dir %{_datadir}/qemu/firmware
%{_datadir}/qemu/firmware/*-aarch32*.json

%changelog
