#
# spec file for package jsonnet
#
# Copyright (c) 2021 SUSE LLC
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


Name:           jsonnet
Version:        0.17.0
Release:        0
Summary:        C++ implementation of Jsonnet
License:        Apache-2.0
URL:            https://github.com/google/jsonnet
Source:         https://github.com/google/jsonnet/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          %{name}-%{version}.dif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest

%description
This an implementation of Jsonnet in C++.

%prep
%setup -q
%autopatch -p0

%build
%cmake -DUSE_SYSTEM_GTEST=ON -DBUILD_STATIC_LIBS=ON -DBUILD_SHARED_BINARIES=OFF
%cmake_build

%install
%cmake_install
# We don't want the libraries and header files
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_includedir}

%files
%license LICENSE
%{_bindir}/jsonnet
%{_bindir}/jsonnetfmt

%changelog
