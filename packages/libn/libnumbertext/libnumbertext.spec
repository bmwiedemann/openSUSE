#
# spec file for package libnumbertext
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%define libname libnumbertext-1_0-0
Name:           libnumbertext
Version:        1.0.11
Release:        0
Summary:        Language-neutral NUMBERTEXT and MONEYTEXT functions
License:        MPL-2.0
URL:            https://github.com/Numbertext/libnumbertext
Source:         https://github.com/Numbertext/libnumbertext/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7-c++
%endif

%description
Language-neutral NUMBERTEXT and MONEYTEXT functions for LibreOffice Calc

%package -n %{libname}
Summary:        Language-neutral NUMBERTEXT and MONEYTEXT functions
Requires:       %{name}-data >= %{version}

%description -n %{libname}
Language-neutral NUMBERTEXT and MONEYTEXT functions for LibreOffice Calc

%package devel
Summary:        Files for Developing with libnumbertext
Requires:       %{libname} = %{version}

%description devel
Language-neutral NUMBERTEXT and MONEYTEXT functions for LibreOffice Calc

This package contains the libnumbertext development files.

%package tools
Summary:        Tools to work with NUMBERTEXT and MONEYTEXT functions
Requires:       %{name}-data >= %{version}

%description tools
This package contains tools to work with NUMBERTEXT and MONEYTEXT functions

%package data
Summary:        Language data for numbertext

%description data
This package contains data providing information for localized nubertext
conversions.

%prep
%setup -q

%build
autoreconf -fvi
%if 0%{?suse_version} < 1500
export CXX=g++-7
%endif
%configure \
	--disable-static \
	--disable-silent-rules \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# missing config.h header
install -m 0644 src/config.h %{buildroot}%{_includedir}/libnumbertext/config.h

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/*.so.*

%files devel
%dir %{_includedir}/libnumbertext
%{_includedir}/libnumbertext/*
%{_libdir}/libnumbertext-1.0.so
%{_libdir}/pkgconfig/libnumbertext.pc

%files tools
%{_bindir}/spellout

%files data
%dir %{_datadir}/libnumbertext
%{_datadir}/libnumbertext/*.sor

%changelog
