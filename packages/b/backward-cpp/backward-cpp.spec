#
# spec file for package backward-cpp
#
# Copyright (c) 2021 SUSE LLC
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


Name:           backward-cpp
Version:        1.5
Release:        0
Summary:        Stack trace printer for C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/bombela/backward-cpp
Source:         https://github.com/bombela/backward-cpp/archive/v%{version}.tar.gz#/backward-cpp-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
backward-cpp is a C++ library which prints stack traces on errors or
segmentation faults.

%package devel
Summary:        Development files for backward-cpp
Group:          Development/Libraries/C and C++

%description devel
Development files for backward-cpp, a stack trace printer for C++.

%prep
%autosetup -n backward-cpp-%{version}

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md

%files devel
%{_includedir}/backward.hpp
%{_libdir}/backward
%{_libdir}/backward/BackwardConfig.cmake

%changelog
