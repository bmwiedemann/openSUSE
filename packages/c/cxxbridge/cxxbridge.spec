#
# spec file for package cxxbridge
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


Name:           cxxbridge
Version:        1.0.187
Release:        0
Summary:        Code generator for safe FFI between Rust and C++
License:        MIT
URL:            https://crates.io/crates/cxxbridge-cmd
Source0:        https://github.com/dtolnay/cxx/releases/download/1.0.187/cxx-1.0.187.tar.gz#/cxx-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  coreutils
BuildRequires:  cargo-packaging
BuildRequires:  gcc
BuildRequires:  gcc-c++

%global crate cxx

%description
C++ code generator for integrating `cxx` crate into non-Cargo builds

%prep
%autosetup -p1 -a1 -n cxx-%{version}

%build
%{cargo_build} -p cxxbridge-cmd

%install
install -D -m 0755 %{_builddir}/cxx-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
%{cargo_test}

%files
%license LICENSE-MIT
%{_bindir}/cxxbridge
%changelog

