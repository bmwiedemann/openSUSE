#
# spec file for package python-cma
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020 Christoph Junghans
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


Name:           python-cma
Version:        4.0.0
Release:        0
Summary:        Covariance Matrix Adaptation Evolution Strategy numerical optimizer
License:        BSD-3-Clause
URL:            https://github.com/CMA-ES/pycma
Source0:        https://github.com/CMA-ES/pycma/archive/r%{version}.tar.gz#/cma-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Recommends:     python-matplotlib
BuildArch:      noarch
%python_subpackages

%description
A stochastic numerical optimization algorithm for difficult
(non-convex, ill-conditioned, multi-modal, rugged, noisy) optimization
problems in continuous search spaces, implemented in Python.

%prep
%autosetup -n pycma-r%{version}
#Remove unneeded shebang
sed -i '1d' cma/{bbobbenchmarks.py,purecma.py,test.py}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m cma.test

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/cma
%{python_sitelib}/cma-%{version}.dist-info

%changelog
