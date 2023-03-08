#
# spec file for package pijul
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


Name:           pijul
Version:        1.0.0~beta.4
Release:        0
Summary:        Distributed version control system based on a theory of patches
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            https://pijul.org/
# Fetched from https://crates.io/api/v1/crates/pijul/1.0.0-beta.2/download#/pijul-1.0.0-beta.2.tar.gz
# and renamed to get rid of the second dash.
Source0:        pijul-1.0.0~beta.4.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  libzstd-devel-static
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  xxhash-devel
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(openssl)
Conflicts:      pijul-bash-completion
Conflicts:      pijul-fish-completion
Conflicts:      pijul-zsh-completion

%description
Pijul is a distributed version control system. Its distinctive feature is to be
based on a theory of patches, which makes it really distributed.

%prep
%setup -qa1
mkdir cargo-home
cat >cargo-home/config <<EOF

[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
# bypass error https://bugzilla.opensuse.org/show_bug.cgi?id=1175502
# to avoid cargo reported error if config.sub has been changed
# by build macro.
%ifarch aarch64
subname='libsodium/build-aux/config.sub'
cfgsub="./vendor/libsodium-sys/$subname"
chkjson='./vendor/libsodium-sys/.cargo-checksum.json'
if [ -f "$cfgsub" ] && [ -f "$chkjson" ]; then
  chksum=`sha256sum $cfgsub |sed -e 's/ .*//'`
  grep -q $subname $chkjson && grep -q $chksum $chkjson || sed -i -e "s#\($subname.:.\)[0-9a-f]*#\1$chksum#" $chkjson
fi
%endif

export CARGO_HOME=`pwd`/cargo-home/
cargo build --release %{?_smp_mflags} --features git

%install

install -Dm0755 target/release/pijul %{buildroot}%{_bindir}/pijul

%files
%{_bindir}/pijul

%changelog
