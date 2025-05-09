#
# spec file for package soapy-osmo
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017-2021, Martin Hauke <mardnh@gmx.de>
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


%bcond_with mod_freesrp
#
%define sover 0
%define soapy_modver 0.8-3
Name:           soapy-osmo
Version:        0.2.5
Release:        0
Summary:        Soapy SDR plugins for Osmo supported SDR devices
License:        GPL-3.0-only
URL:            https://github.com/pothosware/SoapyOsmo/wiki
#Git-Clone:     https://github.com/pothosware/SoapyOsmo.git
Source:         https://github.com/pothosware/SoapyOsmo/archive/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         soapy_osmosdr_rfspace_disable.patch
BuildRequires:  cmake >= 3.5
%if 0%{with mod_freesrp}
BuildRequires:  freesrp-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(libmirisdr)
BuildRequires:  pkgconfig(libosmosdr)

%description
Soapy Osmo - Osmo SDR module
Soapy SDR plugins for OsmoSDR devices

%package -n libSoapyOsmoSDR%{sover}
Summary:        Soapy SDR plugins for Osmo supported SDR devices

%description -n libSoapyOsmoSDR%{sover}
Soapy Osmo - Osmo SDR module
Soapy SDR plugins for OsmoSDR devices

%package devel
Summary:        Development files for the SoapyOsmoSDR library
Requires:       libSoapyOsmoSDR%{sover} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of libSoapyOsmoSDR.

%package -n soapysdr%{soapy_modver}-module-mirisdr
Summary:        SoapySDR mirisdr module

%description -n soapysdr%{soapy_modver}-module-mirisdr
Soapy mirisdr - mirisdr device support for Soapy SDR.
A Soapy module that supports Mirics SDR devices within the Soapy API.

%package -n soapysdr%{soapy_modver}-module-osmosdr
Summary:        SoapySDR osmosdr module

%description -n soapysdr%{soapy_modver}-module-osmosdr
Soapy OsmoSDR - OsmoSDR device support for Soapy SDR.
A Soapy module that supports OsmoSDR devices within the Soapy API.

%if 0%{with mod_freesrp}
%package -n soapysdr%{soapy_modver}-module-freesrp
Summary:        FreeSRP osmosdr module

%description -n soapysdr%{soapy_modver}-module-freesrp
Soapy FreeSRP - FreeSRP device support for Soapy SDR.
A Soapy module that supports FreeSRP devices within the Soapy API.
%endif

%prep
%autosetup -p1 -n SoapyOsmo-%{name}-%{version}

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install

%check
%ctest

%post   -n libSoapyOsmoSDR%{sover} -p /sbin/ldconfig
%postun -n libSoapyOsmoSDR%{sover} -p /sbin/ldconfig

%files -n libSoapyOsmoSDR%{sover}
%license COPYING
%doc Changelog.txt README.md
%{_libdir}/libSoapyOsmoSDR.so.*

%files devel
%{_libdir}/libSoapyOsmoSDR.so

%files -n soapysdr%{soapy_modver}-module-mirisdr
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libmiriSupport.so

%files -n soapysdr%{soapy_modver}-module-osmosdr
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libosmosdrSupport.so

%if 0%{with mod_freesrp}
%files -n soapysdr%{soapy_modver}-module-freesrp
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libfreesrpSupport.so
%endif

%changelog
