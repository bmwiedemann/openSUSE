#
# spec file for package arti
#
# Copyright (c) 2024 SUSE LLC
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


Name:           arti
Version:        1.2.4~0
Release:        0
Summary:        An implementation of Tor, in Rust.
License:        Apache-2.0 OR MIT
URL:            https://gitlab.torproject.org/tpo/core/arti
Source0:        %{name}-%{version}.tar
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
%autosetup -p1 -a1

%build
%limit_build -m 4400
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
