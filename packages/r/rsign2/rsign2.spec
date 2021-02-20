#
# spec file for package rsign2
#
# Copyright (c) 2021 cunix
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


%define _buildshell /bin/bash
%define vlic_dir  vendored
%define short_name  rsign
%define last_update  20210216

Name:           %{short_name}2
Version:        0.5.7
Release:        0
Summary:        Command-line tool to sign files and verify signatures
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/jedisct1/%{name}
Source0:        https://codeload.github.com/jedisct1/%{name}/tar.gz/%{version}#/%{name}-%{version}.tar.gz
# created with "cargo vendor --versioned-dirs"
Source1:        vendor-%{version}.tar.xz
# to verify Source1:
Source2:        Cargo-%{version}-%{last_update}.lock
# Find licenses of dependency packages.
Source3:        find_licenses.sh
# Install licenses of dependency packages.
Source4:        install_licenses.sh
BuildRequires:  cargo
# on 20210216 at least following crates had this minimum version in README.md
# cipher, crypto-mac, digest, generic-array, hmac, pbkdf2, scrypt, sha2, subtle
BuildRequires:  rust >= 1.41
Provides:       %{short_name} = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rust implementation of Minisign, a tool to sign files and verify signatures.

%prep
%setup -q -n %{name}-%{version}
%setup -q -D -T -a 1

cp %{SOURCE2} Cargo.lock

mkdir $PWD/.cargo
cat > $PWD/.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "./.vendor"
EOF

cd $PWD/.vendor
# Find licenses of dependency packages and prepare for installation
bash %{SOURCE3} %{vlic_dir}

%build
export CARGO_HOME=$PWD/.cargo
cargo build --release %{?_smp_mflags}

%install
export CARGO_HOME=$PWD/.cargo
cargo install --path . --root=%{buildroot}%{_prefix}

rm %{buildroot}%{_prefix}/.crates.toml
rm %{buildroot}%{_prefix}/.crates2.json

# Dependency Licenses
install -d -m 0755 %{buildroot}%{_licensedir}/%{name}/%{vlic_dir}
bash %{SOURCE4} .vendor/%{vlic_dir} %{buildroot}/%{_licensedir}/%{name}/%{vlic_dir}

%files
%{_bindir}/%{short_name}
%doc README.md
%license LICENSE
%{_licensedir}/%{name}/%{vlic_dir}/

%changelog
