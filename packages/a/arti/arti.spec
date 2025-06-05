#
# spec file for package arti
#
# Copyright (c) 2025 SUSE LLC
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


%define git_hash 37c0c70ac5cacf49960b4ad91fddcd695708d6c2
Name:           arti
Version:        1.4.3
Release:        0
Summary:        An implementation of Tor, in Rust.
License:        Apache-2.0 OR MIT
URL:            https://gitlab.torproject.org/tpo/core/arti
Source0:        https://gitlab.torproject.org/tpo/core/arti/-/archive/arti-v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
ExclusiveArch:  %{rust_tier1_arches}

%description
An implementation of Tor, in Rust

%prep
%autosetup -p1 -a1 -n arti-arti-v%{version}-%{git_hash}

%build
%limit_build -m 8000
%{cargo_build}

%install
%{cargo_install -p crates/arti}

%check
%{cargo_test}

%files
%doc CHANGELOG.md README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/%{name}

%changelog
