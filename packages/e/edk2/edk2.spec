#
# spec file for package edk2
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


%define platform @BUILD_FLAVOR@%{nil}
%define edk2_platforms_version 0.0~20250313T212503~fece0f1a
%define edk2_non_osi_version 0.0~20250211T163925~ea2040c
%define brotli_version 0.0~20220110T130810~f4153a0
%define cmocka_version 0.0~20191205T115639~1cc9cde
%define public_mipi_sys_t_version 0.0~20230315T074831~370b594
%define mbedtls_version 0.0~20221214T190639~8c892249
%define googletest_version 0.0~20220616T131832~86add13
%define libspdm_version 0.0~20241122T070402~98ef964
%global openssl_version 3.4.1

# Build with edk2-non-osi
%bcond_without edk2_non_osi

# Build in debug mode by default
%bcond_without edk2_debug
%if %{with edk2_debug}
%define build_mode DEBUG
%else
%define build_mode RELEASE
%endif

# This differs on RC
%define archive_version 202502

%if "%{platform}" != "%{nil}"
Name:           edk2-%{platform}
%else
Name:           edk2
%endif
Version:        202502
Release:        0
%if "%{platform}" == "Shell"
Summary:        Shell EFI application
%else
Summary:        Firmware required to run the %{platform}
%endif
License:        SUSE-Firmware
Group:          System/Boot
URL:            https://github.com/tianocore/edk2
Source0:        https://github.com/tianocore/edk2/archive/edk2-stable%{archive_version}.tar.gz
Source1:        edk2-platforms-%{edk2_platforms_version}.tar.xz
Source2:        edk2-non-osi-%{edk2_non_osi_version}.tar.xz
Source3:        brotli-%{brotli_version}.tar.xz
Source4:        edk2-cmocka-%{cmocka_version}.tar.xz
Source5:        public-mipi-sys-t-%{public_mipi_sys_t_version}.tar.xz
Source6:        mbedtls-%{mbedtls_version}.tar.xz
Source7:        googletest-%{googletest_version}.tar.xz
Source8:        libspdm-%{libspdm_version}.tar.xz
Source10:       https://www.openssl.org/source/openssl-%{openssl_version}.tar.gz
Source11:       https://www.openssl.org/source/openssl-%{openssl_version}.tar.gz.asc
Source12:       openssl.keyring
# PATCH-FIX-UPSTREAM - https://github.com/tianocore/edk2/pull/10928 - CVE-2024-38797
Patch1:         10928.patch
#!BuildIgnore:  gcc-PIE
BuildRequires:  acpica
BuildRequires:  bc
BuildRequires:  dos2unix
%if "%{platform}" == "Armada80x0McBin" || "%{platform}" == "SG2042"
BuildRequires:  dtc
%endif
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if "%{platform}" == "Shell"
BuildRequires:  nasm
BuildRequires:  pesign-obs-integration
%endif
BuildRequires:  libuuid-devel
BuildRequires:  python3
BuildRequires:  unzip
%if "%{platform}" == ""
ExclusiveArch:  do_not_build
%elif "%{platform}" == "Shell"
ExcludeArch:    ppc %power64
%elif "%{platform}" == "SG2042"
ExclusiveArch:  riscv64
%else
ExclusiveArch:  aarch64
%endif

%ifarch %ix86
%define ARCH IA32
%elifarch x86_64
%define ARCH X64
%elifarch %arm
%define ARCH ARM
%elifarch aarch64
%define ARCH AARCH64
%elifarch riscv64
%define ARCH RISCV64
%elifarch loongarch64
%define ARCH LOONGARCH64
%endif

%description
%if "%{platform}" == "Shell"
The UEFI 2.0 shell provides a standard pre-boot command line processor.
%else
Firmware required to run the %{platform}
%endif

%prep
%setup -q -n edk2-edk2-stable%{archive_version} -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8
%patch -P 1 -p1

