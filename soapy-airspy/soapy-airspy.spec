#
# spec file for package soapy-airspy
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define soapy_modver 0.7
%define soapy_modname soapysdr%{soapy_modver}-module-airspy
Name:           soapy-airspy
Version:        0.1.2
Release:        0
Summary:        SoapySDR Airspy module
License:        MIT
Group:          Hardware/Other
Url:            https://github.com/pothosware/SoapyAirspy/wiki
#Git-Clone:     https://github.com/pothosware/SoapyAirspy.git
Source:         https://github.com/pothosware/SoapyAirspy/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(libairspy)

%description
Soapy Airspy - Airspy device support for Soapy SDR.
A Soapy module that supports Airspy devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR Airspy module
Group:          System/Libraries

%description -n %{soapy_modname}
Soapy Airspy - Airspy device support for Soapy SDR.
A Soapy module that supports Airspy devices within the Soapy API.

%prep
%setup -q -n SoapyAirspy-%{name}-%{version}

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install

%files -n %{soapy_modname}
%license LICENSE.txt
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libairspySupport.so

%changelog
