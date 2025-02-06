#
# spec file for package soapy-bladerf
#
# Copyright (c) 2025, SUSE LLC
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define soapy_modver 0.8
%define soapy_modname soapysdr%{soapy_modver}-module-bladerf

Name:           soapy-bladerf
Version:        0.4.2
Release:        0
Summary:        SoapySDR BladeRF module
License:        LGPL-2.1
Group:          Hardware/Other
Url:            https://github.com/pothosware/SoapyBladeRF/wiki
#Git-Clone:     https://github.com/pothosware/SoapyBladeRF.git
Source:         https://github.com/pothosware/SoapyBladeRF/archive/%{name}-%{version}.tar.gz#/SoapyBladeRF-%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  soapy-sdr-devel
BuildRequires:  bladeRF-devel

%description
Soapy BladeRF - BladeRF device support for Soapy SDR.
A Soapy module that supports BladeRF devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR BladeRF module
Group:          System/Libraries

%description -n %{soapy_modname}
Soapy BladeRF - BladeRF device support for Soapy SDR.
A Soapy module that supports BladeRF devices within the Soapy API.

%prep
%setup -q -n SoapyBladeRF-%{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check

%files -n %{soapy_modname}
%license LICENSE.LGPLv2.1
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libbladeRFSupport.so

%changelog
