#
# spec file for package python-mcp
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-mcp%{psuffix}
Version:        1.27.0
Release:        0
Summary:        Python implementation of the Model Context Protocol
License:        MIT
Group:          Development/Languages/Python
# GitHub repo https://github.com/modelcontextprotocol/python-sdk
URL:            https://modelcontextprotocol.io/introduction
Source:         https://files.pythonhosted.org/packages/source/m/mcp/mcp-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 4.5
Requires:       python-httpx >= 0.27
Requires:       python-httpx-sse >= 0.4
# From PyJWT[crypto]
Requires:       python-cryptography >= 3.4.0
Requires:       python-jsonschema >= 4.20.0
Requires:       python-pydantic >= 2.7.2
Requires:       python-pydantic-settings >= 2.5.2
Requires:       python-python-multipart >= 0.0.9
Requires:       python-sse-starlette >= 1.6.1
Requires:       python-starlette >= 0.27
Requires:       python-uvicorn >= 0.23.1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module inline-snapshot}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module mcp = %{version}}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-examples}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.32.3}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module typer}
BuildRequires:  %{python_module uv >= 0.7.2}
BuildRequires:  %{python_module websockets}
%endif
%python_subpackages

%description
Model Context Protocol (or Master Control Program?) implementation
for python.

%package devel
Summary:        Executables for %{name}
BuildRequires:  alts
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends: python-uv
Recommends: npm
Conflicts:      mmv

%description devel
This package contains the executables for %{name}.

%prep
%autosetup -p1 -n mcp-%{version}

%build
%if %{without test}
# This is an ugly hack, should not be necessary, but is to build on SLE 15 with Python 3.11
# MgE, 2025-06-19
%if 0%{?suse_version} < 1600
sed -i -e "s/3.12/3.11/g" pyproject.toml
sed -i -e "s/3.13/3.11/g" pyproject.toml
%endif

%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%fdupes %{buildroot}%{python_sitelib}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/mcp
%endif

%check
%if %{with test}
sed -i 's/"python"/"python3"/' tests/client/test_stdio.py
# test_command_execution needs full package including docs
donttest="test_command_execution"
# https://github.com/modelcontextprotocol/python-sdk/commit/17f9c00c53b4463ac1a449d601c2d181664ab857 dropped test_build_metadata[with-path-param]
donttest+=" or test_build_metadata[with-path-param]"
# test_client_session_version_negotiation_failure failure probably related to https://github.com/modelcontextprotocol/python-sdk/issues/1018
donttest+=" or test_client_session_version_negotiation_failure"
# flaky tests on aarch64
donttest+=" or test_streamablehttp_client_get_stream or test_streamablehttp_client_resumption"
%pytest -k "not ($donttest or OAuth)"
# problems with unawaited coroutines
%pytest -k "OAuth" --asyncio-mode=auto
%endif

%post devel
%python_expand %python_install_alternative mcp

%postun devel
%python_expand %python_uninstall_alternative mcp

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/mcp
%{python_sitelib}/mcp-%{version}*-info

%files %{python_files devel}
%license LICENSE
%python_alternative %{_bindir}/mcp
%endif

%changelog
