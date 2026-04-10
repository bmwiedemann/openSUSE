#
# spec file for package python-okta
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2024-2026, Martin Hauke <mardnh@gmx.de>
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
Version:        3.4.0
Release:        0
Summary:        Python SDK for the Okta Management API
License:        Apache-2.0
URL:            https://github.com/okta/okta-sdk-python
Source:         https://github.com/okta/okta-sdk-python/archive/refs/tags/v%{version}.tar.gz#/okta-sdk-python-%{version}.tar.gz
Patch0:         fix-test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aenum}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module flatdict}
BuildRequires:  %{python_module jwcrypto}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pydash}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-recording}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest-twisted}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module xmltodict}
BuildRequires:  %{python_module yarl}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyJWT
Requires:       python-PyYAML
Requires:       python-aenum
Requires:       python-aiohttp
Requires:       python-blinker
Requires:       python-flatdict
Requires:       python-jwcrypto
Requires:       python-pycryptodomex
Requires:       python-pydantic
Requires:       python-pydash
Requires:       python-python-dateutil
Requires:       python-requests
Requires:       python-xmltodict
Requires:       python-yarl
BuildArch:      noarch
%python_subpackages

%description
Python SDK for the Okta Management API.

%prep
%autosetup -p1 -n okta-sdk-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip integration tests (require a network connection)
rm -r tests/integration
%pytest

%files %{python_files}
%license LICENSE.md
%doc CHANGELOG.md README.md
%{python_sitelib}/okta
%{python_sitelib}/okta-%{version}.dist-info

%changelog
