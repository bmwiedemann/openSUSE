#
# spec file for package fixmath
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


%define sover 1
Name:           fixmath
Version:        2022.07.20
Release:        0
Summary:        Fixed point math operations library
License:        MIT
URL:            https://github.com/PetteriAimonen/libfixmath
Source0:        %{url}/archive/refs/heads/master.tar.gz#:/%{name}-%{version}.tar.gz
# PATCH-FIX-SUSE build shared lib instead of static one
Patch0:         build-shared-library.patch
# PATCH-FIX-SUSE use cmake for installation
Patch1:         cmake-install.patch
BuildRequires:  gcc-c++
# Use cmake3 package on SLE12 because cmake is too old (version 3.5)
%if !0%{?is_opensuse} && 0%{?sle_version} < 150000
BuildRequires:  cmake3-full >= 3.13
# Requires C++17
%else
BuildRequires:  cmake >= 3.13
%endif

%description
fixmath is fix point math operations library.

%package devel
Summary:        Header files for dragonbox, a float-to-string conversion library
Group:          Development/Languages/C and C++

%description devel
fixmath is fix point math operations library.

This package contains the headers and the static library.

%prep
%autosetup -n lib%{name}-master -p1

%build
# Fix lto-no-text-in-archive rpmlint error
export CFLAGS="${CFLAGS} -ffat-lto-objects"
export CXXFLAGS="${CXXFLAGS} -ffat-lto-objects"
%if !0%{?is_opensuse} && 0%{?sle_version} < 150000
# Remove -fsanitize=undefined opts in SLE-12-SP5
sed -e '/set(sanitizer_opts/d' -i tests/tests.cmake
%endif
%cmake
%cmake_build

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/libfixmath
%{_libdir}/lib%{name}.so

%changelog
