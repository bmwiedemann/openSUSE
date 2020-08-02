#
# spec file for package libbpf
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


%define sover_major 0
%define libname libbpf%{sover_major}
Name:           libbpf
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Version:        %{version}
Release:        0
Summary:        C library for managing eBPF programs and maps
License:        LGPL-2.1-only
URL:            http://www.kernel.org/
BuildRequires:  kernel-source
BuildRequires:  libelf-devel
BuildRequires:  python3

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
(cd /usr/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile arch/*/{include,lib,Makefile} kernel/bpf lib) | tar -xf -
cp /usr/src/linux/LICENSES/preferred/GPL-2.0 .
sed -i -e 's/CFLAGS += -O2/CFLAGS = $(RPM_OPT_FLAGS)/' Makefile

%build
cd tools/lib/bpf
%if %{__isa_bits} == 64
%make_build CFLAGS="%{optflags}" LP64=1
%else
%make_build CFLAGS="%{optflags}"
%endif

%install
cd tools/lib/bpf
%if %{__isa_bits} == 64
%make_install prefix=/usr LP64=1
%else
%make_install prefix=/usr
%endif
make install_headers prefix=%{buildroot}/usr

rm -f %{buildroot}%{_libdir}/%{name}.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/%{name}.so.%{sover_major}*

%files devel
%{_includedir}/bpf
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
