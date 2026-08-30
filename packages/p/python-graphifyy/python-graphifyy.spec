#
# spec file for package python-graphifyy
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-graphifyy
Version:        0.9.52
Release:        0
Summary:        Code knowledge graph builder and query CLI for AI assistants
License:        Apache-2.0 AND MIT
URL:            https://github.com/Graphify-Labs/graphify
# PyPI sdist omits tests/fixtures and ARCHITECTURE.md, which %%check needs.
# Use the GitHub tag archive (same revision as the PyPI release).
Source:         https://github.com/Graphify-Labs/graphify/archive/refs/tags/v%{version}.tar.gz#/graphify-%{version}.tar.gz
# Optional at runtime: nested YAML frontmatter uses PyYAML when present.
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module mcp >= 1}
BuildRequires:  %{python_module networkx >= 3.4}
BuildRequires:  %{python_module numpy >= 1.21}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rapidfuzz >= 3.0}
BuildRequires:  %{python_module setuptools >= 77}
# HTTP MCP tests import starlette; extra floor is 1.3.1 (CVE-2026-48818 /
# CVE-2026-54283)
BuildRequires:  %{python_module starlette >= 1.3.1}
BuildRequires:  %{python_module tree-sitter >= 0.23}
BuildRequires:  %{python_module tree-sitter-bash}
BuildRequires:  %{python_module tree-sitter-c-sharp}
BuildRequires:  %{python_module tree-sitter-cpp}
BuildRequires:  %{python_module tree-sitter-c}
BuildRequires:  %{python_module tree-sitter-elixir}
BuildRequires:  %{python_module tree-sitter-fortran}
BuildRequires:  %{python_module tree-sitter-go}
BuildRequires:  %{python_module tree-sitter-groovy}
BuildRequires:  %{python_module tree-sitter-javascript}
BuildRequires:  %{python_module tree-sitter-java}
BuildRequires:  %{python_module tree-sitter-json}
BuildRequires:  %{python_module tree-sitter-julia}
BuildRequires:  %{python_module tree-sitter-kotlin}
BuildRequires:  %{python_module tree-sitter-lua}
BuildRequires:  %{python_module tree-sitter-objc}
BuildRequires:  %{python_module tree-sitter-php}
BuildRequires:  %{python_module tree-sitter-powershell}
BuildRequires:  %{python_module tree-sitter-python}
BuildRequires:  %{python_module tree-sitter-ruby}
BuildRequires:  %{python_module tree-sitter-rust}
BuildRequires:  %{python_module tree-sitter-scala}
BuildRequires:  %{python_module tree-sitter-swift}
BuildRequires:  %{python_module tree-sitter-typescript}
BuildRequires:  %{python_module tree-sitter-verilog}
BuildRequires:  %{python_module tree-sitter-zig}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
# git CLI for hook/install tests. spec-cleaner --perl rewrites this into
# perl(Git::*) providers; keep the package name (accepted deviation).
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
# python-tree-sitter-* bindings ctypes-load the C grammar .so from
# %%{_libdir}/tree-sitter/. Only tree-sitter-python's python subpackage
# Requires the C library; the rest omit it, so the python module BR does
# not pull the .so and %%check fails with "cannot open shared object file".
BuildRequires:  tree-sitter-bash
BuildRequires:  tree-sitter-c
BuildRequires:  tree-sitter-c-sharp
BuildRequires:  tree-sitter-cpp
BuildRequires:  tree-sitter-elixir
BuildRequires:  tree-sitter-fortran
BuildRequires:  tree-sitter-go
BuildRequires:  tree-sitter-groovy
BuildRequires:  tree-sitter-java
BuildRequires:  tree-sitter-javascript
BuildRequires:  tree-sitter-json
BuildRequires:  tree-sitter-julia
BuildRequires:  tree-sitter-kotlin
BuildRequires:  tree-sitter-lua
BuildRequires:  tree-sitter-objc
BuildRequires:  tree-sitter-php
BuildRequires:  tree-sitter-powershell
BuildRequires:  tree-sitter-python
BuildRequires:  tree-sitter-ruby
BuildRequires:  tree-sitter-rust
BuildRequires:  tree-sitter-scala
BuildRequires:  tree-sitter-swift
BuildRequires:  tree-sitter-typescript
BuildRequires:  tree-sitter-verilog
BuildRequires:  tree-sitter-zig
Requires:       alts
Requires:       python-networkx >= 3.4
Requires:       python-numpy >= 1.21
Requires:       python-rapidfuzz >= 3.0
Recommends:     %{python_flavor}-tree-sitter >= 0.23
Recommends:     %{python_flavor}-tree-sitter-bash
Recommends:     %{python_flavor}-tree-sitter-c
Recommends:     %{python_flavor}-tree-sitter-c-sharp
Recommends:     %{python_flavor}-tree-sitter-cpp
Recommends:     %{python_flavor}-tree-sitter-elixir
Recommends:     %{python_flavor}-tree-sitter-fortran
Recommends:     %{python_flavor}-tree-sitter-go
Recommends:     %{python_flavor}-tree-sitter-groovy
Recommends:     %{python_flavor}-tree-sitter-java
Recommends:     %{python_flavor}-tree-sitter-javascript
Recommends:     %{python_flavor}-tree-sitter-json
Recommends:     %{python_flavor}-tree-sitter-julia
Recommends:     %{python_flavor}-tree-sitter-kotlin
Recommends:     %{python_flavor}-tree-sitter-lua
Recommends:     %{python_flavor}-tree-sitter-objc
Recommends:     %{python_flavor}-tree-sitter-php
Recommends:     %{python_flavor}-tree-sitter-powershell
Recommends:     %{python_flavor}-tree-sitter-python
Recommends:     %{python_flavor}-tree-sitter-ruby
Recommends:     %{python_flavor}-tree-sitter-rust
Recommends:     %{python_flavor}-tree-sitter-scala
Recommends:     %{python_flavor}-tree-sitter-swift
Recommends:     %{python_flavor}-tree-sitter-typescript
Recommends:     %{python_flavor}-tree-sitter-verilog
Recommends:     %{python_flavor}-tree-sitter-zig
# Matching C grammar libraries (see BuildRequires comment above).
Recommends:     tree-sitter-bash
Recommends:     tree-sitter-c
Recommends:     tree-sitter-c-sharp
Recommends:     tree-sitter-cpp
Recommends:     tree-sitter-elixir
Recommends:     tree-sitter-fortran
Recommends:     tree-sitter-go
Recommends:     tree-sitter-groovy
Recommends:     tree-sitter-java
Recommends:     tree-sitter-javascript
Recommends:     tree-sitter-json
Recommends:     tree-sitter-julia
Recommends:     tree-sitter-kotlin
Recommends:     tree-sitter-lua
Recommends:     tree-sitter-objc
Recommends:     tree-sitter-php
Recommends:     tree-sitter-powershell
Recommends:     tree-sitter-python
Recommends:     tree-sitter-ruby
Recommends:     tree-sitter-rust
Recommends:     tree-sitter-scala
Recommends:     tree-sitter-swift
Recommends:     tree-sitter-typescript
Recommends:     tree-sitter-verilog
Recommends:     tree-sitter-zig
BuildArch:      noarch
# The primary flavor provides the plain PyPI/app name. Do NOT use the
# %%python3_only macro here: it expands to a test for a flavor literally named
# python3, which is false for every real flavor (python313, python314), so its
# body is silently dropped and the Provides never appears.
%if "%{python_flavor}" == "%{primary_python}"
Provides:       graphifyy = %{version}
%endif
%python_subpackages

