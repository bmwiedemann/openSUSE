#
# spec file for package python-dicttoxml
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


Name:           python-dicttoxml
Version:        1.7.16
Release:        0
Summary:        Python module for converting a dictionary to XML
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/quandyfactory/dicttoxml
Source:         https://files.pythonhosted.org/packages/source/d/dicttoxml/dicttoxml-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module converts a Python dictionary or other native data type
into a valid XML string.

%prep
%setup -q -n dicttoxml-%{version}
sed -i '1{\@^#!%{_bindir}/env python@d}' dicttoxml.py
mv LICENCE.txt LICENSE.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no testsuite found

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/dicttoxml.py
%{python_sitelib}/dicttoxml-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/dicttoxml*

%changelog
