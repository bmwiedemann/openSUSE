#
# spec file for package frozen
#
# Copyright (c) 2022 SUSE LLC
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

Name:           frozen
Version:        1.1.1
Release:        0
Summary:        A header only, constexpr alternative to gperf for C++14 users
License:        Apache-2.0
URL:            https://github.com/serge-sans-paille/%{name}
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#:/%{name}-%{version}.tar.gz
Patch0:         frozen-cmake.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Header-only library that provides 0 cost initialization for immutable
containers, fixed-size containers, and various algorithms.

%package devel
Summary:        Header files for frozen, an alternative to gperf
Group:          Development/Languages/C and C++
BuildArch:      noarch

%description devel
Header-only library that provides 0 cost initialization for immutable
containers, fixed-size containers, and various algorithms.

This package contains the headers.

%prep
%autosetup -p1

# The previous empty line is allowing buiding on sle12, where autosetup is buggy

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files devel
%doc README.rst
%license LICENSE
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%dir %{_datadir}/cmake/%{name}
%{_datadir}/cmake/%{name}/*

%changelog
