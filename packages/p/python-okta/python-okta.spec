#
# spec file for package python-okta
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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


%{?sle15_python_module_pythons}
Name:           python-okta
Version:        2.9.10
Release:        0
Summary:        Python SDK for the Okta Management API
License:        Apache-2.0
URL:            https://github.com/okta/okta-sdk-python
Source:         https://files.pythonhosted.org/packages/source/o/okta/okta-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aenum}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module flatdict}
BuildRequires:  %{python_module jwcrypto}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pydash}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-recording}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xmltodict}
BuildRequires:  %{python_module yarl}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyJWT
Requires:       python-PyYAML
Requires:       python-aenum
Requires:       python-aiohttp
Requires:       python-flatdict
Requires:       python-jwcrypto
Requires:       python-pycryptodomex
Requires:       python-pydash
Requires:       python-xmltodict
Requires:       python-yarl
BuildArch:      noarch
%python_subpackages

%description
Python SDK for the Okta Management API.

%prep
%autosetup -p1 -n okta-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip integration tests (require a network connection)
rm -r tests/integration
# skip tests with "fixture 'fs' not found"
rm tests/unit/test_client.py
rm tests/unit/test_http_client.py
rm tests/unit/test_models.py
rm tests/unit/test_oauth.py
%pytest

%files %{python_files}
%license LICENSE.md
%doc CHANGELOG.md README.md
%{python_sitelib}/okta
%{python_sitelib}/okta-%{version}.dist-info

%changelog
