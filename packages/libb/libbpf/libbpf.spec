#
# spec file for package libbpf
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


%define sover_major 0
%define libname libbpf%{sover_major}
Name:           libbpf
Version:        0.4.0
Release:        0
Summary:        C library for managing eBPF programs and maps
License:        LGPL-2.1-only
URL:            https://github.com/libbpf/libbpf
Source:         https://github.com/libbpf/libbpf/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/libbpf/libbpf/issues/337
Patch:          libdir.patch
BuildRequires:  libelf-devel
BuildRequires:  python3
BuildRequires:  zlib-devel

%description
libbpf is a C library which provides API for managing eBPF programs and maps.

%package -n %{libname}
Summary:        C library for managing eBPF programs and maps

%description -n %{libname}
libbpf is a C library which provides API for managing eBPF programs and maps.

%package devel
Summary:        Development files for libbpf
Requires:       %{libname} = %{version}

%description devel
libbpf is a C library which provides API for managing eBPF programs and maps.

%prep
%setup -q

%build
cd src
%make_build V=1 CFLAGS="%{optflags} -fno-lto"

%install
cd src
%make_install V=1 LIBDIR=%{_libdir}
rm -f %{buildroot}%{_libdir}/%{name}.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/%{name}.so.%{sover_major}*

%files devel
%license LICENSE LICENSE.BSD-2-Clause LICENSE.LGPL-2.1
%doc README.md
%{_includedir}/bpf
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
