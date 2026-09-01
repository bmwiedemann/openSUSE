#
# spec file for package soapy-fcdpp
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# SOAPY_SDR_ABI_VERSION; the module dir is ABI-keyed, so this must track soapy-sdr
%define soapy_modver 0.8-3
%define soapy_modname soapysdr%{soapy_modver}-module-fcdpp
Name:           soapy-fcdpp
# Keep in sync with _service; upstream last tagged 0.1.1 in 2019
Version:        0.2.0~git20251009.1ae85f0
Release:        0
Summary:        SoapySDR FUNcube Dongle Pro+ module
# Legal-Review-Notice: BSL-1.0 covers the whole tree. fcd.c/fcd.h carry only
# Xcode's "All rights reserved" template boilerplate from the same author;
# LICENSE_1_0.txt, debian/copyright (Files: *) and the SPDX-License-Identifier
# headers on the remaining sources all say Boost. The previous MIT tag was wrong.
License:        BSL-1.0
URL:            https://github.com/pothosware/SoapyFCDPP/wiki
#Git-Clone:     https://github.com/pothosware/SoapyFCDPP.git
Source:         %{name}-%{version}.tar.zst
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR) >= 0.8
BuildRequires:  pkgconfig(alsa)
# FindHIDAPI.cmake find_library()s hidapi-libusb; hidraw is never linked
BuildRequires:  pkgconfig(hidapi-libusb)

%description
Soapy FCDPP - FUNcube Dongle Pro+ device support for Soapy SDR.
A Soapy module that supports FUNcube Dongle Pro+ and Pro (V1.x) devices
within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR FUNcube Dongle Pro+ module
# soname dep pulls only libSoapySDR, which is what dlopens the module;
# require the package too so SoapySDRUtil is there to probe and use it
Requires:       soapy-sdr

%description -n %{soapy_modname}
Soapy FCDPP - FUNcube Dongle Pro+ device support for Soapy SDR.
A Soapy module that supports FUNcube Dongle Pro+ and Pro (V1.x) devices
within the Soapy API.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
# upstream's cmake_minimum_required is 2.8.12; cmake >= 4 needs the policy
# floor that the distro %%cmake macro already injects
%cmake
%cmake_build

%install
%cmake_install

%files -n %{soapy_modname}
%license LICENSE_1_0.txt
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libFCDPPSupport.so

%changelog
