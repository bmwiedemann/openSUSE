#
# spec file for package numbat
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


Name:           numbat
Version:        1.12.0
Release:        0
URL:            https://github.com/sharkdp/numbat
Summary:        Statically typed programming language for scientific computations
Group:          Productivity/Scientific/Physics
License:        Apache-2.0 OR MIT
Source0:        https://github.com/sharkdp/numbat/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd

%description
Numbat is a statically typed programming language for scientific computations
with first class support for physical dimensions and units.

%prep
%autosetup -a1

%build
%{cargo_build} --all-features
rm book/.gitignore

%install
pushd numbat-cli
%{cargo_install} --all-features
popd

%check
%{cargo_test} --all-features

%files
%license LICENSE-MIT LICENSE-APACHE
%doc     README.md book
%{_bindir}/numbat*

%changelog
