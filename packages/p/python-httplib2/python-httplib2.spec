#
# spec file for package python-httplib2
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


# Tests require network connection
%bcond_with tests
%{?sle15_python_module_pythons}
Name:           python-httplib2
Version:        0.31.0
Release:        0
Summary:        A Python HTTP client library
License:        Apache-2.0 AND MIT AND (GPL-2.0-or-later OR MPL-1.1 OR LGPL-2.1-or-later)
URL:            https://github.com/httplib2/httplib2
Source:         https://files.pythonhosted.org/packages/source/h/httplib2/httplib2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       ca-certificates
Requires:       python-certifi
Requires:       python-pyparsing >= 2.4.2
BuildArch:      noarch
%if %{with tests}
# Test requirements (for ssl module):
BuildRequires:  python
BuildRequires:  python3
%endif
%python_subpackages

%description
A comprehensive HTTP client library that supports many features
left out of other HTTP libraries.

%prep
%autosetup -p1 -n httplib2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests require network connection
# python3 python3/httplib2test.py

%files %{python_files}
%{python_sitelib}/httplib2-%{version}*-info
%{python_sitelib}/httplib2

%changelog
