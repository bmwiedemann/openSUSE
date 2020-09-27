#
# spec file for package soapy-uhd
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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


%define soapy_modver 0.7
%define soapy_modname soapysdr%{soapy_modver}-module-uhd

Name:           soapy-uhd
Version:        0.4.1
Release:        0
Summary:        Soapy SDR plugins for UHD supported SDR devices
License:        GPL-3.0-only
Group:          Hardware/Other
URL:            https://github.com/pothosware/SoapyUHD/wiki
#Git-Clone:     https://github.com/pothosware/SoapyUHD.git
Source:         https://github.com/pothosware/SoapyUHD/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(uhd)
%if 0%{?suse_version} > 1500
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%endif

%description
Soapy UHD - Soapy SDR devices for UHD.
A UHD module that supports Soapy devices within the UHD API.

%package -n %{soapy_modname}
Summary:        Soapy SDR plugins for UHD supported SDR devices
Group:          System/Libraries

%description -n %{soapy_modname}
Soapy UHD - Soapy SDR devices for UHD.
A UHD module that supports Soapy devices within the UHD API.

%prep
%setup -q -n SoapyUHD-%{name}-%{version}

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install

%files -n %{soapy_modname}
%license COPYING
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libuhdSupport.so
%dir %{_libdir}/uhd
%dir %{_libdir}/uhd/modules
%{_libdir}/uhd/modules/libsoapySupport.so

%changelog
