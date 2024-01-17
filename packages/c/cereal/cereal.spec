#
# spec file for package cereal
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2016 Christoph Junghans
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


Name:           cereal
Version:        1.3.2
Release:        0
Summary:        A header-only C++11 serialization library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://uscilab.github.io/cereal/
Source0:        https://github.com/USCiLab/cereal/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_test-devel

%description
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

%package devel
Summary:        Development headers and libraries for cereal library
Group:          Development/Libraries/C and C++

%description devel
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

This package contains development headers and libraries for the cereal library

%prep
%autosetup -p1

%build
%cmake -DSKIP_PORTABILITY_TEST=ON -DWITH_WERROR=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/cereal
%{_libdir}/cmake/cereal

%changelog
