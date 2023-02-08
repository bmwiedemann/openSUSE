#
# spec file for package pegtl
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


Name:           pegtl
Summary:        Parsing Expression Grammar (PEG) Template Library
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/taocpp/PEGTL
Version:        3.2.7
Release:        0
BuildRequires:  cmake >= 3.8.0
BuildRequires:  gcc-c++
Source0:        https://github.com/taocpp/PEGTL/archive/%{version}.tar.gz
BuildArch:      noarch

%description
The Parsing Expression Grammar Template Library (PEGTL) is a C++11
library for creating parsers according to a Parsing Expression
Grammar (PEG).

%package devel
Summary:        Parsing Expression Grammar (PEG) Template Library
Group:          Development/Languages/C and C++

%description devel
The Parsing Expression Grammar Template Library (PEGTL) is a C++11
library for creating parsers according to a Parsing Expression
Grammar (PEG). Grammars are embedded as regular C++ code, and
consist of template hierarchies of classes. These hierarchies
naturally correspond to the inductive definition of PEGs. The
library extends on the subject of PEGs with new expression types,
actions that can be attached to grammar rules, and mechanisms to
ensure helpful diagnostics in case of parsing errors.

%package devel-doc
Summary:        Parsing Expression Grammar (PEG) Template Library
Group:          Documentation/Other

%description devel-doc
This package contains the development documentation for
PEGTL (Parsing Expression Grammar Template Library).

%prep
%setup -q -n PEGTL-%version

%build
# Fix build with GCC 10; To be removed upon upgrade to 3.x (https://github.com/taocpp/PEGTL/issues/217)
export CXXFLAGS="%{optflags} -Wno-error=type-limits"
%cmake \
  -DPEGTL_INSTALL_DOC_DIR:PATH=%{_defaultdocdir}/pegtl \
  -DPEGTL_INSTALL_CMAKE_DIR:PATH=%{_datadir}/cmake/Modules \
  -DPEGTL_BUILD_EXAMPLES:BOOL=OFF \
  -DPEGTL_BUILD_TESTS:BOOL=ON

%cmake_build

%install
%cmake_install
rm %{buildroot}%{_defaultdocdir}/pegtl/LICENSE

%check
%ctest

%files devel
%{_includedir}/*
%{_datadir}/cmake/Modules

%files devel-doc
%license LICENSE
%doc README.md doc/*

%changelog
