#
# spec file for package cpptoml
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cpptoml
Version:        0.1.1
Release:        0
Summary:        Header-only c++ library for parsing TOML
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/skystrife/%{name}
Source:         https://github.com/skystrife/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++

%description
cpptoml is a header-only c++ library for parsing TOML configuration files.

%package devel
Summary:        Header-only c++ library for parsing TOML
Group:          Development/Languages/C and C++

%description devel
cpptoml is a header-only c++ library for parsing TOML configuration files.

This package contains development headers for the cpptoml library

%prep
%setup -q
sed -ie "s,lib/cmake/cpptoml,%{_libdir}/cmake/%{name}," CMakeLists.txt

%build
%cmake
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/cpptoml.h
%{_libdir}/cmake/%{name}

%changelog
