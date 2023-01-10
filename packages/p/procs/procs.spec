#
# spec file for package procs
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

%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
Name:           procs
Version:        0.13.3
Release:        0
Summary:        A modern replacement for ps written in Rust 
License:        MIT
URL:            https://github.com/dalance/procs
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  rust-packaging

%description
procs is a replacement for ps written in Rust.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
RUSTFLAGS=%{rustflags} cargo build --release

%install
RUSTFLAGS=%{rustflags} cargo install --root=%{buildroot}%{_prefix} --path .
# remove residue crate file
rm %{buildroot}%{_prefix}/.crates.toml
rm %{buildroot}%{_prefix}/.crates2.json

%files
%license LICENSE
%doc README.md
%{_bindir}/procs

%changelog

