#
# spec file for package wxsqlite3
#
# Copyright (c) 2020 SUSE LLC
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


%define wx_version_pkgname %(wx-config --version | sed 's@^\\([^\\.]\\+\\.[^\\.]\\+\\)\\(.*\\)@\\1@;s@\\.@_@')
%define wx_version_soname  %(wx-config --version | sed 's@^\\([^\\.]\\+\\.[^\\.]\\+\\)\\(.*\\)@\\1@')
%define sover 0
Name:           wxsqlite3
Version:        4.6.1
Release:        0
Summary:        C++ wrapper around SQLite 3.x
License:        SUSE-wxWidgets-3.1
URL:            https://github.com/utelle/wxsqlite3
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
%if 0%{suse_version} > 1315
BuildRequires:  wxWidgets-devel >= 3
%else
BuildRequires:  wxWidgets-3_0-devel
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
%endif

%description
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database
and is specifically designed for use in programs based on the wxWidgets
library.

%package -n libwxcode_gtk2u_wxsqlite3-%{wx_version_pkgname}-%{sover}
Summary:        C++ wrapper around SQLite 3.x

%description -n libwxcode_gtk2u_wxsqlite3-%{wx_version_pkgname}-%{sover}
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database
and is specifically designed for use in programs based on the wxWidgets
library.

%package        devel
Summary:        C++ wrapper around SQLite 3.x - Development Files
Requires:       libwxcode_gtk2u_wxsqlite3-%{wx_version_pkgname}-%{sover} = %{version}

%description    devel
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database
and is specifically designed for use in programs based on the wxWidgets
library.

%prep
: wx_version_pkgname: %{wx_version_pkgname}
: wx_version_soname: %{wx_version_soname}
wx-config --version
%autosetup

%build
CFLAGS='%{optflags} -Wno-unused-but-set-variable -Wno-unused-variable -Wno-unused-function' 
CXXFLAGS="${CFLAGS}"
autoreconf -fi
%configure \
	--enable-shared \
	--disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libwxcode_gtk2u_wxsqlite3-%{wx_version_pkgname}-%{sover} -p /sbin/ldconfig
%postun -n libwxcode_gtk2u_wxsqlite3-%{wx_version_pkgname}-%{sover} -p /sbin/ldconfig

%files -n libwxcode_gtk2u_wxsqlite3-%{wx_version_pkgname}-%{sover}
%license LICENCE.txt
%doc readme.md
%{_libdir}/libwxcode_gtk2u_wxsqlite3-%{wx_version_soname}.so.%{sover}*

%files devel
%dir %{_includedir}/wx
%{_includedir}/wx/wxsqlite3.h
%{_includedir}/wx/wxsqlite3_version.h
%{_includedir}/wx/wxsqlite3def.h
%{_libdir}/libwxcode_gtk2u_wxsqlite3-%{wx_version_soname}.so
%{_libdir}/pkgconfig/wxsqlite3.pc

%changelog
