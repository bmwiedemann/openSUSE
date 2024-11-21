#
# spec file for package lager
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


Name:           lager
Version:        0.1.1
Release:        0
Summary:        C++ library to assist value-oriented design
License:        MIT
URL:            https://sinusoid.es/lager/
Source0:        https://github.com/arximboldi/lager/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_system-devel
# For tests
BuildRequires:  cmake(Catch2) < 3.0
BuildRequires:  cmake(Immer)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Zug)
BuildRequires:  cmake(cereal)

%description
lager is a C++ library to assist value-oriented design by implementing the
unidirectional data-flow architecture. It is heavily inspired by Elm and Redux,
and enables composable designs by promoting the use of simple value types and
testable application logic via pure functions.

%package devel
Summary:        C++ library to assist value-oriented design

%description devel
lager is a C++ library to assist value-oriented design by implementing the
unidirectional data-flow architecture. It is heavily inspired by Elm and Redux,
and enables composable designs by promoting the use of simple value types and
testable application logic via pure functions.

%prep
%autosetup -p1

sed -i 's#lib/cmake/Lager#%{_lib}/cmake/Lager#' CMakeLists.txt

%build
# Tests are broken and examples add a dependency on sass
%cmake -Dlager_BUILD_EXAMPLES:BOOL=FALSE \
       -Dlager_BUILD_DEBUGGER_EXAMPLES:BOOL=FALSE \
       -Dlager_BUILD_DOCS:BOOL=FALSE

%cmake_build

%install
%cmake_install

%check
# %%ctest won't work
%{__cmake} --build %{__builddir} %{?_smp_mflags} -t check

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/lager/
%{_libdir}/cmake/Lager/

%changelog
