#
# spec file for package mccs
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


Name:           mccs
Version:        1.1
Release:        0
Summary:        Multi Criteria CUDF Solver
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            http://www.i3s.unice.fr/~cpjm/misc/mccs.html
Source:         http://www.i3s.unice.fr/~cpjm/misc/mccs-%{version}-srcs.tgz
# PATCH-FIX-UPSTREAM mccs-gcc11-fix.patch badshah400@gmail.com -- Fix compilation with GCC11
Patch0:         mccs-gcc11-fix.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  lpsolve-devel
BuildRequires:  suitesparse-devel

%description
mccs (which stands for Multi Criteria CUDF Solver) is a CUDF problem solver
developed at UNS during the European MANCOOSI project. mccs take as input a
CUDF problem and computes the best solution according to a set of criteria.
It relies on a Integer Programming solver or a Pseudo Boolean solver to achieve
its task. mccs can use a wide set of underlying solvers like Cplex, Gurobi,
Lpsolver, Glpk, CbC, SCIP or WBO.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
# Parallel build does not work
make USELPSOLVE=1 LPSOLVEDIR=%{_libdir} LPSOLVEINC=%{_includedir}/lpsolve CCCOPT="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
cp mccs %{buildroot}%{_bindir}

%files
%doc CHANGES README
%license LICENCE
%{_bindir}/mccs

%changelog
