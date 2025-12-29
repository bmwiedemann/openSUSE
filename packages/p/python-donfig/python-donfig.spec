#
# spec file for package python-donfig
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-donfig
Version:        0.8.1.post1
Release:        0
Summary:        Python package for configuring a python package
License:        MIT AND BSD-3-Clause
URL:            https://github.com/pytroll/donfig
Source:         https://files.pythonhosted.org/packages/source/d/donfig/donfig-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 62.6}
BuildRequires:  %{python_module versioneer}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Donfig is a python library meant to make configuration easier for other
python packages. Donfig can be configured programmatically, by
environment variables, or from YAML files in standard locations.

%prep
%autosetup -p1 -n donfig-%{version}
sed -si '1 {\@^#!/usr/bin/env python@ d}' donfig/*.py donfig/tests/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.md README.rst
%license LICENSE.txt DASK_LICENSE.txt
%{python_sitelib}/donfig
%{python_sitelib}/donfig-%{version}.dist-info

%changelog
