#
# spec file for package biome
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2022-2023 Avindra Goolcharan <avindra@opensuse.org>
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


%define ver 1.9.0
%define rev b260d5b0e6b2e8e0093128ca2bf1f66c8e5d35da
Name:           biome
Version:        %{ver}
Release:        0
Summary:        A JavaScript and TypeScript toolchain
License:        Apache-2.0 AND MIT
Group:          Productivity/Other
URL:            https://github.com/biomejs/biome
Source0:        https://github.com/biomejs/biome/archive/%{rev}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.53.0

%description
A JavaScript and TypeScript toolchain.

%prep
%autosetup -a1 -p1 -n biome-%{rev}
cp %{SOURCE2} .cargo/config.toml

%build
export BIOME_VERSION=%{ver}-%{rev}
# auditable build fails
cargo build %{?__rustflags} %{?_smp_mflags} --release

%install
mkdir -p %{buildroot}%{_bindir}
cp target/release/%{name} %{buildroot}%{_bindir}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/%{name}

# generate changelog with:
# $$(".Box li").map(l => l.textContent.trim()).join('\n')
%changelog
