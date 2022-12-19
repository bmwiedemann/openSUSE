#
# spec file for package sccache
#
# Copyright (c) 2022 SUSE LLC
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


%define configdir %{_sysconfdir}/%{name}

Name:           sccache
Version:        0.3.3~20
Release:        0
Summary:        A compiler caching tool for Rust, C and C++ with optional cloud storage
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR CC0-1.0) AND ((Apache-2.0 AND BSD-2-Clause) OR MIT) AND (Apache-2.0 OR MIT OR BSD-2-Clause) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT
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
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(openssl)
Requires:       bubblewrap

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
%ifarch x86_64
# 'dist-server' available only on x86_64 so far - https://github.com/mozilla/sccache/issues/656
features="azure,s3,redis,dist-server,dist-client,concurrent-cache"
%else
%ifarch aarch64
features="azure,s3,redis,concurrent-cache"
%else
# Most other arches have issues (especially with ring). Use FS cache only
features="concurrent-cache"
%endif
%endif

%{cargo_build} --no-default-features --features=$features

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
