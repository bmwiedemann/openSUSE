#
# spec file for package python-langgraph-prebuilt
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


Name:           python-langgraph-prebuilt
Version:        1.1.0
Release:        0
Summary:        High-level APIs for creating and executing LangGraph agents and tools
License:        MIT
URL:            https://github.com/langchain-ai/langgraph/tree/main/libs/prebuilt
Source:         https://files.pythonhosted.org/packages/source/l/langgraph_prebuilt/langgraph_prebuilt-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-langchain-core >= 1.3.1
Requires:       python-langgraph-checkpoint >= 2.1.0
BuildArch:      noarch
%python_subpackages

%description
LangGraph Prebuilt provides high-level, ready-to-use building blocks for
constructing and running LangGraph agents and tools.

It ships the create_react_agent factory, the ToolNode executor for invoking
tools inside a graph, tool-call validation and streaming helpers, and the
InjectedState/InjectedStore annotations used to pass graph state into tools.

%prep
%autosetup -p1 -n langgraph_prebuilt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The test suite imports the top-level "langgraph" package, which depends on
# this package (circular dependency on the consumer), so it cannot run during
# this build; only byte-compilation is exercised.
# Recompile as hash-based bytecode: this namespace package ships modules whose
# timestamp-based .pyc desync from the reproducibility-clamped .py mtimes and
# trip python-bytecode-inconsistent-mtime.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langgraph
%python_expand %fdupes %{buildroot}%{$python_sitelib}/langgraph

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/langgraph
%{python_sitelib}/langgraph/prebuilt
%{python_sitelib}/langgraph_prebuilt-%{version}.dist-info

%changelog
