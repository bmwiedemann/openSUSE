#
# spec file for package python-material-color-utilities-python
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-material-color-utilities-python
Version:        0.1.5
Release:        0
Summary:        Python port of material-color-utilities used for Material You colors
License:        Apache-2.0
URL:            https://github.com/avanishsubbiah/material-color-utilities-python
Source:         https://files.pythonhosted.org/packages/source/m/material-color-utilities-python/material-color-utilities-python-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Python port of material-color-utilities used for Material You colors.

%prep
%setup -qn material-color-utilities-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.md
%{python_sitelib}/material_color_utilities_python
%{python_sitelib}/material_color_utilities_python-%{version}.dist-info

%changelog
