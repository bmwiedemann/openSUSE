#
# spec file for package cargo-audit
#
# Copyright (c) 2023 SUSE LLC
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
%global workspace_name rustsec

Name:           cargo-audit
Version:        0.17.5~git0.dc8ec71
Release:        0
Summary:        Audit rust sources for known security vulnerabilities
License:        ( 0BSD OR MIT OR Apache-2.0 ) AND ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR MIT ) AND ( MIT OR Zlib OR Apache-2.0 ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND MIT AND MPL-2.0 AND MPL-2.0+
Group:          Development/Languages/Rust
URL:            https://github.com/RustSec/cargo-audit
Source0:        %{workspace_name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config

BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(openssl)
ExclusiveArch:  %{rust_tier1_arches}

%description
Audit Cargo.lock files for crates with security vulnerabilities reported to the RustSec Advisory Database.

%prep
%setup -q -n %{workspace_name}-%{version}
%setup -qa1 -n %{workspace_name}-%{version}
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}

install -m 0755 %{_builddir}/%{workspace_name}-%{version}/target/release/cargo-audit %{buildroot}%{_bindir}/cargo-audit

%files
%{_bindir}/cargo-audit

%changelog
