#
# spec file for package python-langgraph
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


Name:           python-langgraph
Version:        1.2.8
Release:        0
Summary:        Library for building stateful, multi-actor applications with LLMs
License:        MIT
URL:            https://github.com/langchain-ai/langgraph
Source:         https://files.pythonhosted.org/packages/source/l/langgraph/langgraph-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-langchain-core >= 1.4.7
Requires:       python-langgraph-checkpoint < 5
Requires:       python-langgraph-checkpoint >= 4.1.0
Requires:       python-langgraph-prebuilt < 1.2
Requires:       python-langgraph-prebuilt >= 1.1.0
Requires:       python-langgraph-sdk < 0.5
Requires:       python-langgraph-sdk >= 0.4.2
Requires:       python-pydantic >= 2.7.4
Requires:       python-xxhash >= 3.5.0
BuildArch:      noarch
%python_subpackages

%description
LangGraph is a low-level orchestration framework for building, running and
managing stateful, multi-actor applications with large language models.

It models an application as a graph of nodes and edges with shared state,
adding durable execution with checkpointing, human-in-the-loop interaction,
streaming of tokens and intermediate steps, and time-travel debugging. This
package provides the core graph API (StateGraph), the Pregel runtime, the
functional API, channels and managed values shared across the LangGraph
ecosystem.

%prep
%autosetup -p1 -n langgraph-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The bundled test suite cannot run during the build: tests/conftest.py is
# loaded for the whole tree and unconditionally imports the PostgreSQL and
# SQLite checkpoint backends (langgraph-checkpoint-postgres /
# langgraph-checkpoint-sqlite, not packaged for Factory) plus psycopg and
# redis, so pytest collection fails before any offline unit test executes.
# Only byte-compilation is exercised here.
# Recompile as hash-based bytecode: this namespace package ships many modules
# whose timestamp-based .pyc desync from the reproducibility-clamped .py mtimes
# and trip python-bytecode-inconsistent-mtime.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langgraph
%python_expand %fdupes %{buildroot}%{$python_sitelib}/langgraph

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/langgraph
%{python_sitelib}/langgraph/*.py
%{python_sitelib}/langgraph/py.typed
%{python_sitelib}/langgraph/__pycache__
%{python_sitelib}/langgraph/_internal
%{python_sitelib}/langgraph/channels
%{python_sitelib}/langgraph/func
%{python_sitelib}/langgraph/graph
%{python_sitelib}/langgraph/managed
%{python_sitelib}/langgraph/pregel
%{python_sitelib}/langgraph/stream
%{python_sitelib}/langgraph/utils
%{python_sitelib}/langgraph-%{version}.dist-info

%changelog
