#
# spec file for package freecell-solver
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


%bcond_with tests
%define soversion 0
%define libname libfreecell-solver
Name:           freecell-solver
Version:        6.2.0
Release:        0
Summary:        A Freecell Solver
License:        MIT
Group:          Amusements/Games/Other
URL:            https://fc-solve.shlomifish.org
Source0:        http://fc-solve.shlomifish.org/downloads/fc-solve/%{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.5
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  perl-Template-Toolkit
BuildRequires:  pkgconfig
BuildRequires:  python3-cffi
BuildRequires:  python3-pysol-cards
BuildRequires:  python3-random2
BuildRequires:  python3-six
BuildRequires:  cmake(Rinutils)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Path::Tiny)
%if %{with tests}
BuildRequires:  perl(Task::FreecellSolver::Testing)
%endif

%description
Command line programs which can be used to solve Freecell and other card games.

%package -n %{name}-presets
Summary:        Freecell Solver presets
Group:          Amusements/Games/Other
BuildArch:      noarch

%description -n %{name}-presets
Command line programs which can be used to solve Freecell and other card games.
This package contains the presets used to solve the games.

%package -n %{libname}%{soversion}
Summary:        Freecell Solver library
Group:          System/Libraries
# This dependency is expected
Requires:       %{name}-presets = %{version}

%description -n %{libname}%{soversion}
This package contains the Freecell Solver library which can be used by some
programs to solves Freecell and other card games.

%package devel
Summary:        Freecell Solver development package
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{soversion} = %{version}

%description devel
Development package for the libfreecell-solver library

%prep
%setup -q

%build
%cmake -DBUILD_STATIC_LIBRARY=OFF \
%if %{without tests}
       -DFCS_WITH_TEST_SUITE=OFF \
%endif
       -DFCS_AVOID_TCMALLOC=ON
%cmake_build

%if %{with tests}
%check
%ctest
%endif

%install
%cmake_install

# Fix the rpmlint warnings
rm -v %{buildroot}%{_datadir}/doc/freecell-solver/INSTALL
sed -i 's#%{_bindir}/env python3#%{_bindir}/python3#' %{buildroot}%{_bindir}/*.py
sed -i 's#%{_bindir}/env python3#%{_bindir}/python3#' %{buildroot}%{_bindir}/gen-multiple-pysol-layouts
sed -i '/^#!\/bin/d' %{buildroot}%{_datadir}/freecell-solver/presets/*.sh
%fdupes -s %{buildroot}%{_mandir}

%post   -n %{libname}%{soversion} -p /sbin/ldconfig
%postun -n %{libname}%{soversion} -p /sbin/ldconfig

%files -n %{libname}%{soversion}
%license COPYING.asciidoc
%{_libdir}/libfreecell-solver.so.*

%files devel
%{_includedir}/freecell-solver/
%{_libdir}/libfreecell-solver.so
%{_libdir}/pkgconfig/libfreecell-solver.pc

%files -n %{name}-presets
%{_datadir}/freecell-solver/

%files
%doc %{_datadir}/doc/freecell-solver/
%{_bindir}/dbm-fc-solver
%{_bindir}/depth-dbm-fc-solver
%{_bindir}/*freecell*
%{_bindir}/fc*
%{_bindir}/gen-multiple-pysol-layouts
%{_mandir}/man6/*

%changelog
