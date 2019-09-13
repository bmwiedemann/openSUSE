# vim: set sw=4 ts=4 et:
#
# spec file for package libxdg-basedir
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libxdg-basedir
Version:        1.2.0
Release:        0
%define soname 1
Summary:        XDG Base Directory Specification Library
License:        MIT
Group:          System/Libraries
Url:            http://nevill.ch/libxdg-basedir/
Source:         http://nevill.ch/libxdg-basedir/downloads/libxdg-basedir-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/devnev/libxdg-basedir/pull/3 -- lnussel@suse.de
Patch0:         0001-Overflow-bug.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n "libxdg-basedir-%{version}"
%patch0 -p1

%build
%configure
%__make %{?_smp_flags}

%check
%__make check

%install
%makeinstall
%__rm "%{buildroot}%{_libdir}/libxdg-basedir.la"

%post   -n libxdg-basedir1 -p /sbin/ldconfig
%postun -n libxdg-basedir1 -p /sbin/ldconfig

%files -n "%{name}%{soname}"
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libxdg-basedir.so.%{soname}
%{_libdir}/libxdg-basedir.so.%{soname}.*

%files -n "%{name}-devel"
%defattr(-,root,root)
%{_includedir}/basedir.h
%{_includedir}/basedir_fs.h
%{_libdir}/libxdg-basedir.so
%{_libdir}/libxdg-basedir.a
%{_libdir}/pkgconfig/libxdg-basedir.pc

%changelog
