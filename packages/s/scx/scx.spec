#
# spec file for package scx
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


%define libbpf_min_ver 1.5.0

Name:           scx
Version:        1.0.8
Release:        0
Summary:        Sched_ext CPU schedulers
License:        GPL-2.0-only
URL:            https://github.com/sched-ext/scx
Source0:        scx-%version.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  bpftool >= 7.5.0
BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  jq
BuildRequires:  libbpf-devel >= %libbpf_min_ver
BuildRequires:  lld
BuildRequires:  meson >= 1.3.0
BuildRequires:  ninja
BuildRequires:  zstd
BuildRequires:  pkgconfig(libbpf) >= %libbpf_min_ver
BuildRequires:  pkgconfig(systemd)

%description
sched_ext is a Linux kernel feature which enables implementing kernel thread schedulers in BPF and dynamically loading them. This package contains various scheduler implementations and support utilities.

%package devel
Summary:        Development files for sched-ext
BuildArch:      noarch

%description devel
Header files needed to develop a sched-ext scheduler in C.

%prep
%setup -qa1

%build
# meson macros use set_build_flags which makes the linker fail during build,
# using without macros for now.
meson setup --prefix=%{_prefix} -Doffline=true -Dbpftool=/usr/sbin/bpftool -Dlibbpf_a=disabled -Dopenrc=disabled --buildtype=release build
meson compile -C build -v

%install
meson install -C build --destdir=%{buildroot}

# move lib into scx folder
mv %{buildroot}/%{_prefix}/include/lib %{buildroot}/%{_prefix}/include/scx/

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
%doc README.md

%{_bindir}/*
%{_prefix}/lib/systemd/system/scx.service

# exclude scx_loader because of dbus warning.
%exclude %{_prefix}/lib/systemd/system/scx_loader.service
%exclude %{_prefix}/share/dbus-1

%config %{_sysconfdir}/default/%{name}

%files devel
%license LICENSE
%doc README.md

%{_prefix}/include/scx

%changelog
