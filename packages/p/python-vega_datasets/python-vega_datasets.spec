#
# spec file for package python-vega_datasets
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
Name:           python-vega_datasets
Version:        0.9.0
Release:        0
Summary:        A Python package for offline access to Vega datasets
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/altair-viz/vega_datasets
Source:         https://files.pythonhosted.org/packages/source/v/vega_datasets/vega_datasets-%{version}.tar.gz
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
Requires:       python-pandas
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python package for offline access to vega datasets.
- Provide straightforward access in Python to the datasets made available
- return the results in the form of a Pandas dataframe
- wherever dataset size and/or license constraints make it possible, bundle the dataset with the package so that datasets can be loaded in the absence of a web connection

%prep
%setup -q -n vega_datasets-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest vega_datasets/tests

%files %{python_files}
%license LICENSE
%{python_sitelib}/vega_datasets
%{python_sitelib}/vega_datasets-%{version}*-info

%changelog
