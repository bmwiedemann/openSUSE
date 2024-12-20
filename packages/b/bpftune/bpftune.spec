#
# spec file for package bpftune
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define soname 0_1_3
Name:           bpftune
Version:        0.1~20241219
Release:        0
Summary:        BPF/tracing tools for auto-tuning Linux
License:        GPL-2.0-only WITH Linux-syscall-note
URL:            https://github.com/oracle/bpftune/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  bpftool >= 4.18
BuildRequires:  clang >= 11
BuildRequires:  llvm >= 11
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(libbpf) >= 0.6
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libnl-3.0)
# assertions in code exlude certain architectures
ExcludeArch:    %{ix86} s390x %{arm} ppc64le riscv64

%description
Service consisting of daemon (bpftune) and plugins which support auto-tuning of
Linux via BPF observability.

%package -n libbpftune%{soname}
Summary:        BPF/tracing library

%description -n libbpftune%{soname}
Shared library for (bpftune) for auto-tuning of Linux via BPF observability.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       libbpftune%{soname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing BPF shared object tuners that use %{name}

%prep
%autosetup -p1

%build
%make_build \
	BPFTOOL=%{_sbindir}/bpftool \
	%{nil}

%install
%make_install

# %%check
# /usr/sbin/tc needs root
# %%make_build test

%pre
%service_add_pre bpftune.service

%post
%service_add_post bpftune.service

%preun
%service_del_preun bpftune.service

%postun
%service_del_postun bpftune.service

%ldconfig_scriptlets -n libbpftune%{soname}

%files
%license LICENSE.txt
%{_sbindir}/bpftune
%{_unitdir}/bpftune.service
%dir %{_libdir}/bpftune
%{_libdir}/bpftune/*.so
%{_mandir}/man8/*.gz

%files -n libbpftune%{soname}
%license LICENSE.txt
%{_sysconfdir}/ld.so.conf.d/libbpftune.conf
%{_libdir}/libbpftune.so.*

%files devel
%license LICENSE.txt
%{_includedir}/bpftune
%{_libdir}/libbpftune.so

%changelog
