#
# spec file for package sccache
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


%global rustflags -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2
%define configdir %{_sysconfdir}/%{name}

Name:           sccache
Version:        0.2.15~git1.22a176c
Release:        0
Summary:        A compiler caching tool for Rust, C and C++ with optional cloud storage
License:        Apache-2.0
Group:          Development/Languages/Rust
URL:            https://github.com/mozilla/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source10:       sccache-dist-builder.service
Source11:       sccache-dist-scheduler.service
Source12:       builder.conf
Source13:       scheduler.conf
Source14:       client.example
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(openssl)
Requires:       bubblewrap
ExcludeArch:    s390 s390x ppc ppc64 ppc64le %ix86

%description
Sccache is a ccache-like tool. It is used as a compiler wrapper and
avoids compilation when possible, storing a cache in a remote storage
using the Amazon Simple Cloud Storage Service (S3) API, Redis or
the Google Cloud Storage (GCS) API.

%prep
%setup -q
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config
# Remove exec bits to prevent an issue in fedora shebang checking
find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
export RUSTFLAGS="%{rustflags}"
# 'dist-server' available only on x86_64 so far - https://github.com/mozilla/sccache/issues/656
features="all,dist-client"
%ifarch x86_64
features="$features,dist-server"
%endif
cargo build --offline --release --features=$features

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -D -d -m 0755 %{buildroot}%{configdir}

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/sccache %{buildroot}%{_bindir}/sccache
%ifarch x86_64
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/sccache-dist %{buildroot}%{_bindir}/sccache-dist
%endif

%ifarch x86_64
install -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/sccache-dist-builder.service
install -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/sccache-dist-scheduler.service
%endif
install -m 0644 %{SOURCE12} %{buildroot}%{configdir}/builder.conf
install -m 0644 %{SOURCE13} %{buildroot}%{configdir}/scheduler.conf
install -m 0644 %{SOURCE14} %{buildroot}%{configdir}/client.example

%ifarch x86_64
%pre
%service_add_pre sccache-dist-builder.service
%service_add_pre sccache-dist-scheduler.service

%post
%service_add_post sccache-dist-builder.service
%service_add_post sccache-dist-scheduler.service

%preun
%service_del_preun sccache-dist-builder.service
%service_del_preun sccache-dist-scheduler.service

%postun
%service_del_postun sccache-dist-builder.service
%service_del_postun sccache-dist-scheduler.service
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/sccache
%ifarch x86_64
%{_bindir}/sccache-dist

%{_unitdir}/sccache-dist-builder.service
%{_unitdir}/sccache-dist-scheduler.service
%endif

%dir %{configdir}
%config(noreplace) %{configdir}/scheduler.conf
%config(noreplace) %{configdir}/builder.conf
%config(noreplace) %{configdir}/client.example

%changelog
