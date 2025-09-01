#
# spec file for package jaq
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           jaq
Version:        2.3.0
Summary:        jq clone in Rust
License:        MIT
Release:        0
URL:            https://github.com/01mf02/jaq
Source:         https://github.com/01mf02/jaq/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  gcc

%description
jaq (pronounced like Jacques) is a clone of the JSON data processing tool
jq. jaq aims to support a large subset of jq's syntax and operations.

%prep
%autosetup -a1

%build
%{cargo_build} --package jaq

%check
%{cargo_test}

%install
pushd jaq
%{cargo_install}
popd

%files
%{_bindir}/%{name}
%license LICENSE-MIT
%doc README.md

%changelog
