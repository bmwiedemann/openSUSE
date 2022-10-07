#
# spec file for package atuin
#
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


Name:           atuin
Version:        11.0.0
Release:        0
Summary:        Magical shell history
License:        MIT
URL:            https://github.com/ellie/atuin
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  cargo-packaging
BuildRequires:  libgcc_s1
BuildRequires:  rust+cargo >= 1.59

%description
Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands.
Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/atuin

%changelog
