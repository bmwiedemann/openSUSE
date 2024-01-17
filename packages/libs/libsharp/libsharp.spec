#
# spec file for package libsharp
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


%define sover 0
%define shlib %{name}%{sover}
Name:           libsharp
Version:        1.0.0
Release:        0
Summary:        Library for fast spherical harmonic transforms
License:        GPL-2.0-or-later
URL:            https://github.com/Libsharp/libsharp
Source:         https://downloads.sourceforge.net/project/healpix/Healpix_3.60/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
libsharp is a code library for spherical harmonic transforms (SHTs) with
features including MPI support for distributed memory systems and SHTs of
fields with arbitrary spin, supporting new developments in CPU instruction sets
like the Advanced Vector Extensions (AVX) or fused multiply-accumulate (FMA)
instructions.

%package -n %{shlib}
Summary:        Shared library for libsharp -- a spherical harmonic transforms library

%description -n %{shlib}
libsharp is a code library for spherical harmonic transforms (SHTs).

This package provides the shared library for libsharp.

%package devel
Summary:        Headers and devel files for libsharp
Requires:       %{shlib} = %{version}

%description devel
libsharp is a code library for spherical harmonic transforms (SHTs).

This package provides the headers and devel files for developing applications
against libsharp.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license COPYING
%{_libdir}/libsharp.so.*

%files devel
%license COPYING
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%changelog
