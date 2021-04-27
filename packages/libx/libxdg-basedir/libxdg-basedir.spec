# vim: set sw=4 ts=4 et:
#
# spec file for package libxdg-basedir
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

%define soname 1
Name:           libxdg-basedir
Version:        1.2.2
Release:        0
Summary:        XDG Base Directory Specification Library
License:        MIT
Group:          System/Libraries
URL:            https://github.com/davmac314/libxdg-basedir
Source:         https://github.com/davmac314/libxdg-basedir/releases/download/v%{version}/libxdg-basedir-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files

%description
The XDG Base Directory Specification defines where should user files be looked
for by defining one or more base directories relative in with they should be
located.

This library implements functions to list the directories according to the
specification and provides a few higher-level functions.

%package -n %{name}%{soname}
Summary:        XDG Base Directory Specification Library
Group:          System/Libraries

%description -n %{name}%{soname}
The XDG Base Directory Specification defines where should user files be looked
for by defining one or more base directories relative in with they should be
located.

This library implements functions to list the directories according to the
specification and provides a few higher-level functions.

%package -n %{name}-devel
Summary:        XDG Base Directory Specification Library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}-%{release}

%description -n %{name}-devel
The XDG Base Directory Specification defines where should user files be looked
for by defining one or more base directories relative in with they should be
located.

This library implements functions to list the directories according to the
specification and provides a few higher-level functions.

%prep
%setup -q

%build
autoreconf -fvi
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
rm "%{buildroot}%{_libdir}/libxdg-basedir.la"

%post   -n libxdg-basedir1 -p /sbin/ldconfig
%postun -n libxdg-basedir1 -p /sbin/ldconfig

%files -n "%{name}%{soname}"
%license COPYING
%{_libdir}/libxdg-basedir.so.%{soname}
%{_libdir}/libxdg-basedir.so.%{soname}.*

%files -n "%{name}-devel"
%{_includedir}/basedir.h
%{_includedir}/basedir_fs.h
%{_libdir}/libxdg-basedir.so
%{_libdir}/libxdg-basedir.a
%{_libdir}/pkgconfig/libxdg-basedir.pc

%changelog
