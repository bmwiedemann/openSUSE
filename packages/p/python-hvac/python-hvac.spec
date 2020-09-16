#
# spec file for package python-hvac
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
Name:           python-hvac
Version:        0.10.5
Release:        0
Summary:        HashiCorp Vault API client
License:        BSD-3-Clause
URL:            https://github.com/ianunruh/hvac
Source:         https://github.com/hvac/hvac/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Authlib}
BuildRequires:  %{python_module Flask-SQLAlchemy}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module jwcrypto}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pyhcl >= 0.3.10}
BuildRequires:  %{python_module requests >= 2.21.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.5.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyhcl >= 0.3.10
Requires:       python-requests >= 2.21.0
Requires:       python-six >= 1.5.0
BuildArch:      noarch
%python_subpackages

%description
HashiCorp Vault API client for Python 2/3

%prep
%setup -q -n hvac-%{version}
# doctests and ldap need set up ldap server and that is quite an effort
rm -r tests/doctest/
rm tests/integration_tests/api/auth_methods/test_ldap.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%doc README*
%license LICENSE.txt
%{python_sitelib}/*

%changelog
