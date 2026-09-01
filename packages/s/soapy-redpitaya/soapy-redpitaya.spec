#
# spec file for package soapy-redpitaya
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define soapy_modver 0.8-3
%define soapy_modname soapysdr%{soapy_modver}-module-redpitaya
Name:           soapy-redpitaya
Version:        0.1.1
Release:        0
Summary:        SoapySDR RedPitaya module
License:        GPL-3.0-or-later
URL:            https://github.com/pothosware/SoapyRedPitaya/wiki
#Git-Clone:     https://github.com/pothosware/SoapyRedPitaya.git
Source:         https://github.com/pothosware/SoapyRedPitaya/archive/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-Update-for-compat-with-newer-CMake.patch pothosware/SoapyRedPitaya@0702140 -- cmake_minimum_required range form; cmake 4 rejects a bare pre-3.5 minimum
Patch0:         0001-Update-for-compat-with-newer-CMake.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(SoapySDR)

%description
Soapy RedPitaya - RedPitaya device support for Soapy SDR.
A Soapy module that supports RedPitaya devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR RedPitaya module
# soname dep pulls only libSoapySDR, which is what dlopens the module;
# require the package too so SoapySDRUtil is there to probe and use it
Requires:       soapy-sdr

%description -n %{soapy_modname}
Soapy RedPitaya - RedPitaya device support for Soapy SDR.
A Soapy module that supports RedPitaya devices within the Soapy API.

%prep
%autosetup -p1 -n SoapyRedPitaya-%{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n %{soapy_modname}
%license COPYING
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libRedPitaya.so

%changelog
