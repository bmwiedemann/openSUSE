#
# spec file for package black-hole-solver
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


%global sover 1
# Missing perl(Env::Path), should also skip some tests like build-process
%global run_tests 0
Name:           black-hole-solver
Version:        1.12.0
Release:        0
Summary:        The Black Hole Solver Executable
License:        MIT
Group:          Amusements/Games/Board/Card
URL:            https://www.shlomifish.org/open-source/projects/black-hole-solitaire-solver/
Source:         https://sourceforge.net/projects/fc-solve/files/fc-solve/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE fix-pkgconfig-libdir.patch -- https://sourceforge.net/p/fc-solve/tickets/1/
Patch0:         fix-pkgconfig-libdir.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  xxhash-devel
BuildRequires:  cmake(Rinutils)
BuildRequires:  perl(Path::Tiny)
%if %{run_tests}
# For testing
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Env::Path)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Some)
%endif

%description
This is a solver, written in C, to solve the Solitaire variant called “Black
Hole” and the one called “All in a Row”. It provides a portable C library, and
a command line application that after being fed with a layout will emit the
cards to move.

%package -n libblack_hole_solver%{sover}
Summary:        Solitaire Solver dynamic libraries
Group:          System/Libraries

%description -n libblack_hole_solver%{sover}
Contains the Black Hole Solitaire dynamic library.

%package devel
Summary:        Black Hole Solver development headers
Group:          Development/Libraries/C and C++
Requires:       libblack_hole_solver%{sover} = %{version}

%description devel
Files needed for building applications against Black Hole Solver.

%prep
%autosetup -p1

%build
%cmake -DFCS_AVOID_TCMALLOC=ON \
  -DUSE_SYSTEM_XXHASH=ON \
  -DBUILD_STATIC_LIBRARY=OFF \
  -DENABLE_DISPLAYING_MAX_NUM_PLAYED_CARDS=ON
%cmake_build

%if %{run_tests}
%check
export FCS_TEST_BUILD=0
export FCS_TEST_WITHOUT_VALGRIND=1
%ctest
%endif

%install
%cmake_install

%post -p /sbin/ldconfig -n libblack_hole_solver1
%postun -p /sbin/ldconfig -n libblack_hole_solver1

%files -n libblack_hole_solver1
%{_libdir}/libblack_hole_solver.so.%{sover}
%{_libdir}/libblack_hole_solver.so.%{sover}.*

%files
%license COPYING
%doc README.md NEWS.asciidoc
%{_bindir}/black-hole-solve
%{_mandir}/*/*

%files devel
%{_libdir}/libblack_hole_solver.so
%{_includedir}/black-hole-solver/
%{_libdir}/pkgconfig/*.pc

%changelog
