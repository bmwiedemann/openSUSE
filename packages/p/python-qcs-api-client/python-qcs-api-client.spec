#
# spec file for package python-qcs-api-client
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-qcs-api-client
Version:        0.21.1
Release:        0
Summary:        Python client library for accessing the Rigetti QCS API
License:        MIT
URL:            https://github.com/rigetti/qcs-api-client-python
Source:         https://github.com/rigetti/qcs-api-client-python/archive/refs/tags/v%{version}.tar.gz#/qcs-api-client-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Use pyRFC3339 rather than rfc3339 which is not packaged
Patch0:         switch-to-pyrfc3339.patch
# PATCH-FIX-OPENSUSE Support newer respx
Patch1:         support-new-respx.patch
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pyRFC3339}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module respx}
BuildRequires:  %{python_module retrying}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT
Requires:       python-attrs >= 20.1
Requires:       python-dateutil >= 2.8.1
Requires:       python-httpx >= 0.15
Requires:       python-iso8601 >= 1.0.2
Requires:       python-pyRFC3339
Requires:       python-pydantic >= 1.7.2
Requires:       python-retrying >= 1.3
Requires:       python-toml
BuildArch:      noarch
%python_subpackages

%description
Allows access to the Rigetti Quantum Computing System API

%prep
%autosetup -p1 -n qcs-api-client-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --ignore tests/test_client/test_auth.py -k 'not test_sync_client'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/qcs_api_client-%{version}*.dist-info
%{python_sitelib}/qcs_api_client

%changelog
