#
# spec file for package racer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Michal Vyskocil, michal.vyskocil@opensuse.org
# Copyright (c) 2016 Kristoffer Gronlund, kgronlund@suse.com
# Copyright (c) 2017 Luke Jones, jones_ld@protonmail.com
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
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now
Name:           racer
Version:        2.0.14
Release:        0
Summary:        Code completion for Rust
License:        MIT
Group:          Development/Languages/Other
Url:            https://github.com/phildawes/racer

# See README.packager for instructions on generating
# the source archives
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        README.packager

BuildRequires:  cargo
BuildRequires:  git
BuildRequires:  rust >= 1.30.0
BuildRequires:  rust-std-static >= 1.30.0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
RACER = Rust Auto-Complete-er. A utility intended to provide Rust code
completion for editors and IDEs. Maybe one day the 'er' bit will be
exploring + refactoring or something.

%prep
%setup -q
%setup -q -D -T -a 1
mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
export RUSTFLAGS="%{rustflags}"
export CARGO_HOME=`pwd`/cargo-home/
cargo build --release

%install
export RUSTFLAGS="%{rustflags}"
export CARGO_HOME=`pwd`/cargo-home/
cargo install --root=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/.crates.toml

%files
%defattr(-,root,root)
%doc LICENSE-MIT README.md CHANGELOG.md
%{_bindir}/racer

%changelog
