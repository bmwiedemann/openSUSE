#
# spec file for package valijson
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


Name:           valijson
Version:        1.0.2
Release:        0
Summary:        Header-only C++ library for JSON Schema validation
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/tristanpenman/valijson
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++

%description
Valijson is a header-only JSON Schema validation library for C++11.

Valijson provides a simple validation API that allows you to load JSON Schemas,
and validate documents loaded by one of several supported parser libraries.

%package devel
Summary:        Development headers for valijson
Group:          Development/Libraries/C and C++

%description devel
This package provides development headers for valijson, a JSON Schema
validation library for C++11.

%prep
%autosetup -p1

%build
%cmake

%install
%cmake_install

%files devel
%dir %{_includedir}/valijson/
%{_includedir}/valijson/*
%dir %{_includedir}/compat/
%{_includedir}/compat/optional.hpp
%dir %{_libdir}/cmake/valijson/
%{_libdir}/cmake/valijson/valijsonConfig.cmake
%license LICENSE
%doc README.md

%changelog
