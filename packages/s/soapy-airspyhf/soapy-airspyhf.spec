#
# spec file for package soapy-airspyhf
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


# SoapySDR module ABI; must track soapy-sdr's %%sover (modules<ver> install dir)
%define soapy_modver 0.8-3
%define soapy_modname soapysdr%{soapy_modver}-module-airspyhf
Name:           soapy-airspyhf
Version:        0.2.0+git20251009.7457d69
Release:        0
Summary:        SoapySDR AirspyHF+ module
License:        MIT
URL:            https://github.com/pothosware/SoapyAirspyHF
Source:         %{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# CMakeLists.txt: find_package(SoapySDR "0.4.0" NO_MODULE REQUIRED)
BuildRequires:  pkgconfig(SoapySDR) >= 0.4.0
BuildRequires:  pkgconfig(libairspyhf)

%description
Soapy AirspyHF - AirspyHF+ device support for Soapy SDR.
A Soapy module that supports AirspyHF+ devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR AirspyHF+ module
# soname dep pulls only libSoapySDR, which is what dlopens the module;
# require the package too so SoapySDRUtil is there to probe and use it
Requires:       soapy-sdr

%description -n %{soapy_modname}
Soapy AirspyHF - AirspyHF+ device support for Soapy SDR.
A Soapy module that supports AirspyHF+ devices within the Soapy API.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n %{soapy_modname}
%license LICENSE.txt
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libairspyhfSupport.so

%changelog
