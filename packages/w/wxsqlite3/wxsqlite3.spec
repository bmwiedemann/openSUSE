#
# spec file for package wxsqlite3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define wx_version_soname %(wx-config --version | sed 's@^\\([^\\.]\\+\\.[^\\.]\\+\\)\\(.*\\)@\\1@;s@\\.@_@')
%define sover 0

Name:           wxsqlite3
Version:        3.5.8.20171102.1b93c9c
Release:        0
Summary:        C++ wrapper around SQLite 3.x
License:        SUSE-wxWidgets-3.1
Group:          Development/Libraries/C and C++
Url:            https://github.com/utelle/wxsqlite3
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
%if 0%{?is_opensuse}
BuildRequires:  wxWidgets-devel >= 3
%else
# SLE_12 lacks wxWidgets_3.0-devel
BuildRequires:  wxWidgets-devel < 3
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database
and is specifically designed for use in programs based on the wxWidgets
library.

%package -n libwxcode_gtk2u_wxsqlite3-%{wx_version_soname}-%{sover}
Summary:        C++ wrapper around SQLite 3.x
Group:          System/Libraries

%description -n libwxcode_gtk2u_wxsqlite3-%{wx_version_soname}-%{sover}
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database
and is specifically designed for use in programs based on the wxWidgets
library.

%package        devel
Summary:        C++ wrapper around SQLite 3.x - Development Files
Group:          Development/Libraries/C and C++
Requires:       libwxcode_gtk2u_wxsqlite3-%{wx_version_soname}-%{sover} = %{version}

%description    devel
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database
and is specifically designed for use in programs based on the wxWidgets
library.

%prep
: wx_version_soname: %{wx_version_soname}
wx-config --version
%setup -q

%build
export CFLAGS='%{optflags} -fno-strict-aliasing'
export CXXFLAGS='%{optflags} -fno-strict-aliasing'
autoreconf -fi
%configure \
	--enable-shared \
	--disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
find %{buildroot} -name "*.la" -print -delete

%post -n libwxcode_gtk2u_wxsqlite3-%{wx_version_soname}-%{sover} -p /sbin/ldconfig

%postun -n libwxcode_gtk2u_wxsqlite3-%{wx_version_soname}-%{sover} -p /sbin/ldconfig

%files -n libwxcode_gtk2u_wxsqlite3-%{wx_version_soname}-%{sover}
%defattr(-,root,root,-)
%doc LICENCE.txt readme.md
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/wx
%{_libdir}/*.so
%{_libdir}/pkgconfig

%changelog
