#
# spec file for package rust-cbindgen
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


# Use hardening ldflags.
%global crate_name cbindgen
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now
Name:           rust-%{crate_name}
Version:        0.15.0
Release:        0
Summary:        A tool for generating C bindings from Rust code
License:        MPL-2.0
Group:          Development/Languages/Rust
URL:            https://crates.io/crates/cbindgen
Source0:        https://github.com/eqrion/cbindgen/archive/v%{version}.tar.gz#/%{crate_name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo >= 1.30.0
BuildRequires:  rust >= 1.30.0
BuildRequires:  rust-std-static >= 1.30.0

%description
A tool for generating C bindings from Rust code.

%prep
%setup -q -T -b 0 -n %{crate_name}-%{version}
%setup -q -D -T -a 1 -n %{crate_name}-%{version}
mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
# This should eventually migrate to distro policy
# Enable optimization, debuginfo, and link hardening.
export RUSTFLAGS="%{rustflags}"
export CARGO_HOME=`pwd`/cargo-home/

cargo build --release

%install
# rustflags must be exported again at install as cargo build will
# rebuild the project if it detects flags have changed (to none or other)
export RUSTFLAGS="%{rustflags}"
# install stage also requires re-export of 'cargo-home' or cargo
# will try to download source deps and rebuild
export CARGO_HOME=`pwd`/cargo-home/
# cargo install appends /bin to the path
cargo install --root=%{buildroot}%{_prefix} --path .
# remove spurious files
rm -f %{buildroot}%{_prefix}/.crates.toml
rm -f %{buildroot}%{_prefix}/.crates2.json

%files
%license LICENSE
%{_bindir}/cbindgen

%changelog
