#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define platform @BUILD_FLAVOR@%{nil}
%define edk2_platforms_version 0.0~20230118T162833~201514e6
%define edk2_non_osi_version 0.0~20230118T154213~bc0b6bf
%define brotli_version 0.0~20220110T130810~f4153a0
%global openssl_version 1.1.1s

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
%define archive_version 202211

%if "%{platform}" != "%{nil}"
Name:           edk2-%{platform}
%else
Name:           edk2
%endif
Version:        0.0~20230118T162833~201514e6
Release:        0
Summary:        Firmware required to run the %{platform}
License:        SUSE-Firmware
Group:          System/Boot
URL:            https://github.com/tianocore/edk2
Source0:        https://github.com/tianocore/edk2/archive/edk2-stable%{archive_version}.tar.gz
Source1:        edk2-platforms-%{edk2_platforms_version}.tar.xz
Source2:        edk2-non-osi-%{edk2_non_osi_version}.tar.xz
Source3:        brotli-%{brotli_version}.tar.xz
Source10:       https://www.openssl.org/source/openssl-%{openssl_version}.tar.gz
Source11:       https://www.openssl.org/source/openssl-%{openssl_version}.tar.gz.asc
Source12:       openssl.keyring
Patch999:       edk2-platforms-fix-Hikeys.patch
#!BuildIgnore:  gcc-PIE
%if "%{platform}" != "hikey" && "%{platform}" != "hikey960"
BuildRequires:  acpica
%endif
BuildRequires:  bc
BuildRequires:  dos2unix
%if "%{platform}" == "Armada80x0McBin"
BuildRequires:  dtc
%endif
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  python
BuildRequires:  python3
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if "%{platform}" == ""
ExclusiveArch:  do_not_build
%else
ExclusiveArch:  aarch64
%endif

%description
Firmware required to run the %{platform}

%prep
%setup -q -n edk2-edk2-stable%{archive_version} -a 1 -a 2 -a 3
pushd edk2-platforms-%{edk2_platforms_version}
%patch999 -p1
popd

# Fix path of the brotli submodules
cp -R brotli-%{brotli_version}/* BaseTools/Source/C/BrotliCompress/brotli/
cp -R brotli-%{brotli_version}/* MdeModulePkg/Library/BrotliCustomDecompressLib/brotli/

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
%if "%{platform}" == "hikey"
DSC_PATH="edk2-platforms/Platform/Hisilicon/HiKey/HiKey.dsc"
%endif
%if "%{platform}" == "hikey960"
DSC_PATH="edk2-platforms/Platform/Hisilicon/HiKey960/HiKey960.dsc"
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
%if "%{platform}" == "Overdrive1000Board"
DSC_PATH="edk2-platforms/Platform/SoftIron/Overdrive1000Board/Overdrive1000Board.dsc"
%endif
%if "%{platform}" == "SbsaQemu"
DSC_PATH="edk2-platforms/Platform/Qemu/SbsaQemu/SbsaQemu.dsc"
%endif
BUILD_OPTIONS="-a AARCH64 -p $DSC_PATH -b %{build_mode} -t GCC5 %{?jobs:-n %jobs}"
# BaseTools does not support parallel builds, so no -jN here
ARCH=AARCH64 make -C BaseTools BUILD_CC=gcc BUILD_CXX=g++ BUILD_AS=gcc

. ./edksetup.sh

build $BUILD_OPTIONS

%install
# default outdir
%define outdir Build/%{platform}/%{build_mode}_GCC5
%if "%{platform}" == "hikey"
%if %{with edk2_non_osi}
install -D -m 0644 edk2-non-osi/Platform/Hisilicon/HiKey/mcuimage.bin %{buildroot}/boot/mcuimage.bin
%endif
%define outdir Build/HiKey/%{build_mode}_GCC5
%define fd_file BL33_AP_UEFI.fd
%endif
%if "%{platform}" == "hikey960"
%if %{with edk2_non_osi}
install -D -m 0644 edk2-non-osi/Platform/Hisilicon/HiKey960/lpm3.img %{buildroot}/boot/lpm3.img
%endif
%define outdir Build/HiKey960/%{build_mode}_GCC5
%define fd_file BL33_AP_UEFI.fd
%endif
%if "%{platform}" == "Armada80x0McBin"
%define outdir Build/Armada80x0McBin-AARCH64/%{build_mode}_GCC5
%define fd_file ARMADA_EFI.fd
%endif
%if "%{platform}" == "Overdrive1000Board"
%define outdir Build/Overdrive1000/%{build_mode}_GCC5
%define fd_file OVERDRIVE1000_ROM.fd
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

find %{outdir} -name *.fd

pushd %{outdir}/FV
for file in %{fd_file}; do
  install -D -m 0644 $file %{buildroot}/boot/$file
done
popd

%files
%defattr(-,root,root)
%if %{with edk2_non_osi}
%if "%{platform}" == "hikey"
/boot/mcuimage.bin
%endif
%if "%{platform}" == "hikey960"
/boot/lpm3.img
%endif
%endif
/boot/*.fd

%changelog
