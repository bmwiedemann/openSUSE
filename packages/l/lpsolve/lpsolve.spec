#
# spec file for package lpsolve
#
# Copyright (c) 2026 SUSE LLC
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

%define libname liblpsolve55-0

Name:           lpsolve
Version:        5.5.2.14
Release:        0
Summary:        A Mixed Integer Linear Programming (MILP) Solver
# Per-file license audit (same conclusion as Fedora's):
#   most sources, README.txt and LICENSE: LGPL-2.1-or-later
#   lp_rlp.c (Bison-generated parser): GPL-2.0-or-later WITH Bison-exception-2.2
#   colamd/ (re-added by the Rebase-COLAMD patch): BSD-3-Clause
License:        LGPL-2.1-or-later AND GPL-2.0-or-later WITH Bison-exception-2.2 AND BSD-3-Clause
URL:            https://lp-solve.github.io/
# Repackaged from https://github.com/lp-solve/lp_solve/releases/download/%%{version}/lp_solve_%%{version}_source.tar.gz
# with the non-free colamd/colamd.{c,h} removed; COLAMD 3.0.4 sources are
# added back by lp_solve-5.5.2.11-Rebase-COLAMD-to-3.0.4.patch.
Source0:        lp_solve-%{version}-repackaged.tar.gz
# Use system-wide compiler and linker flags
Patch0:         lp_solve-5.5.2.14-Respect-CC-CFLAGS-and-LDFLAGS.patch
# Link the lp_solve tool against the shared library instead of
# statically duplicating all of its objects
Patch1:         lp_solve-5.5.2.11-Link-a-tool-to-a-shared-library.patch
# Rebase bundled COLAMD to 3.0.4 (1/2)
Patch2:         lp_solve-5.5.2.11-Rebase-COLAMD-to-3.0.4.patch
# Rebase bundled COLAMD to 3.0.4 (2/2): port lp_MDO to the new API
Patch3:         lp_solve-5.5.2.11-Port-lp_MDO-to-colamd-3.0.4.patch
# Build the shared library with a versioned SONAME (shlib policy)
Patch4:         lp_solve-5.5.2.14-versioned-soname.patch
BuildRequires:  binutils
BuildRequires:  gcc
BuildRequires:  grep
# The lp_solve tool links against the shared library
Requires:       %{libname} = %{version}

%description
Mixed Integer Linear Programming (MILP) solver lpsolve solves pure
linear, (mixed) integer/binary, semi-continuous and special ordered
sets (SOS) models.

%package -n %{libname}
Summary:        A Mixed Integer Linear Programming (MILP) Solver Library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later WITH Bison-exception-2.2 AND BSD-3-Clause
# The library keeps its historic subpackage name; libreoffice and
# mccs link against it. SONAME is liblpsolve55.so.0, the unversioned
# linker symlink ships in -devel.
Provides:       bundled(colamd) = 3.0.4

%description -n %{libname}
Mixed Integer Linear Programming (MILP) solver library lpsolve solves
pure linear, (mixed) integer/binary, semi-continuous and special
ordered sets (SOS) models.

%ldconfig_scriptlets -n %{libname}

%package devel
Summary:        Development files for lpsolve
License:        LGPL-2.1-or-later
Requires:       %{libname} = %{version}

%description devel
Header files for developing with the lpsolve library.

%prep
%autosetup -p1 -n lp_solve
mv colamd/License.txt colamd/colamd_license

%build
export CFLAGS="%{optflags}"
pushd lpsolve55
sh -x ccc
rm bin/ux*/liblpsolve55.a
popd
pushd lp_solve
sh -x ccc
popd

%install
install -d %{buildroot}%{_bindir} %{buildroot}%{_libdir} %{buildroot}%{_includedir}/lpsolve
install -p -m 755 lp_solve/bin/ux*/lp_solve %{buildroot}%{_bindir}/
install -p -m 755 lpsolve55/bin/ux*/liblpsolve55.so.0 %{buildroot}%{_libdir}/
ln -s liblpsolve55.so.0 %{buildroot}%{_libdir}/liblpsolve55.so
install -p -m 644 lp*.h yacc_read.h %{buildroot}%{_includedir}/lpsolve/

%check
LP_PATH="$(echo lpsolve55/bin/ux*)"
# The library must carry the versioned SONAME and the tool must
# record it as NEEDED (shlib packaging policy)
readelf -d "$LP_PATH/liblpsolve55.so.0" | grep -q 'SONAME.*\[liblpsolve55.so.0\]'
readelf -d lp_solve/bin/ux*/lp_solve | grep -q 'NEEDED.*\[liblpsolve55.so.0\]'
# Verify the lp_solve tool works
echo 'max: x; x < 42;' | \
    LD_LIBRARY_PATH="$LP_PATH" ./lp_solve/bin/ux*/lp_solve -S1 | \
    grep -e ': 42\.0*$'
# Verify a demo program builds and runs against the shared library
cc %{optflags} -I. demo/demo.c -L"$LP_PATH" -llpsolve55
LD_LIBRARY_PATH="$LP_PATH" ./a.out </dev/null

%files
%license colamd/colamd_license LICENSE
%doc README.txt
%{_bindir}/lp_solve

%files -n %{libname}
%{_libdir}/liblpsolve55.so.0*

%files devel
%doc demo/demo.c
%{_includedir}/lpsolve
%{_libdir}/liblpsolve55.so

%changelog
