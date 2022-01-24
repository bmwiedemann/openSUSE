#
# spec file for package stellarsolver
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
Name:           stellarsolver
Version:        1.9
Release:        0
Summary:        Astrometric Solver
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/rlancaste/stellarsolver
Source0:        https://github.com/rlancaste/stellarsolver/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/rlancaste/stellarsolver/pull/88
Patch0:         fix-version.patch
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(wcslib)

%description
An Astrometric Plate Solver for Mac, Linux, and Windows,
built on Astrometry.net and SEP (sextractor).

%package -n libstellarsolver%{sover}
Summary:        Astrometric Solver runtime library
Group:          System/Libraries

%description  -n libstellarsolver%{sover}
An Astrometric Plate Solver for Mac, Linux, and Windows,
built on Astrometry.net and SEP (sextractor), runtime library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libstellarsolver%{sover} = %{version}

%description devel
Development headers and libraries for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

%post -n libstellarsolver%{sover} -p /sbin/ldconfig
%postun -n libstellarsolver%{sover} -p /sbin/ldconfig

%files -n libstellarsolver%{sover}
%license LICENSE
%{_libdir}/libstellarsolver.so.%{sover}
%{_libdir}/libstellarsolver.so.%{version}

%files devel
%license LICENSE
%{_includedir}/libstellarsolver/
%{_libdir}/cmake/StellarSolver/
%{_libdir}/libstellarsolver.so
%{_libdir}/pkgconfig/stellarsolver.pc

%changelog
