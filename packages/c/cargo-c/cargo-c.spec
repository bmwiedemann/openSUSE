#
# spec file for package cargo-c
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019 Andreas Schneider <asn@cryptomilk.org>.
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

Name:           cargo-c
Version:        0.9.15~git0.2d3044b
Release:        0
Summary:        Helper to build and install c-like libraries from Rust
License:        MIT
Group:          Development/Languages/Rust

URL:            https://crates.io/crates/cargo-c
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config

Source1000:     README.suse-maint
BuildRequires:  cargo
BuildRequires:  pkgconfig(openssl)

%description
The is a cargo applet to build and install C-ABI compatibile dynamic and static
libraries from Rust.

It produces and installs a correct pkg-config file, a static library and a
dynamic library, and a C header to be used by any C (and C-compatible)
software.

%prep
%autosetup -a1 -p1

install -d -m 0755 .cargo
cp %{SOURCE2} .cargo/config

%build
export RUSTFLAGS="%{rustflags}"
cargo build --offline --release

%install
export RUSTFLAGS="%{rustflags}"
cargo install --offline --root=%{buildroot}%{_prefix} --path .

find %{buildroot} -name .crates2.json -delete
rm -rf %{buildroot}%{_datadir}/cargo/registry
rm %{buildroot}%{_prefix}/.crates.toml

%files
%license LICENSE
%doc README.md
%{_bindir}/cargo-capi
%{_bindir}/cargo-cbuild
%{_bindir}/cargo-cinstall
%{_bindir}/cargo-ctest

%changelog
