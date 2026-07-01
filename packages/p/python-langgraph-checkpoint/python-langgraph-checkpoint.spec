#
# spec file for package python-langgraph-checkpoint
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-langgraph-checkpoint
Version:        4.1.1
Release:        0
Summary:        Library with base interfaces for LangGraph checkpoint savers
License:        MIT
URL:            https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint
Source:         https://files.pythonhosted.org/packages/source/l/langgraph_checkpoint/langgraph_checkpoint-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-langchain-core >= 0.2.38
Requires:       python-ormsgpack >= 1.12.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dataclasses-json}
BuildRequires:  %{python_module langchain-core >= 0.2.38}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module ormsgpack >= 1.12.0}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
LangGraph Checkpoint provides the base interfaces and reference
implementations for checkpoint savers (checkpointers) used by LangGraph.

Checkpointers persist the state of a graph at every super-step, enabling
features such as human-in-the-loop interaction, memory across runs, time
travel and fault tolerance. This package ships the in-memory reference
saver and the serialization machinery shared by the persistent backends.

%prep
%autosetup -p1 -n langgraph_checkpoint-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_redis_cache.py requires a running Redis server (offline build);
# test_conformance_delta.py self-skips when the conformance suite is absent.
%pytest tests --ignore tests/test_redis_cache.py
# Recompile as hash-based bytecode: this namespace package ships many modules
# whose timestamp-based .pyc desync from the reproducibility-clamped .py mtimes
# and trip python-bytecode-inconsistent-mtime.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langgraph
%python_expand %fdupes %{buildroot}%{$python_sitelib}/langgraph

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/langgraph
%{python_sitelib}/langgraph/cache
%{python_sitelib}/langgraph/checkpoint
%{python_sitelib}/langgraph/store
%{python_sitelib}/langgraph_checkpoint-%{version}.dist-info

%changelog
