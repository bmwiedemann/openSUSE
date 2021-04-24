#
# spec file for package python-scikit-sparse
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-scikit-sparse
Version:        0.4.5
Release:        0
# For license file
%define tag     c94f8418b6c36c3ff9db4f87e00fc08bd51cfb4b
Summary:        Scikits sparse matrix package
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/scikit-sparse/scikit-sparse/
Source:         https://files.pythonhosted.org/packages/source/s/scikit-sparse/scikit-sparse-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.13.3}
BuildRequires:  %{python_module scipy >= 0.19}
BuildRequires:  %{python_module setuptools >= 18.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  suitesparse-devel
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-numpy >= 1.12
Requires:       python-scipy >= 0.18
ExcludeArch:    %{ix86}

%python_subpackages

%description
Sparse matrix tools.

This is a sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper.

There is a wrapper for the CHOLMOD library for sparse Cholesky
decomposition.

%prep
%setup -q -n scikit-sparse-%{version}
# no need for nose here -- gh#scikit-sparse/pull#66
sed -i 's/from nose.tools import assert_raises/from pytest import raises as assert_raises/' sksparse/test_cholmod.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -ra --pyargs sksparse

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/sksparse
%{python_sitearch}/scikit_sparse-%{version}*-info

%changelog
