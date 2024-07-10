#
# spec file for package minisat
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


Name:           minisat
URL:            http://minisat.se/MiniSat.html
Version:        2.2.1+20200902
Release:        0
Summary:        SAT solver
License:        MIT
Group:          Development/Tools/Other
Source0:        %{name}-%{version}.tar.xz
Patch0:         CMakeLists-use-absolute-libdir-in-rpath-handling.patch
Patch1:         0001-CMakeLists-support-different-lib-dirs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  zlib-devel

%description
MiniSat is a comparatively small SAT solver with documentation
(through the following paper). The first version was just above 600
lines while containing many then-desirable features (conflict-clause
recording, conflict-driven backjumping, VSIDS dynamic variable order,
two-literal watch scheme), and even extensions for incremental SAT
and for non-clausal constraints over boolean variables.

The current MiniSat v2 supports variable elimination style
simplification, too.

%package -n libminisat2
Summary:        SAT solver
Group:          System/Libraries

%description -n libminisat2
MiniSat is a comparatively small SAT solver. It can do
conflict-clause recording, conflict-driven backjumping, VSIDS dynamic
variable order, two-literal watch scheme, non-clausal constraints
over boolean variables, and variable elimination style
simplification.

%package devel
Summary:        Devel files for minisat
Group:          Development/Libraries/C and C++
Requires:       libminisat2 = %{version}
Requires:       zlib-devel

%description devel
Headers and libraries for the minisat package.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake -DMINISAT_INSTALL_CMAKE_DIR=%{_libdir}/cmake/%{name}
%make_jobs

%install
%cmake_install

%post   -n libminisat2 -p /sbin/ldconfig
%postun -n libminisat2 -p /sbin/ldconfig

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}_core

%files -n libminisat2
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so

%changelog
