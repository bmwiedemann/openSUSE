#
# spec file for package Imath
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


%global so_suffix -3_1
%define sonum     29
Name:           Imath
Version:        3.1.6
Release:        0
Summary:        C++ and Python Library of 2D and 3D Vector, Matrix, and Math Operations
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.openexr.com/
Source0:        https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v%{version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Imath is a library for the C++ representation of 2D and 3D vectors
and matrices and other mathematical objects, functions, and data
types common in computer graphics applications, including the “half”
16-bit floating-point type.

%package devel
Summary:        Base library for ILM software (OpenEXR)
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libImath%{so_suffix}-%{sonum} = %{version}
Requires:       libstdc++-devel
# provides ilmbase-devel partly only; openexr-devel requires Imath-devel
# and provides/obsoletes it
Obsoletes:      ilmbase-devel < 3.0

%description devel
Devel files for Imath, which is the base library for OpenEXR.

%package -n libImath%{so_suffix}-%{sonum}
Summary:        Vector/matrix library for OpenEXR
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libImath%{so_suffix}-%{sonum}
%{summary}.

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install

%check
# https://github.com/openexr/openexr/issues/570
%ifnarch i586
export LD_LIBRARY_PATH="$PWD/build/src/Imath:$LD_LIBRARY_PATH"
%ctest
%endif

%post -n libImath%{so_suffix}-%{sonum} -p /sbin/ldconfig
%postun -n libImath%{so_suffix}-%{sonum} -p /sbin/ldconfig

%files devel
%doc CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%license LICENSE.md
%{_includedir}/Imath
%{_libdir}/libImath.so
%{_libdir}/libImath%{so_suffix}.so
%{_libdir}/pkgconfig/Imath.pc
%dir %{_libdir}/cmake/Imath/
%{_libdir}/cmake/Imath/*.cmake

%files -n libImath%{so_suffix}-%{sonum}
%{_libdir}/libImath%{so_suffix}.so.%{sonum}*

%changelog
