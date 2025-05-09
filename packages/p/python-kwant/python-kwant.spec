#
# spec file for package python-kwant
#
# Copyright (c) 2025 SUSE LLC
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


%define modname kwant
%{?sle15_python_module_pythons}
Name:           python-kwant
Version:        1.5.0
Release:        0
Summary:        Python library for numerical quantum transport calculations
License:        BSD-2-Clause
URL:            https://kwant-project.org/
Source0:        https://files.pythonhosted.org/packages/source/k/kwant/kwant-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.18}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  blas-devel
BuildRequires:  fdupes
BuildRequires:  lapack-devel
BuildRequires:  mumps-devel
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.18
Requires:       python-scipy >= 1.3
Requires:       python-tinyarray
Recommends:     python-matplotlib
Recommends:     python-qsymm
Recommends:     python-sympy
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.3}
BuildRequires:  %{python_module sympy >= 1.5}
BuildRequires:  %{python_module tinyarray}
# /SECTION
# mumps exclusion list is "i586 s390 ppc armv7l" (sic!)
ExcludeArch:    %ix86 %arm

%python_subpackages

%description
Kwant is a Python library for numerical calculations on tight-binding
models with a strong focus on quantum transport. Kwant can be used to
simulate a variety of systems and phenomena in quantum physics
including: metals, graphene, topological insulators, quantum Hall
effect, superconductivity, spintronics, molecular electronics, any
combination of the above, and many other things. Kwant can calculate
transport properties (conductance, noise, scattering matrix),
dispersion relations, modes, wave functions, various Green’s
functions, out-of-equilibrium local quantities.

%prep
%setup -q -n kwant-%{version}

%build
# This prints the URL, but it also Cythonizes
python3 setup.py --cython --url
# CAN'T FIND mumps HEADERS
export CFLAGS="%{optflags} -I%{_includedir}/mumps"
%pyproject_wheel

%install
%pyproject_install

# REMOVE UNNEEDED HEADER FILE
%python_expand rm %{buildroot}%{$python_sitearch}/%{modname}/graph/defs.h

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# TESTS CANNOT BE RUN FROM TOPLEVEL SOURCE DIR
mkdir testing && pushd testing
export PYTHONPATH+=%{buildroot}%{python3_sitearch}
export PYTHONDONTWRITEBYTECODE=1
python3 -c 'import kwant; kwant.test()'
popd

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE.rst
%{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}-%{version}.dist-info

%changelog
