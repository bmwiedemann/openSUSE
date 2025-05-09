#
# spec file for package libsigrokdecode
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


Name:           libsigrokdecode
%define libname %{name}4
%define baseversion 0.6.0
Version:        0.6.0~git20241001.71f4514
Release:        0
Summary:        Protocol Decoders for sigrok
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://sigrok.org/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         libsigrokdecode-versioned-decoders.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel >= 0.9.4
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.24.0
BuildRequires:  libsigrok-devel >= 0.3.0
BuildRequires:  libtool
BuildRequires:  python3-devel >= 3.2

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

libsigrokdecode is a shared library written in C which provides the basic
API for running sigrok protocol decoders. The protocol decoders themselves
are written in Python.

%package     -n %{libname}
Summary:        Protocol Decoder Library for sigrok
Group:          System/Libraries
Requires:       python3-base
# Fix screwup
Obsoletes:      %{libname} = 0.6.0+git20240304.0235970

%description -n %{libname}
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

libsigrokdecode is a shared library written in C which provides the basic
API for running sigrok protocol decoders. The protocol decoders themselves
are written in Python.

%package     -n libirmp0
Summary:        Protocol Decoder Library for sigrok
Group:          System/Libraries

%description -n libirmp0
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

%package        devel
Summary:        Protocol Decoder Library for sigrok
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       python3-devel

%description    devel
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

libsigrokdecode is a shared library written in C which provides the basic
API for running sigrok protocol decoders. The protocol decoders themselves
are written in Python.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
        --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_datadir}/%{name}-%{baseversion}/

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n libirmp0 -p /sbin/ldconfig
%postun -n libirmp0 -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc README HACKING NEWS
%{_libdir}/libsig*.so.*
%{_datadir}/%{name}-%{baseversion}/

%files -n libirmp0
%{_libdir}/libirmp*.so.*
%license COPYING

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
