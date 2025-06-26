#
# spec file for package biome
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2022-2025 Avindra Goolcharan <avindra@opensuse.org>
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


%define rev 09f49bade82e0aa15201b7db2efef10b1c330763
Name:           biome
Version:        2.0.5
Release:        0
Summary:        A JavaScript and TypeScript toolchain
License:        Apache-2.0 AND MIT
Group:          Productivity/Other
URL:            https://github.com/biomejs/biome
Source0:        https://github.com/biomejs/biome/archive/refs/tags/@biomejs/biome@%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.53.0
BuildRequires:  cargo-packaging
BuildRequires:  zstd

%description
A toolchain for web projects, aimed to provide functionalities to maintain
them. Biome offers formatter and linter, usable via CLI and LSP.

%prep
%autosetup -a1 -p1 -n %{name}--biomejs-%{name}-%{version}

%build
export BIOME_VERSION=%{version}-%{rev}
%{cargo_build} -p biome_cli

%install
mkdir -p %{buildroot}%{_bindir}
cp target/release/%{name} %{buildroot}%{_bindir}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/%{name}

%changelog
