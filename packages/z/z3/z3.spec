#
# spec file for package z3
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define python_subpackage_only 1
%define sover %(echo %{version} | sed 's@\\([0-9]*\\)\\.\\([0-9]*\\)\\..*@\\1_\\2@')
Name:           z3
Version:        5.1.0
Release:        0
Summary:        Theorem prover from Microsoft Research
License:        MIT
URL:            https://github.com/Z3Prover/z3/wiki
Source0:        https://github.com/Z3Prover/z3/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        python-z3-pyproject.toml
Source2:        python-z3-setup.py
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 44}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.16
BuildRequires:  fdupes
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%{?python_enable_dependency_generator}
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(gmpxx)
%else
BuildRequires:  gmp-devel
%endif
%python_subpackages

%description
Z3 is a satisfiability modulo theories (SMT) solver; given a set of
constraints with variables, it reports a set of values for those
variables that would meet the constraints.  The Z3 input format is an
extension of the one defined by the SMT-LIB 2.0 standard.  Z3 supports
arithmetic, fixed-size bit-vectors, extensional arrays, datatypes,
uninterpreted functions, and quantifiers.

%package -n libz3-%{sover}
Summary:        Library for the Z3 SMT theorem prover

%description -n libz3-%{sover}
Z3 is a Satisfiability Modulo Theories (SMT) solver and integrates
several decision procedures.

This subpackage contains the Z3 runtime library needed for Z3 and
other projects.

%package devel
Summary:        Development files for Z3
Requires:       libz3-%{sover} = %{version}

%description devel
Development files for the Z3 library.

%package -n python-%{name}
Summary:        Python bindings for %{name}
Requires:       libz3-%{sover} = %{version}
Provides:       python3-z3 = %{version}-%{release}
Obsoletes:      python3-z3 < %{version}-%{release}
BuildArch:      noarch

%description -n python-%{name}
Z3 is a theorem prover from Microsoft Research.

Python bindings for the module.

%prep
%autosetup -p1 -n z3-z3-%{version}

%build
%define __builder ninja
%cmake \
  -DZ3_BUILD_LIBZ3_SHARED=true \
  -DZ3_USE_LIB_GMP=true \
  -DZ3_BUILD_PYTHON_BINDINGS=true \
  -DZ3_INSTALL_PYTHON_BINDINGS=false \
  -DZ3_ENABLE_EXAMPLE_TARGETS=false \
  -DZ3_LINK_TIME_OPTIMIZATION=true

%cmake_build

mkdir -p python-wheel
cp %{SOURCE1} python-wheel/pyproject.toml
cp %{SOURCE2} python-wheel/setup.py
cp -a python/z3 python-wheel/

pushd python-wheel
export Z3_VERSION=%{version}
%pyproject_wheel
popd

%install
%cmake_install
pushd build/python-wheel
%pyproject_install
popd

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Upstream calls neither enable_testing() nor add_test(), so %%ctest finds no
# tests at all. The unit tests live in the EXCLUDE_FROM_ALL target test-z3,
# which has to be built and invoked explicitly ("/a" = run all of them).
# The Python singlespec macros stash the CMake build directory away as
# _build.tmp while they switch flavours in %%install, so restore it first.
[ -d %{__builddir} ] || mv _build.tmp %{__builddir}
pushd %{__builddir}
%cmake_build test-z3
./test-z3 /a
popd

%ldconfig_scriptlets -n libz3-%{sover}

%files
%license LICENSE.txt
%doc README.md RELEASE_NOTES.md
%{_bindir}/z3

%files -n libz3-%{sover}
%license LICENSE.txt
%{_libdir}/libz3.so.*

%files devel
%license LICENSE.txt
%{_includedir}/z3*.h
%{_libdir}/libz3.so
%{_libdir}/pkgconfig/z3.pc
%dir %{_libdir}/cmake/z3/
%{_libdir}/cmake/z3/Z3Config.cmake
%{_libdir}/cmake/z3/Z3ConfigVersion.cmake
%{_libdir}/cmake/z3/Z3Targets*

%files %{python_files z3}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/z3/
%{python_sitelib}/z3_solver-%{version}*.dist-info/

%changelog
