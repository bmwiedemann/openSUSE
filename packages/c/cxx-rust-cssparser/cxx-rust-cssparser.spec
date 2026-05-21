#
# spec file for package cxx-rust-cssparser
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.10.0

%bcond_without released

Name:           cxx-rust-cssparser
Version:        1.0.0
Release:        0
Summary:        Library for parsing CSS using the Rust cssparser crate
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/cxx-rust-cssparser
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        cxx-rust-cssparser.keyring
%endif
Source3:        vendor.tar.zst
# PATCH-FIX-UPSTREAM
Patch0:         Fix_offline_build.patch
BuildRequires:  corrosion
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  zstd

%description
A C++ library for parsing CSS that uses the Rust cssparser crate internally.

%package -n libcxx-rust-cssparser1
Summary:        Library for parsing CSS using the Rust cssparser crate

%description -n libcxx-rust-cssparser1
A C++ library for parsing CSS that uses the Rust cssparser crate internally.

%package devel
Summary:        Library for parsing CSS using the Rust cssparser crate
Requires:       kf6-extra-cmake-modules >= %{kf6_version}
Requires:       libcxx-rust-cssparser1 = %{version}

%description devel
A C++ library for parsing CSS that uses the Rust cssparser crate internally.

%prep
%autosetup -p1 -a3

%build
# vendor.tar.zst contains the crates here
export CARGO_HOME=$PWD/rust

# Tests don't work: ctest calls cargo with --manifest-path, breaking $CARGO_HOME :-/
%cmake_kf6 \
  -DBUILD_DOCS:BOOL=FALSE \
  -DBUILD_TESTING:BOOL=FALSE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libcxx-rust-cssparser1

%files
%{_kf6_bindir}/cxx-rust-cssparser-parse

%files -n libcxx-rust-cssparser1
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libcxx-rust-cssparser.so.*

%files devel
%{_includedir}/cxx-rust-cssparser/
%{_kf6_cmakedir}/cxx-rust-cssparser/
%{_kf6_libdir}/libcxx-rust-cssparser.so

%changelog

