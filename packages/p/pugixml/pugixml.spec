#
# spec file for package pugixml
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


%define _libname libpugixml1
Name:           pugixml
Version:        1.15
Release:        0
Summary:        Light-weight C++ XML Processing Library
License:        MIT
Group:          System/Libraries
URL:            https://pugixml.org/
Source0:        https://github.com/zeux/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         pugixml-config.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
pugixml is a light-weight C++ XML processing library. It features:

- DOM-like interface with rich traversal/modification capabilities
- Extremely fast non-validating XML parser which constructs the DOM tree from
  an XML file/buffer
- XPath 1.0 implementation for complex data-driven tree queries
- Full Unicode support with Unicode interface variants and automatic encoding
  conversions

%package devel
Summary:        Development Files for pugixml
Group:          Development/Libraries/C and C++
Requires:       %{_libname} = %{version}

%description devel
This package provides development libraries and headers needed to build
software using pugixml.

%package -n %{_libname}
Summary:        Light-weight C++ XML Processing Library
Group:          System/Libraries

%description -n %{_libname}
pugixml is a light-weight C++ XML processing library. It features:

- DOM-like interface with rich traversal/modification capabilities
- Extremely fast non-validating XML parser which constructs the DOM tree from
  an XML file/buffer
- XPath 1.0 implementation for complex data-driven tree queries
- Full Unicode support with Unicode interface variants and automatic encoding
  conversions

%prep
%autosetup -p1

%build
%cmake -DPUGIXML_BUILD_TESTS=ON
%make_build

%install
%cmake_install

%post -n %{_libname} -p /sbin/ldconfig
%postun -n %{_libname} -p /sbin/ldconfig

%check
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150300
# Tweak path to find libpugixml.so.1 for Leap 15.3 and older
export LD_LIBRARY_PATH="$PWD/build"
%endif
%ctest

%files devel
%doc readme.txt docs/*
%{_includedir}/*.hpp
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so

%files -n %{_libname}
%{_libdir}/libpugixml.so.*

%changelog