# Fix path of the brotli submodules
cp -R brotli-%{brotli_version}/* BaseTools/Source/C/BrotliCompress/brotli/
cp -R brotli-%{brotli_version}/* MdeModulePkg/Library/BrotliCustomDecompressLib/brotli/
# Fix path for cmocka
cp -R edk2-cmocka-%{cmocka_version}/* UnitTestFrameworkPkg/Library/CmockaLib/cmocka/
# Fix path for public-mipi-sys-t
cp -R public-mipi-sys-t-%{public_mipi_sys_t_version}/* MdePkg/Library/MipiSysTLib/mipisyst/
# Fix path for mbedtls
cp -R mbedtls-%{mbedtls_version}/* CryptoPkg/Library/MbedTlsLib/mbedtls/
# Fix path for googletest
cp -R googletest-%{googletest_version}/* UnitTestFrameworkPkg/Library/GoogleTestLib/googletest/
# Fix path for libspdm
cp -R libspdm-%{libspdm_version}/* SecurityPkg/DeviceSecurity/SpdmLib/libspdm

ln -sf edk2-platforms-%{edk2_platforms_version} edk2-platforms
ln -sf edk2-non-osi-%{edk2_non_osi_version} edk2-non-osi

# add openssl
pushd CryptoPkg/Library/OpensslLib/openssl
tar -xf %{SOURCE10} --strip 1
popd

%build
%if %{with edk2_non_osi}
export PACKAGES_PATH=$PWD:$PWD/edk2-platforms:$PWD/edk2-platforms/Drivers:$PWD/edk2-non-osi
%else
export PACKAGES_PATH=$PWD:$PWD/edk2-platforms:$PWD/edk2-platforms/Drivers
%endif
export PYTHON_COMMAND=python3
%if "%{platform}" == "ArmVExpress-FVP-AArch64"
DSC_PATH="edk2-platforms/Platform/ARM/VExpressPkg/ArmVExpress-FVP-AArch64.dsc"
%endif
%if "%{platform}" == "Armada80x0McBin"
DSC_PATH="edk2-platforms/Platform/SolidRun/Armada80x0McBin/Armada80x0McBin.dsc"
%endif
%if "%{platform}" == "RPi3"
DSC_PATH="edk2-platforms/Platform/RaspberryPi/RPi3/RPi3.dsc"
%endif
%if "%{platform}" == "RPi4"
DSC_PATH="edk2-platforms/Platform/RaspberryPi/RPi4/RPi4.dsc"
%endif
%if "%{platform}" == "SbsaQemu"
DSC_PATH="edk2-platforms/Platform/Qemu/SbsaQemu/SbsaQemu.dsc"
%endif
%if "%{platform}" == "SG2042"
DSC_PATH="edk2-platforms/Platform/Sophgo/SG2042_EVB_Board/SG2042.dsc"
%endif
%if "%{platform}" == "Shell"
DSC_PATH="ShellPkg/ShellPkg.dsc"
%endif
BUILD_OPTIONS="-a %{ARCH} -p $DSC_PATH -b %{build_mode} -t GCC5 %{?jobs:-n %jobs}"
# BaseTools does not support parallel builds, so no -jN here
ARCH=%{ARCH} make -C BaseTools BUILD_CC=gcc BUILD_CXX=g++ BUILD_AS=gcc

. ./edksetup.sh

build $BUILD_OPTIONS

%install
# default outdir
%define outdir Build/%{platform}/%{build_mode}_GCC5
%if "%{platform}" == "ArmVExpress-FVP-AArch64"
%define fd_file FVP_AARCH64_EFI.fd
%endif
%if "%{platform}" == "Armada80x0McBin"
%define outdir Build/Armada80x0McBin-AARCH64/%{build_mode}_GCC5
%define fd_file ARMADA_EFI.fd
%endif
%if "%{platform}" == "RPi3"
%define fd_file RPI_EFI.fd
%endif
%if "%{platform}" == "RPi4"
%define fd_file RPI_EFI.fd
%endif
%if "%{platform}" == "SbsaQemu"
%define fd_file SBSA_FLASH[01].fd
truncate -s 256M %{outdir}/FV/%{fd_file}
%endif
%if "%{platform}" == "SG2042"
%define outdir Build/SG2042_EVB/%{build_mode}_GCC5
%define fd_file SG2042.fd
%endif

%if "%{platform}" == "Shell"
install -D -m 0644 %{outdir}/%{ARCH}/ShellPkg/Application/Shell/Shell/OUTPUT/Shell.efi %{buildroot}/usr/lib/edk2/Shell.efi

export BRP_PESIGN_FILES="*.efi"

%else
find %{outdir} -name *.fd

pushd %{outdir}/FV
for file in %{fd_file}; do
  install -D -m 0644 $file %{buildroot}/boot/$file
done
popd
%endif

%files
%if "%{platform}" == "Shell"
%dir %{_prefix}/lib/edk2
%{_prefix}/lib/edk2/Shell.efi
%else
/boot/*.fd
%endif

%changelog
