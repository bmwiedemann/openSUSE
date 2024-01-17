#
# spec file for package cxxopts
#
# Copyright (c) 2023 SUSE LLC
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
Version:        3.1.1
Release:        0
Summary:        C++ command line option parser
License:        MIT
URL:            https://github.com/jarro2783/cxxopts
Source0:        https://github.com/jarro2783/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake

%description
CXXOpts is a C++ option parser library supporting some of the
GNU-style syntax for options.

%package devel
Summary:        Development files for %{name}
Requires:       libstdc++-devel

%description devel
CXXOpts is a C++ option parser library supporting single-letter options
with a single dash, and long options with a double-dash.
(There are some corner cases in 3.0.0 where behavior is not exactly
matching GNU getopt or POSIX mode.)
It requires and makes use of C++11 <regex>.

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
