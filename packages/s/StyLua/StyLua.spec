#
# spec file for package StyLua
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


%define _bin_name stylua
Name:           StyLua
Version:        0.15.3
Release:        0
Summary:        Opinionated Lua code formatter
License:        (Apache-2.0 OR MIT) AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND Apache-2.0 AND MIT AND MPL-2.0 AND MPL-2.0
URL:            https://github.com/JohnnyMorganz/StyLua
Source0:        https://github.com/JohnnyMorganz/StyLua/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo

%description
StyLua is an opinonated code formatter for Lua 5.1, 5.2, 5.3, 5.4 and Luau
built using full-moon. StyLua is inspired by the likes of prettier, it
parses your Lua codebase, and prints it back out from scratch, enforcing a
consistent code style.

%prep
%setup -q -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config.toml

%build
%{cargo_build} --all-features

%install
%{cargo_install} --all-features

%check
%{cargo_test}

%files
%{_bindir}/%{_bin_name}
%license LICENSE.md
%doc README.md

%changelog
