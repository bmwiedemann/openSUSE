#
# spec file for package libwps
#
# Copyright (c) 2022 SUSE LLC
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
%define libname libwps-0_4-4
Name:           libwps
Version:        0.4.13
Release:        0
Summary:        Library for the Microsoft Works text and spreadsheet formats
License:        LGPL-2.1-or-later AND MPL-2.0
URL:            https://libwps.sourceforge.io/
Source:         https://downloads.sourceforge.net/project/libwps/libwps/libwps-%{version}/libwps-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(librevenge-0.0)
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
libwps is a library for importing the Microsoft Works word processor
and spreadsheet file format.

%package -n %{libname}
Summary:        Library for the Microsoft Works text and spreadsheet formats

%description -n %{libname}
libwps is a library for importing the Microsoft Works word processor
and spreadsheet file format.

%package devel
Summary:        Files for Developing with libwps
Requires:       %{libname} = %{version}

%description devel
libwps is a library for importing the Microsoft Works word processor
and spreadsheet file format.

This package contains the libwps development files.

%package tools
Summary:        Tools for converting the Microsoft Works text and spreadsheet formats

%description tools
Tools to work with the Microsoft Works word processor and spreadsheet
file format, based on libwps.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
	--disable-silent-rules \
	--disable-werror \
	--disable-static \
	--docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_docdir}/%{name}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING.LGPL COPYING.MPL
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libwps*.pc
%{_includedir}/libwps-*

%files tools
%{_bindir}/*
%doc %dir %{_docdir}/%{name}
%doc ChangeLog CREDITS NEWS

%changelog
