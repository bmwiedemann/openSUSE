#
# spec file for package freecell-solver
#
# Copyright (c) 2024 SUSE LLC
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


%define soversion 0
%define libname libfreecell-solver
%bcond_with tests
Name:           freecell-solver
Version:        6.12.0
Release:        0
Summary:        A Freecell Solver
License:        MIT
URL:            https://fc-solve.shlomifish.org
Source0:        https://fc-solve.shlomifish.org/downloads/fc-solve/%{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.5
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  perl-Template-Toolkit
BuildRequires:  pkgconfig
BuildRequires:  cmake(Rinutils)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  pkgconfig(glib-2.0)
Requires:       python3-pysol-cards
Requires:       python3-random2
Requires:       python3-six
%if %{with tests}
BuildRequires:  python3-cffi
BuildRequires:  python3-pysol-cards
BuildRequires:  python3-random2
BuildRequires:  python3-six
BuildRequires:  perl(Task::FreecellSolver::Testing)
%endif

%description
Command line programs which can be used to solve Freecell and other card games.

%package -n %{name}-presets
Summary:        Freecell Solver presets
BuildArch:      noarch

%description -n %{name}-presets
Command line programs which can be used to solve Freecell and other card games.
This package contains the presets used to solve the games.

%package -n %{libname}%{soversion}
Summary:        Freecell Solver library
# This dependency is expected
Requires:       %{name}-presets = %{version}

%description -n %{libname}%{soversion}
This package contains the Freecell Solver library which can be used by some
programs to solves Freecell and other card games.

%package devel
Summary:        Freecell Solver development package
Requires:       %{libname}%{soversion} = %{version}

%description devel
Development package for the libfreecell-solver library

%prep
%autosetup -p1

# Unneeded 3rdparty module
rm -r rinutils

%build
%cmake -DBUILD_STATIC_LIBRARY:BOOL=FALSE \
       -DCMAKE_INSTALL_DOCDIR:STRING=%{_datadir}/doc/freecell-solver \
%if %{without tests}
       -DFCS_WITH_TEST_SUITE:BOOL=FALSE -D_PYTHON3=_PYTHON3-NOTFOUND \
%endif
       -DFCS_AVOID_TCMALLOC:BOOL=TRUE

%cmake_build

%if %{with tests}
%check
%ctest
%endif

%install
%cmake_install

# Fix the rpmlint warnings
rm -v %{buildroot}%{_datadir}/doc/freecell-solver/INSTALL
sed -i 's#%{_bindir}/env python3$#%{_bindir}/python3#' %{buildroot}%{_bindir}/*.py
sed -i 's#%{_bindir}/env python3$#%{_bindir}/python3#' %{buildroot}%{_bindir}/gen-multiple-pysol-layouts
sed -i '/^#!\/bin/d' %{buildroot}%{_datadir}/freecell-solver/presets/*.sh
%fdupes -s %{buildroot}%{_mandir}

%ldconfig_scriptlets -n %{libname}%{soversion}

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
