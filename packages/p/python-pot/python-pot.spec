#
# spec file for package python-POT
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


Name:           python-pot
Version:        0.9.6.post1
Release:        0
Summary:        Python Optimal Transport Library
License:        MIT
URL:            https://github.com/PythonOT/POT
Source:         https://github.com/PythonOT/POT/archive/refs/tags/%{version}.tar.gz#/pot-%{version}.tar.gz
# PATCH-FIX-UPSTREAM A couple of commits from gh#PythonOT/POT#788
Patch0:         fix-scipy-version-compatibility.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Cython >= 0.23}
BuildRequires:  %{python_module numpy-devel >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  gcc-c++
BuildRequires:  fdupes
Requires:       python-numpy
Requires:       python-scipy
%python_subpackages

%description
POT: Python Optimal Transport, has the following main features:
* A large set of differentiable solvers for optimal transport problems, including:
  *  Exact linear OT, entropic and quadratic regularized OT,
  *  Gromov-Wasserstein (GW) distances, Fused GW distances and variants of
     quadratic OT,
  *  Unbalanced and partial OT for different divergences,
*  OT barycenters (Wasserstein and GW) for fixed and free support,
*  Fast OT solvers in 1D, on the circle and between Gaussian Mixture Models (GMMs),
*  Many ML related solvers, such as domain adaptation, optimal transport mapping
   estimation, subspace learning, Graph Neural Networks (GNNs) layers.
*  Several backends for easy use with Pytorch, Jax, Tensorflow, Numpy and Cupy arrays.

%prep
%autosetup -p1 -n POT-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv ot ot.do-not-use
# Requires in-place build, since it assumes ot.helpers in the current
# working directory
donttest="xxxxxxxxx"
if [ $(getconf LONG_BIT) -eq 32 ]; then
    # Fails on 32 bit arches due to long vs int64_t
    donttest="test_partial_wasserstein_1d"
fi
%pytest_arch --ignore test/test_helpers.py -k "not $donttest"
mv ot.do-not-use ot

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/ot
%{python_sitearch}/[Pp][Oo][Tt]-%{version}.dist-info

%changelog
