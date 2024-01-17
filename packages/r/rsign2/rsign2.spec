#
# spec file
#
# Copyright (c) 2021-2022 cunix
# Copyright (c) 2022 SUSE LLC
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


%define short_name  rsign

# repeated here to guard against script deletes
#
# Copyright (c) 2021-2022 cunix
#

Name:           %{short_name}2
Version:        0.6.3+0
Release:        0
Summary:        Command-line tool to sign files and verify signatures
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/jedisct1/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
# on 20230623 at least crate "clap" had this minimum version requirement
BuildRequires:  cargo >= 1.64
BuildRequires:  vendored_licenses_packager
Provides:       %{short_name} = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rust implementation of Minisign, a tool to sign files and verify signatures.

%prep
%setup -q -n %{name}-%{version}
%setup -q -D -T -a 1

mkdir .cargo
cp %{SOURCE2} .cargo/config

%vendored_licenses_packager_prep

%build
cargo build --release %{?_smp_mflags}

%install
cargo install --path . --root=%{buildroot}%{_prefix}

rm %{buildroot}%{_prefix}/.crates.toml
rm %{buildroot}%{_prefix}/.crates2.json

%vendored_licenses_packager_install

%files
%{_bindir}/%{short_name}
%doc README.md
%license LICENSE
%vendored_licenses_packager_files

%changelog
