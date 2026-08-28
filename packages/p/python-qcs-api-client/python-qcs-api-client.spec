#
# spec file for package python-qcs-api-client
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-qcs-api-client
Version:        0.27.3
Release:        0
Summary:        Python client library for accessing the Rigetti QCS API
License:        MIT
URL:            https://github.com/rigetti/qcs-api-client-python
Source:         https://github.com/rigetti/qcs-api-client-python/archive/refs/tags/v%{version}.tar.gz#/qcs-api-client-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Use pyRFC3339 rather than rfc3339 which is not packaged
Patch1:         switch-to-pyrfc3339.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION runtime
BuildRequires:  %{python_module PyJWT >= 2.12.1}
BuildRequires:  %{python_module attrs >= 25.4}
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module pyRFC3339 >= 1.1}
BuildRequires:  %{python_module pydantic >= 2.10.6}
BuildRequires:  %{python_module pydantic-settings >= 2.8.1}
BuildRequires:  %{python_module python-dateutil >= 2.9.0}
BuildRequires:  %{python_module qcs-api-client-common >= 0.17.5}
BuildRequires:  %{python_module tenacity >= 9.1}
BuildRequires:  %{python_module toml >= 0.10.2}
# /SECTION
# SECTION test
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module respx >= 0.20}
# /SECTION
Requires:       python-PyJWT >= 2.12.1
Requires:       python-attrs >= 25.4
Requires:       python-httpx >= 0.28.1
Requires:       python-pyRFC3339 >= 1.1
Requires:       python-pydantic >= 2.10.6
Requires:       python-pydantic-settings >= 2.8.1
Requires:       python-python-dateutil >= 2.9.0
Requires:       python-qcs-api-client-common >= 0.17.5
Requires:       python-tenacity >= 9.1
Requires:       python-toml >= 0.10.2
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
%pytest -k "not test_datetime_conversion"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/qcs_api_client
%{python_sitelib}/qcs_api_client-%{version}.dist-info

%changelog
