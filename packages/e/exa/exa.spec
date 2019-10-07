#
# spec file for package exa
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           exa
Version:        0.9.0
Release:        0
Summary:        Replacement for ls written in Rust
License:        MIT
Group:          System/Base
Url:            https://the.exa.website/
Source0:        https://github.com/ogham/exa/archive/v%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    %ix86 ppc

%description
exa is a replacement for ls written in Rust.
With similar but not identical options.

%prep
%setup -q
%setup -q -D -T -a 1
mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
cargo build --release %{?_smp_mflags}

%install
mkdir build
cargo install --path . --root=build
mkdir -p %{buildroot}%{_bindir}
install -Dm0755 build/bin/exa %{buildroot}%{_bindir}/exa

%files
%license LICENCE
%doc README.md
%{_bindir}/exa

%changelog
