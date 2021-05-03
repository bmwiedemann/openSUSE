#
# spec file for package tealdeer
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


Name:           tealdeer
Version:        1.4.1
Release:        0
Summary:        An implementation of tldr in Rust
License:        Apache-2.0 OR MIT
Group:          Productivity/Other
URL:            https://github.com/dbrgn/tealdeer
Source0:        https://github.com/dbrgn/tealdeer/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
# Instructions on how to generate vendor.tar.xz
Source2:        README.packager
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  libopenssl-devel
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  zlib-devel

%description
An implementation of tldr in Rust. It has example based and community-driven man pages.

%prep
%setup -qa1
mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
cargo build --release --locked %{?_smp_mflags}

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .

%files
%doc README.md
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/tldr

%changelog
