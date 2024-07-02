#
# spec file for package expected-lite
#
# Copyright (c) 2020 SUSE LLC
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


Name:           expected-lite
Version:        0.8.0
Release:        0
Summary:        Expected objects in C++11 and later in a single-file header-only library
License:        BSL-1.0
URL:            https://github.com/martinmoene/expected-lite
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
expected lite: Expected objects in C++11 and later in a single-file header-only library

%package devel
Summary:        Expected objects in C++11 
Group:          Development/Libraries/C and C++
Requires:       libstdc++-devel

%description devel
Development files for a header-only library

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.txt
%doc CHANGES.txt README.md
%{_includedir}/nonstd/
%{_libdir}/cmake/expected-lite/

%changelog
