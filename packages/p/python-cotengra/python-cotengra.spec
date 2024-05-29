#
# spec file for package python-cotengra
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


Name:           python-cotengra
Version:        0.6.2
Release:        0
Summary:        Hyper optimized contraction trees for large tensor networks and einsums
License:        Apache-2.0
URL:            https://github.com/jcmgray/cotengra
Source:         https://files.pythonhosted.org/packages/source/c/cotengra/cotengra-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-autoray
Recommends:     python-cotengrust
Recommends:     python-cytoolz
Recommends:     python-kahypar
Recommends:     python-networkx
Recommends:     python-numpy
Recommends:     python-opt-einsum
Recommends:     python-optuna
Recommends:     python-ray
# SECTION test requirements
BuildRequires:  %{python_module altair}
BuildRequires:  %{python_module autoray}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opt-einsum}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module seaborn}
BuildRequires:  %{python_module tqdm}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A python library for contracting tensor networks or einsum expressions involving large numbers of tensors.
Some of the key feautures of cotengra include:
 * drop-in einsum replacement
 * an explicit contraction tree object that can be flexibly built, modified and visualized
 * a 'hyper optimizer' that samples trees while tuning the generating meta-paremeters
 * dynamic slicing for massive memory savings and parallelism
 * support for hyper edge tensor networks and thus arbitrary einsum equations
 * paths that can be supplied to numpy.einsum, opt_einsum, quimb among others
 * performing contractions with tensors from many libraries via cotengra, even if they don't provide einsum
   or tensordot but do have (batch) matrix multiplication

%prep
%autosetup -p1 -n cotengra-%{version}
sed -i '/addopts/d' pyproject.toml
rm cotengra/.gitattributes
# Note: ignore the rust files for now gh#jcmgray/cotengra#30

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -n auto

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/cotengra
%{python_sitelib}/cotengra-%{version}.dist-info

%changelog
