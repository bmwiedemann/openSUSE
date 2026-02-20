#
# spec file for package scx
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.0.20
Release:        0
Summary:        Sched_ext CPU schedulers
License:        GPL-2.0-only
URL:            https://github.com/sched-ext/scx
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
Source2:        scx.service
Source3:        scx.env
BuildRequires:  bpftool >= 7.5.0
BuildRequires:  cargo-packaging
BuildRequires:  clang >= %{llvm_min_ver}
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  libbpf-devel >= %{libbpf_min_ver}
BuildRequires:  lld
BuildRequires:  llvm >= %{llvm_min_ver}
BuildRequires:  pkgconfig
BuildRequires:  rust+cargo >= 1.82
BuildRequires:  zstd
BuildRequires:  pkgconfig(libbpf) >= %{libbpf_min_ver}
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(systemd)

ExclusiveArch:  %{rust_arches}
ExcludeArch:    %{ix86}

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
%cargo_build

%install
export CARGO_HOME=$PWD/.cargo

for path in ./tools/scxtop \
	./tools/scxcash \
	./scheds/rust/scx_p2dq \
	./scheds/rust/scx_tickless \
	./scheds/rust/scx_chaos \
	./scheds/rust/scx_rusty \
	./scheds/rust/scx_flash \
	./scheds/rust/scx_rustland \
	./scheds/rust/scx_mitosis \
	./scheds/rust/scx_rlfifo \
	./scheds/rust/scx_wd40 \
	./scheds/rust/scx_lavd \
	./scheds/rust/scx_cosmos \
	./scheds/rust/scx_layered \
	./scheds/rust/scx_beerland \
	./scheds/rust/scx_bpfland; do
pushd "${path}"
%{cargo_install}
popd
done

install -Dm644 %{SOURCE2} \
    %{buildroot}%{_unitdir}/scx.service

install -Dm644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/default/scx

mkdir -p %{buildroot}%{_includedir}/%{name}
install -Dm644 scheds/include/scx/*.h \
    %{buildroot}%{_includedir}/%{name}

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
%{_bindir}/scx{cash,top,_*}
%{_unitdir}/scx.service
%config(noreplace) %{_sysconfdir}/default/%{name}

%files devel
%license LICENSE
%doc README.md BREAKING_CHANGES.md DEVELOPER_GUIDE.md
%{_includedir}/%{name}

%changelog
