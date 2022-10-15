#
# spec file for package cxxopts
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


Name:           cxxopts
Version:        3.0.0
Release:        0
Summary:        Lightweight C++ command line option parser
License:        MIT
URL:            https://github.com/jarro2783/%{name}
Source0:        https://github.com/jarro2783/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
CXXOpts is a lightweight C++ option parser library, supporting the standard
GNU style syntax for options.

%package devel
Summary:        Development files for %{name}
Requires:       libstdc++-devel

%description devel
CXXOpts is a lightweight C++ option parser library, supporting the standard
GNU style syntax for options (development package).

%prep
%autosetup -p1

%build
%cmake \
   -DCXXOPTS_BUILD_EXAMPLES:BOOL=oFF \
   -DCXXOPTS_BUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
