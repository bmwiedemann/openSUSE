#
# spec file for package soapy-rtlsdr
#
# Copyright (c) 2025 SUSE LLC
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
%define soapy_modname soapysdr%{soapy_modver}-module-rtlsdr

Name:           soapy-rtlsdr
Version:        0.3.3
Release:        0
Summary:        SoapySDR RTL-SDR support module
License:        MIT
URL:            https://github.com/pothosware/SoapyRTLSDR/wiki
#Git-Clone:     https://github.com/pothosware/SoapyRTLSDR.git
Source:         https://github.com/pothosware/SoapyRTLSDR/archive/soapy-rtl-sdr-%{version}.tar.gz
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(librtlsdr)

%description
Soapy RTL-SDR - RTL-SDR device support for Soapy SDR.
A Soapy module that supports RTL-SDR devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR RTL-SDR support module

%description -n %{soapy_modname}
Soapy RTL-SDR - RTL-SDR device support for Soapy SDR.
A Soapy module that supports RTL-SDR devices within the Soapy API.

%prep
%setup -q -n SoapyRTLSDR-soapy-rtl-sdr-%{version}

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n %{soapy_modname}
%license LICENSE.txt
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/librtlsdrSupport.so

%changelog
