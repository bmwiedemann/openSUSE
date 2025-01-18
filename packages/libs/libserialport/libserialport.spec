#
# spec file for package libserialport
#
# Copyright (c) 2025 SUSE LLC
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


%define libname %{name}0
Summary:        Handles OS-specific details when using serial ports
License:        LGPL-3.0-or-later
Group:          Productivity/Scientific/Electronics

Name:           libserialport
Version:        0.1.2
Release:        0
URL:            http://sigrok.org
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libudev)
Source0:        https://sigrok.org/download/source/libserialport/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

libserialport is a minimal, cross-platform shared library written in C
that is intended to take care of the OS-specific details when writing
software that uses serial ports.

It is licensed under the terms of the GNU Lesser General Public License,
version 3 or later.

%package -n %libname

Summary:        Handles OS-specific details when using serial ports
Group:          Productivity/Scientific/Electronics

%description -n %libname
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

libserialport is a minimal, cross-platform shared library written in C
that is intended to take care of the OS-specific details when writing
software that uses serial ports.

%package devel

Summary:        Handles OS-specific details when using serial ports
Group:          Development/Libraries/C and C++
Requires:       %libname = %version

%description devel
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

libserialport is a minimal, cross-platform shared library written in C
that is intended to take care of the OS-specific details when writing
software that uses serial ports.

%prep
%setup -q

%build
autoreconf -f
%configure --disable-static
make %{?smp_mflags}

%install
make install DESTDIR=%buildroot

rm -f %buildroot%{_libdir}/libserialport.la

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%license COPYING
%doc README NEWS
%_libdir/*.so.*

%files devel
%defattr(-,root,root,-)
%license COPYING
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*

%changelog
