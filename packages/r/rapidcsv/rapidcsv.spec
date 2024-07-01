#
# spec file for package rapidcsv
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


Name:           rapidcsv
Version:        8.83
Release:        0
Summary:        C++ header-only library for CSV parsing
License:        BSD-3-Clause
URL:            https://github.com/d99kris/rapidcsv
Source:         https://github.com/d99kris/rapidcsv/archive/refs/tags/v%{version}/rapidcsv-%{version}.tar.gz
Group:          Development/Libraries/C and C++
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  make

%description
Rapidcsv is a C++ header-only library for CSV parsing.
It targets rapid development rather than rapid parsing.

%package devel
Summary:        C++ header-only library for CSV parsing
Group:          Development/Languages/C and C++
BuildArch:      noarch

%description devel
Rapidcsv is a C++ header-only library for CSV parsing.
It targets rapid development rather than rapid parsing.

%prep
%autosetup -p1

%build
# This is a header-only library, we don't build anything but unit-tests
%cmake -DCMAKE_BUILD_TYPE=Debug -DRAPIDCSV_BUILD_TESTS:BOOL=On
%cmake_build

%install
%cmake_install

find examples -perm 0755 -and -type f -exec chmod 0644 {} +
mkdir -p %{buildroot}/%{_docdir}/%{name}-devel
cp -rp examples %{buildroot}/%{_docdir}/%{name}-devel/examples

%fdupes %{buildroot}/%{_prefix}

%check
%ctest

%files devel
%license LICENSE
%doc README.md doc
%{_includedir}/rapidcsv.h
%{_docdir}/%{name}-devel/examples

%changelog
