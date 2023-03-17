#
# spec file for package fixmath
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


Name:           fixmath
Version:        2022.07.20
Release:        0
Summary:        Fixed-point math operations library
License:        MIT
URL:            https://github.com/PetteriAimonen/libfixmath
Group:          Development/Libraries/C and C++
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
fixmath is a fixed-point math operations library written in C and
implementing the Q16.16 format.

%package devel
Summary:        Header files for fixmath, a fixed-point math library
Requires:       %name = %version
Conflicts:      %name < %version-%release

%description devel
fixmath is a fixed-point math operations library written in C and
implementing the Q16.16 format.

This package contains the headers.

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
sv="$PWD/fixmath.sym"
echo "FIXMATH_%version { global: *; };" >"$sv"
%cmake -DCMAKE_SHARED_LINKER_FLAGS:STRING="-Wl,--version-script=$sv"
%cmake_build

%install
%cmake_install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/lib%{name}.so

%files devel
%doc README.md
%license LICENSE
%{_includedir}/libfixmath

%changelog
