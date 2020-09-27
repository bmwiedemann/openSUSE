#
# spec file for package libnbcompat
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2020 Archie L. Cobbs <archie@dellroad.org>
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

# the "0" below is the shared library "current" number (see Autobook, section 11.4)
%define libname     libnbcompat0

Name:           libnbcompat
Version:        1.0.1
Release:        0
Summary:        NetBSD compatibility library 
License:        BSD-4-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/archiecobbs/%{name}
Source:         https://github.com/archiecobbs/%{name}/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
%{name} is a NetBSD compatibility library that supplies routines used by NetBSD
bootstrap tools that are missing on other operating systems.

%package -n %{libname}
Summary:        NetBSD compatibility library 
Group:          Development/Libraries/C and C++

%description -n %{libname}
This package holds the shared library of %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package holds the development files for %{name}.

%{name} is a NetBSD compatibility library that supplies routines used by NetBSD
bootstrap tools that are missing on other operating systems.

%prep
%setup -q

%build
autoreconf -vfi -I .
%configure --disable-static LIBDIR='%{_libdir}'
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name '*.la' -delete -print

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