%description
Graphify turns a codebase into a queryable knowledge graph
(graphify-out/graph.json) and registers a /graphify skill with AI coding
assistants. The graphify CLI answers plain-English questions about the
graph with file:line citations, traces paths between components, explains
symbols and summarizes pull-request impact. Individual language support is
provided by the python-tree-sitter-<language> grammar modules; a missing
grammar only disables that language.

%package mcp
Summary:        Model Context Protocol server for graphify
Requires:       %{python_flavor}-graphifyy = %{version}
Requires:       %{python_flavor}-mcp >= 1
Requires:       %{python_flavor}-starlette >= 1.3.1
Requires:       alts
# the primary flavor provides the plain PyPI/app name (see the main package)
%if "%{python_flavor}" == "%{primary_python}"
Provides:       graphifyy-mcp = %{version}
%endif

%description mcp
The graphify-mcp entry point, exposing the graphify knowledge graph
to AI assistants over the Model Context Protocol.

%prep
%autosetup -n graphify-%{version}
# a library module, never installed as a script: drop its stray shebang
sed -i '1{/^#!/d}' graphify/callflow_html.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/graphify
%python_clone -a %{buildroot}%{_bindir}/graphify-mcp
%python_group_libalternatives graphify
%python_group_libalternatives graphify-mcp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# api/network-dependent tests are deselected: they exercise hosted LLM
# endpoints with credentials the build environment does not have
# test_skillgen.py imports tools/ and extra skillgen machinery not needed
# for the installed package
# the additionally ignored files need network access (DNS) or an
# unsandboxed HOME; both are unavailable in the build environment
# test_label_communities_batches_when_over_batch_size asserts batch
# completion order [100, 100, 50], but label_communities runs batches
# concurrently (max_concurrency=4), so the observed order is racy
# test_built_wheel_ships_the_full_skill_payload runs python -m build;
# OBS python3.14 has a conflicting build package without __main__
# PYTEST_ADDOPTS --basetemp avoids pytest-of-abuild: two query CLI
# tests assert "build" not in the output, which matches the OBS user
export PYTEST_ADDOPTS="--basetemp=%{_tmppath}/gfytmp"
%pytest --ignore tests/test_skillgen.py --ignore tests/test_hooks.py --ignore tests/test_terraform.py --ignore tests/test_security.py --ignore tests/test_home_sandbox.py --ignore tests/test_watch.py --ignore tests/test_manifest_ingest.py --ignore tests/test_llm_backends.py --ignore tests/test_install_strings.py --ignore tests/test_detect.py -k "not (anthropic or openai or gemini or bedrock or ollama or test_label_communities_batches_when_over_batch_size or test_built_wheel_ships_the_full_skill_payload)"

%pre
%python_libalternatives_reset_alternative graphify

%pre mcp
%python_libalternatives_reset_alternative graphify-mcp

%files %{python_files}
%license LICENSE LICENSE-MIT NOTICE
%doc README.md
%python_alternative %{_bindir}/graphify
%{python_sitelib}/graphify
%{python_sitelib}/graphifyy-%{version}.dist-info

%files %{python_files mcp}
%python_alternative %{_bindir}/graphify-mcp

%changelog
