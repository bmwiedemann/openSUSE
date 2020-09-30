#
# spec file for package python-opt-einsum
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-opt-einsum
Version:        3.3.0
Release:        0
Summary:        Optimizing numpys einsum function
License:        MIT
URL:            https://github.com/dgasmith/opt_einsum
Source:         https://files.pythonhosted.org/packages/source/o/opt_einsum/opt_einsum-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
Requires:       python-numpy >= 1.7
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Optimized einsum can significantly reduce the overall execution time of einsum-like expressions (e.g.,
`np.einsum`,`dask.array.einsum`,`pytorch.einsum`,`tensorflow.einsum`)
by optimizing the expression's contraction order and dispatching many
operations to canonical BLAS, cuBLAS, or other specialized routines. Optimized
einsum is agnostic to the backend and can handle NumPy, Dask, PyTorch,
Tensorflow, CuPy, Sparse, Theano, JAX, and Autograd arrays as well as potentially
any library which conforms to a standard API. See the
[**documentation**](http://optimized-einsum.readthedocs.io) for more
information.

%prep
%setup -q -n opt_einsum-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
