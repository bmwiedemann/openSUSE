#
# spec file for package zug
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


Name:           zug
Version:        0.1.1
Release:        0
Summary:        Transducers for C++
License:        BSL-1.0
URL:            https://sinusoid.es/zug/
Source0:        https://github.com/arximboldi/zug/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/arximboldi/zug/issues/45
Patch0:         zug-gcc15.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
# includes catch2/catch.hpp
BuildRequires:  cmake(Catch2) < 3.0

%description
zug is a C++ library providing transducers. Transducers are composable
sequential transformations independent of the source. They can be used to
express algorithms over pull-based sequences (iterators, files) but also push
based sequences (signals, events, asynchronous streams) in a generic way.

%package devel
Summary:        Transducers for C++

%description devel
zug is a C++ library providing transducers. Transducers are composable
sequential transformations independent of the source. They can be used to
express algorithms over pull-based sequences (iterators, files) but also push
based sequences (signals, events, asynchronous streams) in a generic way.

%prep
%autosetup -p1

sed -i 's#lib/cmake/Zug#%{_lib}/cmake/Zug#' CMakeLists.txt

%build
%cmake -Dzug_BUILD_EXAMPLES=FALSE \
       -Dzug_BUILD_DOCS:BOOL=FALSE

%cmake_build

%install
%cmake_install

%check
# %%ctest won't work
%{__cmake} --build %{__builddir} %{?_smp_mflags} -t check

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/zug/
%{_libdir}/cmake/Zug/

%changelog
