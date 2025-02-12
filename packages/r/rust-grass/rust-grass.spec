#
# spec file for package grass
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Bjørn Lie
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

%define _name grass

Name:           rust-grass
Version:        0.13.4
Release:        0
Summary:        A Sass compiler written purely in Rust
License:        MIT
URL:            https://github.com/connorskees/grass
Source:         %{_name}-%{version}.tar.zst
Source1:        vendor.tar.zst
ExclusiveArch:  %{rust_tier1_arches}

BuildRequires:  cargo
BuildRequires:  cargo-packaging
Conflicts:      grass

%description
This crate aims to provide a high level interface for compiling
Sass into plain CSS. It offers a very limited API, currently
exposing only 2 functions.

In addition to a library, this crate also includes a binary that is
intended to act as an invisible replacement to the Sass commandline
executable.

%prep
%autosetup -n %{_name}-%{version} -p1 -a1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{_name}-%{version}/target/release/%{_name} %{buildroot}%{_bindir}/%{_name}

%check
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{_name}

%changelog
