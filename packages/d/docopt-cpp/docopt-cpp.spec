#
# spec file for package docopt-cpp
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


%define lib_name libdocopt0

Name:           docopt-cpp
Version:        0.6.3
Release:        0
Summary:        C++11 library for creating an option parser from docstrings
License:        MIT
URL:            https://github.com/docopt/docopt.cpp
Source:         https://github.com/docopt/docopt.cpp/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  c++_compiler

%description
Library for creating an option parser from a docstring.

%package devel
Summary:        Developmment files for libdocopt
Requires:       %{lib_name} = %{version}

%description devel
This package contains the development files for libdocopt

%package -n %{lib_name}
Summary:        C++11 library for creating an option parser from docstrings

%description -n %{lib_name}
Library for creating an option parser from a docstring.

%prep
%autosetup -p1 -n docopt.cpp-%{version}

%build
export CXXFLAGS="-ffat-lto-objects"
%cmake
%cmake_build

%install
%cmake_install
rm -fv %{buildroot}/%{_libdir}/*.a

%ldconfig_scriptlets -n %{lib_name}

%files -n %{lib_name}
%license LICENSE-MIT
%{_libdir}/libdocopt.so.*

%files devel
%license LICENSE-MIT
%doc README.rst
%{_includedir}/docopt
%{_libdir}/cmake/docopt
%{_libdir}/libdocopt.so
%{_libdir}/pkgconfig/docopt.pc

%changelog
