#
# spec file for package ade
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


%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%bcond_without tests
%bcond_with docs
%bcond_with tutorials

Name:           ade
Version:        0.1.2d
Release:        0
Summary:        Graph construction, manipulation, and processing framework
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://opencv.org/
Source0:        https://github.com/opencv/ade/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ade-use-cxx14-standard.patch gh#opencv/ade#44 badshah400@gmail.com -- Enforce CMAKE_CXX_STANDARD=14 to allow building tests with gtest >= 1.14.0
Patch0:         ade-use-cxx14-standard.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake > 3.2
%if %{with tests}
BuildRequires:  gtest
%endif
%if %{with doc}
BuildRequires:  doxygen
%endif

%description
A graph construction, manipulation, and processing framework. It is suitable
for organizing data flow processing and execution.

%package devel
Summary:        Development files for using ade
Group:          Development/Libraries/C and C++

%description devel
A graph construction, manipulation, and processing framework. It is suitable
for organizing data flow processing and execution.

%prep
%autosetup -p1
# fixup library install directory (i.e. use CMake default)
sed -i -e 's@ DESTINATION lib@ DESTINATION ${CMAKE_INSTALL_LIBDIR}@' sources/ade/CMakeLists.txt

%build
# c++14 is required, at a minimum, for gtest to build tests
%cmake \
  %{?with_tutorials:-DBUILD_ADE_TUTORIAL=ON} \
  %{?with_docs:-DBUILD_ADE_DOCUMENTATION=ON} \
  %{?with_tests:-DGTEST_ROOT:PATH=%{_prefix} \
  -DENABLE_ADE_TESTING=ON} \
  %{nil}

%cmake_build

%install
%cmake_install
%if %{with tests}
rm %{buildroot}%{_bindir}/ade-tests
%endif

%if %{with tests}
%check
%ctest
%endif

%files devel
%license LICENSE
%doc README.md
%{_includedir}/ade
%{_libdir}/*.a
%dir %{_datadir}/ade
%{_datadir}/ade/*.cmake

%changelog
