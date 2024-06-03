#
# spec file for package i3status-rust
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           i3status-rust
Version:        0.33.1
Release:        0%{?dist}
Summary:        Feature-rich and resource-friendly replacement for i3status, written in Rust

License:        APSL-2.0 AND GPL-3.0-or-later AND MPL-2.0 AND Apache-2.0 AND (Apache-2.0 OR MIT) AND CC-BY-3.0 AND CC-BY-SA-4.0 AND (Artistic-1.0-Perl OR GPL-1.0-or-later) AND BSL-1.0 AND (Apache-2.0 OR BSL-1.0) AND CC0-1.0 AND (GPL-2.0-or-later OR MIT) AND HPND AND ISC AND Zlib AND BSD-2-Clause AND BSD-3-Clause AND Unicode-DFS-2016
URL:            https://github.com/greshake/i3status-rust
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config

ExclusiveArch:  %{rust_tier1_arches}

BuildRequires:  cargo >= 1.40
BuildRequires:  cargo-packaging
BuildRequires:  libpulse-devel
BuildRequires:  libsensors4-devel
BuildRequires:  rust >= 1.40
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(openssl)

Recommends:     fontawesome-fonts

Enhances:       i3
Enhances:       sway

%description
i3status-rs is a feature-rich and resource-friendly replacement for i3status,
written in pure Rust. It provides a way to display "blocks" of system
information (time, battery status, volume, etc) on the i3 bar. It is also
compatible with sway.

%prep
%setup -qa1

cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

rm -f %{buildroot}%{_prefix}/.crates.toml %{buildroot}%{_prefix}/.crates2.json
strip --strip-all %{buildroot}%{_bindir}/*

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r files/* %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc README.md NEWS.md CONTRIBUTING.md examples/ doc/*
%{_bindir}/i3status-rs
%{_datadir}/%{name}/

%changelog
