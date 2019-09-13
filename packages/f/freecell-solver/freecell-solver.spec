#
# spec file for package freecell-solver
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           freecell-solver
Version:        5.0.0
Release:        0
Summary:        A Freecell Solver
License:        MIT
Group:          Amusements/Games/Other
URL:            http://fc-solve.shlomifish.org
Source0:        http://fc-solve.shlomifish.org/downloads/fc-solve/%{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  perl-Template-Toolkit
BuildRequires:  pkgconfig
BuildRequires:  python3-random2
BuildRequires:  python3-six
BuildRequires:  perl(Path::Tiny)

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
# This dependency is expected
Group:          System/Libraries
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
       -DFCS_WITH_TEST_SUITE=OFF \
       -DFCS_AVOID_TCMALLOC=ON
%make_jobs

%install
%cmake_install

# Fix the rpmlint warnings
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
%license COPYING.asciidoc
%{_includedir}/freecell-solver/
%{_libdir}/libfreecell-solver.so
%{_libdir}/pkgconfig/libfreecell-solver.pc

%files -n %{name}-presets
%license COPYING.asciidoc
%{_datadir}/freecell-solver/

%files
%license COPYING.asciidoc
%doc %{_datadir}/doc/freecell-solver/
%doc AUTHORS.asciidoc NEWS.asciidoc README.asciidoc USAGE.asciidoc
%{_bindir}/*freecell*
%{_bindir}/fc*
%{_bindir}/gen-multiple-pysol-layouts
%{_mandir}/man6/*

%changelog
