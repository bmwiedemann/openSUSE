#
# spec file for package dragonbox
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


%define sover 1
Name:           dragonbox
Version:        1.1.3
Release:        0
Summary:        A float-to-string conversion library
License:        Apache-2.0 OR BSL-1.0
Group:          Development/Languages/C and C++
URL:            https://github.com/jk-jeon/dragonbox/
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-SUSE install the header in a sane path
Patch0:         fix-install-path.patch
Patch1:         cmake.patch
BuildRequires:  pkgconfig
# Use cmake3 package on SLE12 because cmake is too old (version 3.5)
%if !0%{?is_opensuse} && 0%{?sle_version} < 150000
# Requires C++17
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++ >= 7
%endif
BuildRequires:  cmake >= 3.5

%description
This library is a reference implementation of Dragonbox in C++.

Dragonbox is a float-to-string conversion algorithm based on a beautiful
algorithm Schubfach, developed by Raffaello Giulietti in 2017-2018.
Dragonbox is further inspired by Grisu and Grisu-Exact.

%package devel
Summary:        Header files for dragonbox, a float-to-string conversion library
Group:          Development/Languages/C and C++

%description devel
This library is a reference implementation of Dragonbox in C++.

Dragonbox is a float-to-string conversion algorithm based on a beautiful
algorithm Schubfach, developed by Raffaello Giulietti in 2017-2018.
Dragonbox is further inspired by Grisu and Grisu-Exact.

This package contains the headers.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1500
export CC="gcc-7"
export CXX="g++-7"
%endif
export CXXFLAGS="-std=c++17"
%cmake -DDRAGONBOX_INSTALL_TO_CHARS=OFF
%cmake_build

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE-*
%dir %{_libdir}/cmake/%{name}-%{version}
%{_libdir}/cmake/%{name}-%{version}/%{name}Targets.cmake
%{_libdir}/cmake/%{name}-%{version}/%{name}Config.cmake
%{_libdir}/cmake/%{name}-%{version}/%{name}ConfigVersion.cmake
%dir %{_includedir}//%{name}
%{_includedir}/%{name}/%{name}.h

%changelog
