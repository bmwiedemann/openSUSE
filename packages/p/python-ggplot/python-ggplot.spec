#
# spec file for package python-ggplot
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test
Name:           python-ggplot
Version:        0.11.5
Release:        0
# Tag for current release, used for the license
%define lictag  01a75b19aef2b573eed931a8285da00a3df169d1
Summary:        Python clone of R's ggplot
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/yhat/ggplot/
Source:         https://files.pythonhosted.org/packages/source/g/ggplot/ggplot-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/yhat/ggpy/%{lictag}/LICENSE
BuildRequires:  %{python_module Cycler}
BuildRequires:  %{python_module brewer2mpl}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module patsy >= 0.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module statsmodels}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Cycler
Requires:       python-brewer2mpl
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-patsy >= 0.4
Requires:       python-scipy
Requires:       python-six
Requires:       python-statsmodels
BuildArch:      noarch
%python_subpackages

%description
The ggplot package is a Python implementation of the grammar of
graphics. It is not intended to be a feature-for-feature port of
ggplot2 for R. There will be feature overlap, but not
necessarily mimicry.

%prep
%setup -q -n ggplot-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
