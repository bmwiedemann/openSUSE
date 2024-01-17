#
# spec file for package libnxz
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


%global soversion 0
%define libname %{name}%{soversion}
Name:           libnxz
Version:        0.64
Release:        0
Summary:        Zlib implementation for POWER processors
License:        Apache-2.0 OR GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/%{name}/power-gzip
Source:         %{url}/archive/v%{version}.tar.gz#:/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  ppc64 ppc64le

%description
libnxz implements a zlib-compatible API for Linux userspace programs that exploit the NX GZIP accelerator available on POWER9 and newer processors.

%package -n %{libname}
Summary:        Zlib implementation for POWER processors

%description -n %{libname}
libnxz implements a zlib-compatible API for Linux userspace programs that exploit the NX GZIP accelerator available on POWER9 and newer processors.

This package contains the shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}0 = %{version}

%description devel
libnxz implements a zlib-compatible API for Linux userspace programs that exploit the NX GZIP accelerator available on POWER9 and newer processors.

This package contains the development files for %{name}.

%prep
%autosetup -p1 -n power-gzip-%{version}
dos2unix doc/Addendum-NX-GZIP-for-PowerVM.txt

%build
export CFLAGS="-ffat-lto-objects %optflags"
%configure --enable-zlib-api
%make_build

%install
%make_install
# Remove the installed licenses
rm %{buildroot}%{_datadir}/doc/libnxz/{APACHE-2.0,gpl-2.0}.txt
# Remove the static library
rm %{buildroot}%{_libdir}/%{name}.a

%check
# libnxz tests only work on P9 servers or newer, with Linux >= 5.8.
# This combination is not guaranteed to be present at build time. Check if
# NX GZIP engine device is available before deciding to run the tests.
if [ -w "/dev/crypto/nx-gzip" ]; then
	%make_build check
fi

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license licenses/*
%{_libdir}/%{name}.so.%{soversion}
%{_libdir}/%{name}.so.%{soversion}.*

%files devel
%doc doc/Addendum-NX-GZIP-for-PowerVM.txt README.md
%exclude %{_libdir}/%{name}.so.%{soversion}*
%{_libdir}/%{name}.*
%{_includedir}/%{name}.h

%changelog
