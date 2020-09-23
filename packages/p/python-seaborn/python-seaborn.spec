#
# spec file for package python-seaborn
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
%define         skip_python2 1
Name:           python-seaborn
Version:        0.11.0
Release:        0
Summary:        Statistical data visualization for python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mwaskom/seaborn
Source:         https://files.pythonhosted.org/packages/source/s/seaborn/seaborn-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module fastcluster}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module matplotlib >= 2.1.2}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module numpy-devel >= 1.13.3}
BuildRequires:  %{python_module pandas >= 0.22.0}
BuildRequires:  %{python_module patsy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module statsmodels}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildConflicts: python-buildservice-tweak
Requires:       python-matplotlib >= 2.1.2
Requires:       python-numpy >= 1.13.3
Requires:       python-pandas >= 0.22.0
Requires:       python-scipy >= 1.0.1
Requires:       python-six
Recommends:     python-Pillow
Recommends:     python-fastcluster
Recommends:     python-patsy
Recommends:     python-statsmodels
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest seaborn

%files %{python_files}
%license LICENSE
%doc README.md
%doc licences/
%{python_sitelib}/seaborn*

%changelog
