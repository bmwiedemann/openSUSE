#
# spec file for package ovmf
#
# Copyright (c) 2025 SUSE LLC
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
%global openssl_version 3.0.15
%global softfloat_version b64af41c3276f
%if 0%{?suse_version} < 1599
%bcond_with build_riscv64
%else
%bcond_without build_riscv64
%endif

Name:           ovmf
Version:        202411
Release:        0
Summary:        Open Virtual Machine Firmware
License:        BSD-2-Clause-Patent
Group:          System/Emulators/PC
URL:            https://github.com/tianocore/edk2
Source0:        edk2-edk2-stable%{version}.tar.gz
Source1:        https://www.openssl.org/source/old/3.0/openssl-%{openssl_version}.tar.gz
Source111:      https://www.openssl.org/source/old/3.0/openssl-%{openssl_version}.tar.gz.asc
Source112:      openssl.keyring
Source113:      openssl.keyring.README
Source114:      descriptors.tar.xz.README
Source2:        README
Source3:        SLES-UEFI-CA-Certificate-2048.crt
Source4:        openSUSE-UEFI-CA-Certificate-2048.crt
# berkeley-softfloat-3: https://github.com/ucb-bar/berkeley-softfloat-3
Source6:        berkeley-softfloat-3-%{softfloat_version}.tar.xz
Source7:        descriptors.tar.xz
# oniguruma: https://github.com/kkos/oniguruma,  "src" directory only
Source8:        oniguruma-v6.9.4_mark1-src.tar.xz
# public-mipi-sys-t: https://github.com/MIPI-Alliance/public-mipi-sys-t
Source9:        public-mipi-sys-t-1.1-edk2.tar.gz
# mbedtls: https://github.com/Mbed-TLS/mbedtls
Source10:       mbedtls-3.3.0.tar.gz
# brotli: https://github.com/google/brotli
Source11:       brotli-f4153a09f87cbb9c826d8fc12c74642bb2d879ea.tar.gz
# libspdm: https://github.com/DMTF/libspdm.git
Source12:       libspdm-50924a4c8145fc721e17208f55814d2b38766fe6.tar.gz
# pylibfdt: https://github.com/devicetree-org/pylibfdt
Source13:       pylibfdt-cfff805481bdea27f900c32698171286542b8d3c.tar.gz
Source100:      %{name}-rpmlintrc
Source101:      gdb_uefi.py.in
Patch1:         %{name}-gdb-symbols.patch
Patch2:         %{name}-pie.patch
Patch3:         %{name}-disable-ia32-firmware-piepic.patch
Patch6:         %{name}-ignore-spurious-GCC-12-warning.patch
# Bug 1205978 - Got Page-Fault exception when VM is booting with edk2-stable202211 ovmf
Patch7:         %{name}-Revert-OvmfPkg-PlatformInitLib-dynamic-mmio-window-s.patch
# Bug 1207095 - ASSERT [ArmCpuDxe] /home/abuild/rpmbuild/BUILD/edk2-edk2-stable202211/ArmPkg/Library/DefaultExceptionHandlerLib/AArch64/DefaultExceptionHandler.c(333): ((BOOLEAN)(0==1))
Patch8:         %{name}-Revert-ArmVirtPkg-make-EFI_LOADER_DATA-non-executabl.patch
# Bug 1205613 - L3: win 2k22 UEFI xen VMs cannot boot in xen after upgrade
Patch9:         %{name}-Revert-OvmfPkg-OvmfXen-Set-PcdFSBClock.patch
# Bug 1236009 - Build failure on Leap 15.5/15.6 due to unsupported GCC flag -mstack-protector-guard for aarch64 cross-compiler
Patch10:        %{name}-Revert-Add-Stack-Cookie-Support-to-MSVC-and-GCC.patch

%ifarch x86_64
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} <= 150700
Patch11:        %{name}-BaseTools-Using-gcc12-for-building-image.patch
%endif
%endif
BuildRequires:  bc
BuildRequires:  cross-arm-binutils
BuildRequires:  cross-arm-gcc%{gcc_version}
BuildRequires:  dosfstools
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
%ifarch x86_64
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} <= 150700
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%endif
%endif
BuildRequires:  iasl
BuildRequires:  libbpf1
BuildRequires:  libuuid-devel
BuildRequires:  mkisofs
BuildRequires:  mtools
BuildRequires:  nasm
BuildRequires:  openssl
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  virt-firmware
%ifnarch aarch64
BuildRequires:  cross-aarch64-binutils
BuildRequires:  cross-aarch64-gcc%{gcc_version}
%endif
%ifnarch x86_64
BuildRequires:  cross-x86_64-binutils
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} <= 150700
BuildRequires:  cross-x86_64-gcc12
%else
BuildRequires:  cross-x86_64-gcc%{gcc_version}
%endif
%endif
%ifnarch riscv64
%if %{with build_riscv64}
BuildRequires:  cross-riscv64-binutils
BuildRequires:  cross-riscv64-gcc%{gcc_version}
%endif
%endif
# Only build on the architectures with
#  1. cross-compilers, 2. iasl
ExclusiveArch:  x86_64 aarch64 riscv64

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

