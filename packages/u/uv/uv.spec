#
# spec file for package uv
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


Name:           uv
Version:        0.1.42
Release:        0
Summary:        A Python package installer and resolver, written in Rust 
License:        Apache-2.0 or MIT
URL:            https://github.com/astral-sh/uv
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  rust >= 1.77
Requires:       python3

%description
uv is a Python package installer and resolver, written in Rust. Designed as a
drop-in replacement for common pip and pip-tools workflows.

%prep
%autosetup -p1 -a1

%build
%{cargo_build} --all

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 -t %{buildroot}%{_bindir}/ %{_builddir}/%{name}-%{version}/target/release/uv{,-dev} 

# Tests require network
#%%check
#%%cargo_test

%files
%license LICENSE-*
%doc README.md
%{_bindir}/uv
%{_bindir}/uv-dev

%changelog

