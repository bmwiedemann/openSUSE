#
# spec file for package libbpf
#
# Copyright (c) 2024 SUSE LLC
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


%define sover_major 1
%define libname libbpf%{sover_major}
Name:           libbpf
Version:        1.4.3
Release:        0
Summary:        C library for managing eBPF programs and maps
License:        LGPL-2.1-only
URL:            https://github.com/libbpf/libbpf
Source:         https://github.com/libbpf/libbpf/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  libelf-devel
BuildRequires:  linux-glibc-devel >= 4.5
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

%package devel-static
Summary:        Static library for libbpf
Requires:       %{libname} = %{version}
Requires:       %{name}-devel = %{version}

%description devel-static
libbpf is a C library which provides API for managing eBPF programs and maps.

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
cd src
%make_build V=1 CFLAGS="%{optflags}"

%install
cd src
%make_install V=1

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

%files devel-static
%{_libdir}/%{name}.a

%changelog
