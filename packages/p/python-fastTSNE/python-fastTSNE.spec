#
# spec file for package python-fastTSNE
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         skip_python2 1
Name:           python-fastTSNE
Version:        0.2.13
Release:        0
Summary:        Python implementations of t-SNE
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pavlin-policar/fastTSNE
Source0:        https://files.pythonhosted.org/packages/source/f/fastTSNE/fastTSNE-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/pavlin-policar/fastTSNE/master/LICENSE
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel > 1.14}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numba >= 0.38.1
Requires:       python-numpy > 1.14
Requires:       python-scikit-learn >= 0.20
Requires:       python-scipy
# SECTION test requirements
BuildRequires:  %{python_module fire}
BuildRequires:  %{python_module MulticoreTSNE}
BuildRequires:  %{python_module numba >= 0.38.1}
BuildRequires:  %{python_module scikit-learn >= 0.20}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
This package provides two implementations of t-SNE:

  * Barnes-hut t-SNE is inspired by Multicore t-SNE and is
    appropriate for small data sets and has asymptotic complexity
    O(n log n).
  * Fit-SNE is inspired by the C++ implementation of Fit-SNE and is
    appropriate for larger data sets (>10,000 samples). It has
    asymptotic complexity O(n).

Both implementations are included because Barnes-Hut t-SNE tends
to be slightly faster for smaller data sets, while Fit-SNE is much
faster for larger data sets (>10,000 samples).

%prep
%setup -q -n fastTSNE-%{version}
cp %{SOURCE10} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

# Don't package tests in generic directory
%python_expand rm -rf %{buildroot}%{$python_sitearch}/tests/

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/*

%changelog
