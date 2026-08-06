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
Version:        5.0.0
Release:        0
Summary:        Theorem prover from Microsoft Research
License:        MIT
Group:          Productivity/Scientific/Other
URL:            https://github.com/Z3Prover/z3/wiki
Source0:        https://github.com/Z3Prover/z3/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        python-z3-pyproject.toml
Source2:        python-z3-setup.py
# PATCH-FIX-UPSTREAM python-use-non-devel-so.patch bsc#1243028 mcepl@suse.com
# load libz3 with soversion (from gh#Z3Prover/z3#7518)
Patch0:         python-use-non-devel-so.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 44}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  help2man
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%{?python_enable_dependency_generator}
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13-c++
%else
BuildRequires:  c++_compiler
%endif
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
Group:          System/Libraries

%description -n libz3-%{sover}
Z3 is a Satisfiability Modulo Theories (SMT) solver and integrates
several decision procedures.

This subpackage contains the Z3 runtime library needed for Z3 and
other projects.

%package devel
Summary:        Development files for Z3
Group:          Development/Languages/C and C++
Requires:       libz3-%{sover} = %{version}

%description devel
Development files for the Z3 library.

%package -n python-%{name}
Summary:        Python bindings for %{name}
Group:          Development/Languages/Python
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
%if 0%{?suse_version} < 1600
export CXX=g++-13
%endif

%cmake \
  -DZ3_BUILD_LIBZ3_SHARED=true \
  -DZ3_USE_LIB_GMP=true \
  -DZ3_BUILD_PYTHON_BINDINGS=true \
  -DZ3_INSTALL_PYTHON_BINDINGS=false \
  -DZ3_ENABLE_EXAMPLE_TARGETS=false \
%if 0%{?suse_version} >= 1550
  -DZ3_LINK_TIME_OPTIMIZATION=true
%else
  -DZ3_LINK_TIME_OPTIMIZATION=false
%endif

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
%ctest

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
