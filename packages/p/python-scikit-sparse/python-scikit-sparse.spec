#
# spec file for package python-scikit-sparse
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# For license file
%define tag     c94f8418b6c36c3ff9db4f87e00fc08bd51cfb4b
Name:           python-scikit-sparse
Version:        0.4.16
Release:        0
Summary:        Scikits sparse matrix package
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/scikit-sparse/scikit-sparse/
Source:         https://files.pythonhosted.org/packages/source/s/scikit-sparse/scikit_sparse-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.23.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy >= 0.19}
BuildRequires:  %{python_module setuptools >= 18.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  suitesparse-devel
Requires:       python-numpy >= 1.23.3
Requires:       python-scipy >= 0.18
ExcludeArch:    %{ix86}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Sparse matrix tools.

This is a sparse matrix code in Python that plays well with
scipy.sparse, but that is somehow unsuitable for inclusion in scipy
proper.

There is a wrapper for the CHOLMOD library for sparse Cholesky
decomposition.

%prep
%autosetup -p1 -n scikit_sparse-%{version}
# Move the test data to tests
mv sksparse/test_data tests

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -ra --pyargs tests

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/sksparse
%{python_sitearch}/scikit_sparse-%{version}.dist-info

%changelog
