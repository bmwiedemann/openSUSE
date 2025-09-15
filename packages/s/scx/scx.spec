#
# spec file for package scx
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _lto_cflags %{nil}
%define libbpf_min_ver 1.4
%define llvm_min_ver 17
Name:           scx
Version:        1.0.16
Release:        0
Summary:        Sched_ext CPU schedulers
License:        GPL-2.0-only
URL:            https://github.com/sched-ext/scx
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
BuildRequires:  bpftool >= 7.5.0
BuildRequires:  clang >= %{llvm_min_ver}
BuildRequires:  jq
BuildRequires:  libbpf-devel >= %{libbpf_min_ver}
BuildRequires:  lld
BuildRequires:  llvm >= %{llvm_min_ver}
BuildRequires:  meson >= 1.2.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  rust+cargo >= 1.82
BuildRequires:  zstd
BuildRequires:  pkgconfig(libbpf) >= %{libbpf_min_ver}
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(systemd)
ExclusiveArch:  %{rust_arches}

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This package contains various scheduler implementations and support utilities.

%package devel
Summary:        Development files for sched-ext
BuildArch:      noarch

%description devel
Header files needed to develop a sched-ext scheduler in C.

%prep
%autosetup -p1 -a1

%build
%meson \
  -Doffline=true \
  -Dbpftool=%{_sbindir}/bpftool \
  -Dlibbpf_a=disabled \
  -Dopenrc=disabled \
  -Denable_stress=false \
  %{?nil}
%meson_build

%install
%meson_install

%pre
%service_add_pre scx.service

%post
%service_add_post scx.service

%preun
%service_del_preun scx.service

%postun
%service_del_postun scx.service

%files
%license LICENSE
%doc README.md OVERVIEW.md
%{_bindir}/scx{cash,ctl,top,_*}
%{_bindir}/vmlinux_docify
%{_unitdir}/scx.service
%config(noreplace) %{_sysconfdir}/default/%{name}

# exclude scx_loader because of dbus warning.
%exclude %{_prefix}/lib/systemd/system/scx_loader.service
%exclude %{_datadir}/dbus-1
%exclude %{_datadir}/scx_loader

%files devel
%license LICENSE
%doc README.md BREAKING_CHANGES.md DEVELOPER_GUIDE.md
%{_includedir}/%{name}

%changelog
