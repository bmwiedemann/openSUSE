#
# spec file for package arti
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Eyad Issa <eyadlorenzo@gmail.com>
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


%global git_hash 0b636d9d8d3309663de0fb5554255f5f8f82544d

Name:           arti
Version:        1.6.0
Release:        0
Summary:        An implementation of Tor, in Rust.
License:        (Apache-2.0 OR MIT) AND LGPL-3.0-only
URL:            https://gitlab.torproject.org/tpo/core/arti
Source0:        https://gitlab.torproject.org/tpo/core/arti/-/archive/arti-v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.85.1
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
ExclusiveArch:  %{rust_tier1_arches}

%description
An implementation of Tor, in Rust

%prep
%autosetup -p1 -a1 -n arti-arti-v%{version}-%{git_hash}

%build
%limit_build -m 8000
%{cargo_build} -p arti

%install
%{cargo_install -p crates/arti}

%check
%{cargo_test}

%files
%doc CHANGELOG.md README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/%{name}

%changelog
