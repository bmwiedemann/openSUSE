#
# spec file for package python-thewalrus
#
# Copyright (c) 2020 SUSE LLC
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


%define packagename thewalrus
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-thewalrus
Version:        0.13.0
Release:        0
Summary:        An open-source software architecture for photonic quantum computing
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/XanaduAI/thewalrus
Source:         https://github.com/XanaduAI/thewalrus/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module dask-all}
BuildRequires:  %{python_module numba >= 0.43.1}
BuildRequires:  %{python_module numpy >= 1.13.3}
BuildRequires:  %{python_module numpy-devel >= 1.13.3}
BuildRequires:  %{python_module pytest >= 5.4.1}
BuildRequires:  %{python_module repoze.lru >= 0.7}
BuildRequires:  %{python_module scipy >= 1.2.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sympy >= 1.5.1}
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-dask-all
Requires:       python-numba
Requires:       python-numpy >= 1.13.3
Requires:       python-repoze.lru >= 0.7
Requires:       python-scipy >= 1.2.1
Requires:       python-sympy >= 1.5.1
# Test failed for i586, no clue why.
ExcludeArch:    i586
%python_subpackages

%description
A library for the calculation of hafnians, Hermite polynomials and Gaussian boson sampling.

%prep
%setup -q -n %{packagename}-%{version}

%build
# We need to add -fopenmp manually, because otherwise
# setup.py build breaks CFLAGS gh#XanaduAI/thewalrus#198
export CFLAGS="%{optflags} -fopenmp"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*egg-info
%{python_sitearch}/%{packagename}

%changelog
