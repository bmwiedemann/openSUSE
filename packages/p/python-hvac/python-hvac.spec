#
# spec file for package python-hvac
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


Name:           python-hvac
Version:        2.3.0
Release:        0
Summary:        HashiCorp Vault API client
License:        BSD-3-Clause
URL:            https://github.com/hvac/hvac
Source:         https://github.com/hvac/hvac/releases/download/v%{version}/hvac-%{version}.tar.gz
BuildRequires:  %{python_module Authlib}
BuildRequires:  %{python_module Flask-SQLAlchemy}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module jwcrypto}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pyhcl >= 0.3.10}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.21.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyhcl >= 0.3.10
Requires:       python-requests >= 2.21.0
BuildArch:      noarch
%python_subpackages

%description
HashiCorp Vault API client for Python 2/3

%prep
%autosetup -p1 -n hvac-%{version}
# doctests and ldap need set up ldap server and that is quite an effort
rm -r tests/doctest/
rm tests/integration_tests/api/auth_methods/test_ldap.py
find hvac -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.* docs/changelog.rst
%license LICENSE.txt
%{python_sitelib}/hvac
%{python_sitelib}/hvac-%{version}.dist-info

%changelog
