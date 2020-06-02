#
# spec file for package python-xmltodict
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
Name:           python-xmltodict
Version:        0.12.0
Release:        0
Summary:        Module to make XML working resemble JSON
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/martinblech/xmltodict
Source:         https://files.pythonhosted.org/packages/source/x/xmltodict/xmltodict-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-xml
BuildArch:      noarch
BuildRequires:  %{python_module pytest}
%python_subpackages

%description
xmltodict is a Python module that makes working with XML feel like you are
working with json, as in this:
http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html

%prep
%setup -q -n xmltodict-%{version}
sed -i '1{\@^#!%{_bindir}/env python@d}' xmltodict.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/xmltodict.py*
%pycache_only %{python_sitelib}/__pycache__/xmltodict.*.py*
%{python_sitelib}/xmltodict-%{version}-py*.egg-info

%changelog