%if %{with build_riscv64}
%package -n qemu-uefi-riscv64
Summary:        UEFI QEMU rom image (RISC-V 64)
Group:          System/Emulators/PC
BuildArch:      noarch

%description -n qemu-uefi-riscv64
This package contains the UEFI rom image (RISC-V 64) for QEMU
virt board.
%endif

%prep
%setup -q -n edk2-edk2-stable%{version}

# bsc#973038 Remove the packages we don't need to avoid any potential
# license issue.
PKG_TO_REMOVE="EmulatorPkg"
rm -rf $PKG_TO_REMOVE

%autopatch -p1

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

# add public-mipi-sys-t
pushd MdePkg/Library/MipiSysTLib/mipisyst
tar -xf %{SOURCE9} --strip 1
popd

# add mbedtls
pushd CryptoPkg/Library/MbedTlsLib/mbedtls
tar -xf %{SOURCE10} --strip 1
popd

# add brotli
pushd BaseTools/Source/C/BrotliCompress/brotli
tar -xf %{SOURCE11} --strip 1
popd
pushd MdeModulePkg/Library/BrotliCustomDecompressLib/brotli
tar -xf %{SOURCE11} --strip 1
popd

# add libspdm
pushd SecurityPkg/DeviceSecurity/SpdmLib/libspdm
tar -xf %{SOURCE12} --strip 1
popd

# add libfdt
pushd MdePkg/Library/BaseFdtLib/libfdt
tar -xf %{SOURCE13} --strip 1
popd

%build

# Enable python3 build
export PYTHON3_ENABLE=TRUE
export PYTHON_COMMAND=python3

# For some reason ARM still uses TPM2_CONFIG_ENABLE
OVMF_FLAGS=" \
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
	-D SECURE_BOOT_ENABLE \
	-D BUILD_SHELL=FALSE \
	-a IA32 \
	-p OvmfPkg/OvmfPkgIa32.dsc \
	-b DEBUG \
	-t $TOOL_CHAIN \
"

# Flavors for x86_64: 2MB, 4MB, 4MB+SMM and AMD SEV
FLAVORS_X64=("ovmf-x86_64" "ovmf-x86_64-4m" "ovmf-x86_64-smm" "ovmf-x86_64-sev")
# Flavors will NOT enroll default kek/db keys
FLAVORS_X64_SKIP_SB_KEY=("ovmf-x86_64-sev")
# Flavors only support unified image (no separate *-code/-vars files)
FLAVORS_X64_UNIFIED_ONLY=("")
BUILD_OPTIONS_X64=" \
	$OVMF_FLAGS \
	-D BUILD_SHELL=FALSE \
	-a X64 \
	-b DEBUG \
	-t $TOOL_CHAIN \
"

# Flavors for aarch64
FLAVORS_AA64=("aavmf-aarch64")
BUILD_OPTIONS_AA64=" \
	$OVMF_FLAGS \
	-D SECURE_BOOT_ENABLE \
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
%if %{with build_riscv64}
# Flavors for riscv
FLAVORS_RV64=("riscv")
BUILD_OPTIONS_RV64=" \
	$OVMF_FLAGS \
	-D SECURE_BOOT_ENABLE \
	-a RISCV64 \
	-p OvmfPkg/RiscVVirt/RiscVVirtQemu.dsc \
	-b DEBUG \
	-t $TOOL_CHAIN \
"
%endif

# Build BaseTools
%ifarch x86_64
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} <= 150700
echo "gcc_version="`gcc -dumpversion`
export CC=gcc-12
export CXX=g++-12
%endif
	make -C BaseTools
%endif
%ifarch aarch64
	ARCH=AARCH64 make -C BaseTools
%endif
%ifarch riscv64
	ARCH=RISCV64 make -C BaseTools
%endif

