#
# spec file for package python-agent-client-protocol
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


Name:           python-agent-client-protocol
Version:        0.7.0
Release:        0
Summary:        A Python implement of Agent Client Protocol (ACP, by Zed Industries)
License:        Apache-2.0
URL:            https://agentclientprotocol.github.io/python-sdk/
Source:         https://files.pythonhosted.org/packages/source/a/agent-client-protocol/agent_client_protocol-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module datamodel-code-generator}
BuildRequires:  %{python_module mkdocs}
BuildRequires:  %{python_module mkdocs-material}
#    deptry>=0.23.0
#    ty>=0.0.1a16
#    mkdocstrings
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  %{python_module pydantic >= 2.7}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pydantic >= 2.7
Suggests:       python-logfire >= 0.14
Suggests:       python-opentelemetry-sdk >= 1.28.0
BuildArch:      noarch
%python_subpackages

%description
Agent Client Protocol

Build ACP-compliant agents and clients in Python with generated schema
models, asyncio transports, helper builders, and runnable demos.

%prep
%autosetup -p1 -n agent_client_protocol-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_ADDOPTS="--import-mode=importlib"
# rpc tests are stalling endlessly
%pytest -k 'not test_rpc'

%files %{python_files}
%{python_sitelib}/acp
%{python_sitelib}/agent_client_protocol-%{version}*-info

%changelog
