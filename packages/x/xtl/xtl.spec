#
# spec file for package xtl
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


Name:           xtl
Version:        0.6.18
Release:        0
Summary:        The x template library
License:        BSD-3-Clause
URL:            https://github.com/xtensor-stack/xtl
Source:         https://github.com/xtensor-stack/xtl/archive/%{version}.tar.gz#/xtl-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  cmake(nlohmann_json)

%description
Basic tools (containers, algorithms) used by other quantstack packages.

%package        devel
Summary:        The x template library
Requires:       cmake(nlohmann_json)

%description    devel
Basic tools (containers, algorithms) used by other quantstack packages.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/xtl/
%{_libdir}/cmake/xtl/
%{_libdir}/pkgconfig/xtl.pc

%changelog
