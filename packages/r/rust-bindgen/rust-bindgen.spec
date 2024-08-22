#
# spec file for package rust-bindgen
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           rust-bindgen
Version:        0.70.1
Release:        0
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
License:        BSD-3-Clause
Group:          Development/Languages/Rust
#Git-Clone:     https://github.com/rust-lang/rust-bindgen.git
URL:            https://rust-lang.github.io/rust-bindgen/
Source:         %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rust

%description
Automatically generates Rust FFI bindings to C (and some C++) libraries.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -m 0755 target/release/bindgen %{buildroot}%{_bindir}/bindgen

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/bindgen

%changelog
