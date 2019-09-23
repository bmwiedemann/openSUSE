#
# spec file for package cargo-vendor
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Luke Jones, luke.nukem.jones@gmail.com
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


# Use hardening ldflags.
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now
Name:           cargo-vendor
Version:        0.1.23
Release:        0
Summary:        A Cargo subcommand to vendor Rust dependencies
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
URL:            https://github.com/alexcrichton/cargo-vendor
Source0:        https://github.com/alexcrichton/cargo-vendor/releases/download/%{version}/cargo-vendor-src-%{version}.tar.gz
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.30.0
BuildRequires:  rust-std-static >= 1.30.0
# curl-sys: libcurl, openssl
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2) >= 0.23
BuildRequires:  pkgconfig(libssh2) >= 1.4.3
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
This is a Cargo subcommand which vendors all crates.io dependencies into a local directory using Cargo's support for source replacement.

%prep
%setup -q -n %{name}-src-%{version}
mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

# The configure macro will modify some autoconf-related files, which upsets
# cargo when it tries to verify checksums in those files.  If we just truncate
# that file list, cargo won't have anything to complain about.
find vendor -name .cargo-checksum.json \
  -exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'

%build
# This should eventually migrate to distro policy
# Enable optimization, debuginfo, and link hardening.
export RUSTFLAGS="%{rustflags}"
export CARGO_HOME=`pwd`/cargo-home/
export LIBGIT2_SYS_USE_PKG_CONFIG=1
export LIBSSH2_SYS_USE_PKG_CONFIG=1

cargo build --release

%install
# rustflags must be exported again at install as cargo build will
# rebuild the project if it detects flags have changed (to none or other)
export RUSTFLAGS="%{rustflags}"
# install stage also requires re-export of 'cargo-home' or cargo
# will try to download source deps and rebuild
export CARGO_HOME=`pwd`/cargo-home/
# cargo install appends /bin to the path
cargo install --root=%{buildroot}%{_prefix}
# remove spurious file
rm %{buildroot}%{_prefix}/.crates.toml

%files
%doc LICENSE-MIT LICENSE-APACHE README.md
%{_bindir}/cargo-vendor

%changelog
