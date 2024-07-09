#
# spec file for package python-seaborn
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


Name:           python-seaborn
Version:        0.13.2
Release:        0
Summary:        Statistical data visualization for python
License:        BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/mwaskom/seaborn
Source:         https://files.pythonhosted.org/packages/source/s/seaborn/seaborn-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#mwaskom/seaborn#3685
Patch0:         support-numpy-2.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module matplotlib >= 3.6.2}
BuildRequires:  %{python_module numpy-devel >= 1.20}
BuildRequires:  %{python_module pandas >= 1.2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildConflicts: python-buildservice-tweak
Requires:       python-matplotlib >= 3.6.2
Requires:       python-numpy >= 1.20
Requires:       python-pandas >= 1.2
Recommends:     python-fastcluster
Recommends:     python-scipy >= 1.7
Recommends:     python-statsmodels >= 0.12
# SECTION tests with extras
BuildRequires:  %{python_module fastcluster}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.7}
BuildRequires:  %{python_module statsmodels >= 0.12}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Seaborn is a library for making attractive and informative
statistical graphics in Python. It is built on top of
matplotlib and tightly integrated with the PyData stack,
including support for numpy and pandas data structures and
statistical routines from scipy and statsmodels.

Some of the features that seaborn offers are:
- Several built-in themes that improve on the default matplotlib
  aesthetics
- Tools for choosing color palettes to make beautiful plots that
  reveal patterns in your data
- Functions for visualizing univariate and bivariate distributions
  or for comparing them between subsets of data
- Tools that fit and visualize linear regression models for different
  kinds of independent and dependent variables
- Functions that visualize matrices of data and use clustering
  algorithms to discover structure in those matrices
- A function to plot statistical timeseries data with flexible
  estimation and representation of uncertainty around the estimate
- High-level abstractions for structuring grids of plots that let you
  easily build complex visualizations

%prep
%autosetup -p1 -n seaborn-%{version}
# remove shebang
sed -i '1{/env python/d}' seaborn/external/appdirs.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="testeverythingexcept"
# This fails in i586 because of int size
if [ $(getconf LONG_BIT) -eq 32 ]; then
  donttest="$donttest or test_index_alignment_between_series"
fi
%pytest -n auto -rfEs -k "not ($donttest)"

%files %{python_files}
%license LICENSE.md licences/*
%doc README.md
%{python_sitelib}/seaborn
%{python_sitelib}/seaborn-%{version}.dist-info

%changelog
