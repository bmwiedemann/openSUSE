#
# spec file for package zziplib
#
# Copyright (c) 2021 SUSE LLC
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


%define lname   libzzip-0-13
Name:           zziplib
Version:        0.13.72
Release:        0
Summary:        ZIP Compression Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://zziplib.sourceforge.net
Source0:        https://github.com/gdraheim/zziplib/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch0:         zziplib-0.13.62.patch
Patch8:         bsc1154002-prevent-unnecessary-perror.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  zip
BuildRequires:  pkgconfig(zlib)

%description
ZZipLib is a library for dealing with ZIP and ZIP-like archives by
using algorithms of zlib.

%package -n %{lname}
Summary:        ZIP compression library
Group:          System/Libraries
Obsoletes:      zziplib < %{version}-%{release}
Provides:       zziplib = %{version}-%{release}

%description -n %{lname}
ZZipLib is a library for dealing with ZIP and ZIP-like archives by
using algorithms of zlib.

%package devel
Summary:        Development files for zziplib, a ZIP compression library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       pkgconfig(zlib)

%description devel
That are the header files needed for developing applications using
ZZipLib.

%prep
%setup -q
%patch0
%patch8 -p1
# do not bother with html docs saving us python2 dependency
sed -i -e 's:docs ::g' Makefile.am

%build
%cmake -DZZIP_TESTCVE=OFF
%cmake_build

%install
%cmake_install
rm -f docs/Make* docs/zziplib-manpages.ar
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING.LIB
%{_libdir}/libzzip*.so.*

%files devel
%doc docs/README.SDL ChangeLog README TODO
%{_bindir}/unzzip*
%{_bindir}/zz*
%{_bindir}/unzip-mem
%{_libdir}/libzzip*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/__zzip_*.3%{?ext_man}
%{_mandir}/man3/zzip_*.3%{?ext_man}

%changelog
