#
# spec file for package uefi-shell
#
# Copyright (c) 2026 SUSE LLC
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


%undefine _build_create_debug
%global openssl_version 3.5.1
%global softfloat_version b64af41c3276f
%if 0%{?suse_version} < 1599
%bcond_with build_riscv64
%else
%bcond_without build_riscv64
%endif

Name:           uefi-shell
Version:        202511
Release:        0
Summary:        UEFI Shell built from EDK II project
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
Source7:        descriptors.tar.xz
# oniguruma: https://github.com/kkos/oniguruma,  "src" directory only
Source8:        oniguruma-v6.9.4_mark1-src.tar.xz
# public-mipi-sys-t: https://github.com/MIPI-Alliance/public-mipi-sys-t
Source9:        public-mipi-sys-t-1.1-edk2.tar.gz
# mbedtls: https://github.com/Mbed-TLS/mbedtls
Source10:       mbedtls-3.3.0.tar.gz
# brotli: https://github.com/google/brotli
Source11:       brotli-e230f474b87134e8c6c85b630084c612057f253e.tar.gz
# libspdm: https://github.com/DMTF/libspdm.git
Source12:       libspdm-50924a4c8145fc721e17208f55814d2b38766fe6.tar.gz
# pylibfdt: https://github.com/devicetree-org/pylibfdt
Source13:       pylibfdt-cfff805481bdea27f900c32698171286542b8d3c.tar.gz
Source100:      ovmf-rpmlintrc
Source101:      gdb_uefi.py.in
Patch1:         ovmf-gdb-symbols.patch
Patch2:         ovmf-pie.patch
Patch3:         ovmf-disable-ia32-firmware-piepic.patch
# Bug 1236009 - Build failure on Leap 15.5/15.6 due to unsupported GCC flag -mstack-protector-guard for aarch64 cross-compiler
Patch10:        ovmf-Revert-Add-Stack-Cookie-Support-to-MSVC-and-GCC.patch
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
UEFI Shell for x86_64

%package -n uefi-shell-x86_64
Summary:        UEFI Shell for X86_64
Group:          System/Emulators/PC
BuildArch:      noarch

%description -n uefi-shell-x86_64
UEFI Shell for x86_64

%package -n uefi-shell-aarch64
Summary:        UEFI Shell for AARCH64
Group:          System/Emulators/PC
BuildArch:      noarch

%description -n uefi-shell-aarch64
UEFI Shell for AARCH64

%if %{with build_riscv64}
%package -n uefi-shell-riscv64
Summary:        UEFI Shell for RISCV64
Group:          System/Emulators/PC
BuildArch:      noarch

%description -n uefi-shell-riscv64
UEFI Shell for RISCV64
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

%if 0%{?suse_version} > 1320
TOOL_CHAIN=GCC5
%else
echo `gcc -dumpversion`
TOOL_CHAIN=GCC$(gcc -dumpversion|sed 's/\([0-9]\)\.\([0-9]\).*/\1\2/')
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

# Build Shell.efi for X64
%ifnarch x86_64
# Assign the cross-compiler prefix
export ${TOOL_CHAIN}_BIN="x86_64-suse-linux-"
%endif
build -a X64 -p ShellPkg/ShellPkg.dsc -t $TOOL_CHAIN
mkdir X64
cp Build/Shell/DEBUG_*/X64/ShellPkg/Application/Shell/Shell/DEBUG/Shell.efi X64

# Build Shell.efi for AARCH64
%ifnarch aarch64
# Assign the cross-compiler prefix
export ${TOOL_CHAIN}_AARCH64_PREFIX="aarch64-suse-linux-"
%endif
build -a AARCH64 -p ShellPkg/ShellPkg.dsc -t $TOOL_CHAIN
mkdir AARCH64
cp Build/Shell/DEBUG_*/AARCH64/ShellPkg/Application/Shell/Shell/DEBUG/Shell.efi AARCH64

# Build Shell.efi for RISCV64
%if %{with build_riscv64}
%ifnarch riscv64
# Assign the cross-compiler prefix
export ${TOOL_CHAIN}_RISCV64_PREFIX="riscv64-suse-linux-"
%endif
build -a RISCV64 -p ShellPkg/ShellPkg.dsc -t $TOOL_CHAIN
mkdir RISCV64
cp Build/Shell/DEBUG_*/RISCV64/ShellPkg/Application/Shell/Shell/DEBUG/Shell.efi RISCV64
%endif

%install
mkdir -p %{buildroot}/%{_datadir}/ovmf/
mkdir -p %{buildroot}%{_datadir}/ovmf/x86_64
install -m 0644 X64/Shell.efi %{buildroot}/%{_datadir}/ovmf/x86_64/Shell.efi
mkdir -p %{buildroot}%{_datadir}/ovmf/aarch64
install -m 0644 AARCH64/Shell.efi %{buildroot}/%{_datadir}/ovmf/aarch64/Shell.efi
%if %{with build_riscv64}
mkdir -p %{buildroot}%{_datadir}/ovmf/riscv64
install -m 0644 RISCV64/Shell.efi %{buildroot}/%{_datadir}/ovmf/riscv64/Shell.efi
%endif

%files -n uefi-shell-x86_64
%dir %{_datadir}/ovmf
%dir %{_datadir}/ovmf/x86_64
%{_datadir}/ovmf/x86_64/Shell.efi

%files -n uefi-shell-aarch64
%dir %{_datadir}/ovmf
%dir %{_datadir}/ovmf/aarch64
%{_datadir}/ovmf/aarch64/Shell.efi

%if %{with build_riscv64}
%files -n uefi-shell-riscv64
%dir %{_datadir}/ovmf
%dir %{_datadir}/ovmf/riscv64
%{_datadir}/ovmf/riscv64/Shell.efi
%endif

%changelog
