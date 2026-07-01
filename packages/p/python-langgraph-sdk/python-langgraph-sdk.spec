#
# spec file for package python-langgraph-sdk
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


%{?sle15_python_module_pythons}
Name:           python-langgraph-sdk
Version:        0.4.2
Release:        0
Summary:        SDK for interacting with the LangGraph API
License:        MIT
URL:            https://github.com/langchain-ai/langgraph/tree/main/libs/sdk-py
Source:         https://files.pythonhosted.org/packages/source/l/langgraph_sdk/langgraph_sdk-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpx >= 0.25.2
Requires:       python-langchain-core >= 1.4.0
Requires:       python-langchain-protocol >= 0.0.15
Requires:       python-orjson >= 3.11.5
Requires:       python-websockets >= 14
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module httpx >= 0.25.2}
BuildRequires:  %{python_module langchain-core >= 1.4.0}
BuildRequires:  %{python_module langchain-protocol >= 0.0.15}
BuildRequires:  %{python_module orjson >= 3.11.5}
BuildRequires:  %{python_module pydantic >= 2}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module websockets >= 14}
# /SECTION
%python_subpackages

%description
The LangGraph SDK provides synchronous and asynchronous Python clients for
interacting with the LangGraph API, exposing helpers for assistants, threads,
runs, crons and the persistent store.

%prep
%autosetup -p1 -n langgraph_sdk-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Offline unit tests only (they mock httpx transports; no network access).
# The integration/ suite needs a live langgraph-api stack (and imports the
# langgraph package); it is excluded upstream via the "integration" marker but
# still imported at collection time, so skip the directory outright.
%pytest tests --ignore=tests/integration
# Recompile the installed modules as hash-based bytecode to avoid
# python-bytecode-inconsistent-mtime from the reproducibility-clamped .py mtimes.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langgraph_sdk
%python_expand %fdupes %{buildroot}%{$python_sitelib}/langgraph_sdk

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/langgraph_sdk
%{python_sitelib}/langgraph_sdk-%{version}.dist-info

%changelog