# Import the build functions
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
	[ovmf-x86_64]="-p OvmfPkg/OvmfPkgX64.dsc -D FD_SIZE_2MB -D SECURE_BOOT_ENABLE"
	[ovmf-x86_64-4m]="-p OvmfPkg/OvmfPkgX64.dsc -D FD_SIZE_4MB -D NETWORK_TLS_ENABLE -D SECURE_BOOT_ENABLE"
	[ovmf-x86_64-smm]="-a IA32 -p OvmfPkg/OvmfPkgIa32X64.dsc -D FD_SIZE_4MB -D NETWORK_TLS_ENABLE -D SMM_REQUIRE -D SECURE_BOOT_ENABLE"
	[ovmf-x86_64-sev]="-p OvmfPkg/OvmfPkgX64.dsc -D FD_SIZE_4MB -D NETWORK_TLS_ENABLE"
)
declare -A OUTDIR_X64
OUTDIR_X64=(
	[ovmf-x86_64]="OvmfX64"
	[ovmf-x86_64-4m]="OvmfX64"
	[ovmf-x86_64-smm]="Ovmf3264"
	[ovmf-x86_64-sev]="OvmfX64"
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

# remove -code/-vars files for unfied only flavors
for flavor in ${FLAVORS_X64_UNIFIED_ONLY[@]}; do
	rm $flavor-code.bin
	rm $flavor-vars.bin
done

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
cp Build/ArmVirtQemu-AARCH64/DEBUG_GCC*/FV/QEMU_EFI.fd aavmf-aarch64-code.bin
truncate -s 64M aavmf-aarch64-code.bin
cp Build/ArmVirtQemu-AARCH64/DEBUG_GCC*/FV/QEMU_VARS.fd aavmf-aarch64-vars.bin
truncate -s 64M aavmf-aarch64-vars.bin

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
cp Build/ArmVirtQemu-ARM/DEBUG_GCC*/FV/QEMU_EFI.fd aavmf-aarch32-code.bin
truncate -s 64M aavmf-aarch32-code.bin
cp Build/ArmVirtQemu-ARM/DEBUG_GCC*/FV/QEMU_VARS.fd aavmf-aarch32-vars.bin
truncate -s 64M aavmf-aarch32-vars.bin

# Remove the temporary build files to reduce the disk usage (bsc#1178244)
rm -rf Build/ArmVirtQemu-ARM/

### Build RISCV64 UEFI Images ###
%if %{with build_riscv64}
%ifnarch riscv64
# Assign the cross-compiler prefix
export ${TOOL_CHAIN}_RISCV64_PREFIX="riscv64-suse-linux-"
%endif
# Build the UEFI image without keys
build $BUILD_OPTIONS_RV64

cp Build/RiscVVirtQemu/DEBUG_GCC*/FV/RISCV_VIRT_CODE.fd ovmf-riscv64-code.bin
truncate -s 32M ovmf-riscv64-code.bin
cp Build/RiscVVirtQemu/DEBUG_GCC*/FV/RISCV_VIRT_VARS.fd ovmf-riscv64-vars.bin
truncate -s 32M ovmf-riscv64-vars.bin

# Remove the temporary build files to reduce the disk usage (bsc#1178244)
rm -rf Build/RiscVVirtQemu/

%endif

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

	# We only build the variable templates for X64 and AARCH64
	if [ "$ARCH" == "X64" ]; then
		FLAVORS=${FLAVORS_X64[@]}
		# some flavors should NOT enroll default keys
		for skip in ${FLAVORS_X64_SKIP_SB_KEY[@]}; do
   			FLAVORS=("${FLAVORS[@]/$skip}")
		done
	elif [ "$ARCH" == "AARCH64" ]; then
		FLAVORS=${FLAVORS_AA64[@]}
	fi

	# Generate the varstore templates
	for flavor in ${FLAVORS[@]}; do
		for key in ${KEY_SOURCES[@]}; do
			ln "${flavor}-code.bin" "${flavor}-${key}-code.bin"

			if [ "$key" == "ms" ]; then
				virt-fw-vars --secure-boot --enroll-cert "${PKKEK[$key]}" -i "${flavor}-vars.bin" -o "${flavor}-${key}-vars.bin"
			else
				# GUID of EnrollDefaultKeys.efi, already used by virt-fw-vars for PK and KEK
				virt-fw-vars --secure-boot --enroll-cert "${PKKEK[$key]}" -i "${flavor}-vars.bin" -o "${flavor}-${key}-vars.bin" \
					     --no-microsoft --microsoft-kek none --add-db a0baa8a3-041d-48a8-bc87-c36d121b5e3d "${PKKEK[$key]}"
			fi
		done
	done

	if [ "$ARCH" == "X64" ]; then
		# Generate the unified firmware with preloaded keys for
		# backward compatibility. (bsc#1159793)
		for flavor in ${FLAVORS[@]}; do
			for key in ${KEY_SOURCES[@]}; do
				cat "${flavor}-${key}-vars.bin" "${flavor}-code.bin" > "${flavor}-${key}.bin"
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

%if %{without build_riscv64}
rm %{buildroot}%{_datadir}/qemu/firmware/*-riscv64*.json
%endif

%files
%doc README

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

%if %{with build_riscv64}
%files -n qemu-uefi-riscv64
%license License.txt
%dir %{_datadir}/qemu/
%{_datadir}/qemu/ovmf-riscv64-code.bin
%{_datadir}/qemu/ovmf-riscv64-vars.bin
%dir %{_datadir}/qemu/firmware
%{_datadir}/qemu/firmware/*-riscv64*.json
%endif

%changelog
