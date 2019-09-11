#
# spec file for package python-sklearn-pandas
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
Name:           python-sklearn-pandas
Version:        1.8.0
Release:        0
Summary:        Pandas integration with sklearn
License:        Zlib AND BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/paulgb/sklearn-pandas
Source:         https://files.pythonhosted.org/packages/source/s/sklearn-pandas/sklearn-pandas-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.6.1
Requires:       python-pandas >= 0.11.0
Requires:       python-scikit-learn >= 0.15.0
Requires:       python-scipy >= 0.14
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy >= 1.6.1}
BuildRequires:  %{python_module pandas >= 0.11.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-learn >= 0.15.0}
BuildRequires:  %{python_module scipy >= 0.14}
# /SECTION
%python_subpackages

%description
This module provides a bridge between Scikit-Learn's machine learning
methods and pandas-style Data Frames.

%prep
%setup -q -n sklearn-pandas-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/sklearn_pandas*

%changelog
