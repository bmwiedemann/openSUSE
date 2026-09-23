#
# spec file for package graphifyy
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

# Build the application against the distribution's primary Python flavour;
# this is a single-flavour application, not a multi-flavour module
# (successor of the python-graphifyy multibuild package).
%define pythons %{primary_python}
Name:           graphifyy
Version:        0.9.66
Release:        0
Summary:        Code knowledge graph builder and query CLI for AI assistants
License:        Apache-2.0 AND MIT
URL:            https://github.com/Graphify-Labs/graphify
# PyPI sdist omits tests/fixtures and ARCHITECTURE.md, which %%check needs.
# Use the GitHub tag archive (same revision as the PyPI release).
Source:         https://github.com/Graphify-Labs/graphify/archive/refs/tags/v%{version}.tar.gz#/graphify-%{version}.tar.gz
# Optional at runtime: nested YAML frontmatter uses PyYAML when present.
BuildRequires:  %{primary_python}-PyYAML
BuildRequires:  %{primary_python}-mcp >= 1
BuildRequires:  %{primary_python}-networkx >= 3.4
BuildRequires:  %{primary_python}-numpy >= 1.21
BuildRequires:  %{primary_python}-pip
BuildRequires:  %{primary_python}-pytest
BuildRequires:  %{primary_python}-rapidfuzz >= 3.0
# .robot/.resource extraction parses via robot.api (upstream [robot] extra);
# absent, those tests skip and only Robot Framework support is lost
BuildRequires:  %{primary_python}-robotframework >= 4.0
# Upstream build wants setuptools >= 83, not yet in the tree (has
# 80.9): keep the satisfiable floor, plain setuptools.build_meta
# needs nothing newer.
BuildRequires:  %{primary_python}-setuptools >= 77
# HTTP MCP tests import starlette; extra floor is 1.3.1 (CVE-2026-48818 /
# CVE-2026-54283)
BuildRequires:  %{primary_python}-starlette >= 1.3.1
BuildRequires:  %{primary_python}-tree-sitter >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-bash >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-c >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-c-sharp >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-cpp >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-elixir >= 0.3
BuildRequires:  %{primary_python}-tree-sitter-fortran >= 0.6
BuildRequires:  %{primary_python}-tree-sitter-go >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-groovy >= 0.1
BuildRequires:  %{primary_python}-tree-sitter-java >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-javascript >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-json >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-julia >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-kotlin >= 1.0
BuildRequires:  %{primary_python}-tree-sitter-lua >= 0.2
BuildRequires:  %{primary_python}-tree-sitter-objc >= 3.0
BuildRequires:  %{primary_python}-tree-sitter-php >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-powershell >= 0.26
BuildRequires:  %{primary_python}-tree-sitter-python >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-ruby >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-rust >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-scala >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-swift >= 0.7
BuildRequires:  %{primary_python}-tree-sitter-typescript >= 0.23
BuildRequires:  %{primary_python}-tree-sitter-verilog >= 1.0
BuildRequires:  %{primary_python}-tree-sitter-zig >= 1.0
BuildRequires:  %{primary_python}-wheel
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
Requires:       %{primary_python}-networkx >= 3.4
Requires:       %{primary_python}-numpy >= 1.21
Requires:       %{primary_python}-rapidfuzz >= 3.0
Recommends:     %{primary_python}-robotframework >= 4.0
Recommends:     %{primary_python}-tree-sitter >= 0.23
Recommends:     %{primary_python}-tree-sitter-bash >= 0.23
Recommends:     %{primary_python}-tree-sitter-c >= 0.23
Recommends:     %{primary_python}-tree-sitter-c-sharp >= 0.23
Recommends:     %{primary_python}-tree-sitter-cpp >= 0.23
Recommends:     %{primary_python}-tree-sitter-elixir >= 0.3
Recommends:     %{primary_python}-tree-sitter-fortran >= 0.6
Recommends:     %{primary_python}-tree-sitter-go >= 0.23
Recommends:     %{primary_python}-tree-sitter-groovy >= 0.1
Recommends:     %{primary_python}-tree-sitter-java >= 0.23
Recommends:     %{primary_python}-tree-sitter-javascript >= 0.23
Recommends:     %{primary_python}-tree-sitter-json >= 0.23
Recommends:     %{primary_python}-tree-sitter-julia >= 0.23
Recommends:     %{primary_python}-tree-sitter-kotlin >= 1.0
Recommends:     %{primary_python}-tree-sitter-lua >= 0.2
Recommends:     %{primary_python}-tree-sitter-objc >= 3.0
Recommends:     %{primary_python}-tree-sitter-php >= 0.23
Recommends:     %{primary_python}-tree-sitter-powershell >= 0.26
Recommends:     %{primary_python}-tree-sitter-python >= 0.23
Recommends:     %{primary_python}-tree-sitter-ruby >= 0.23
Recommends:     %{primary_python}-tree-sitter-rust >= 0.23
Recommends:     %{primary_python}-tree-sitter-scala >= 0.23
Recommends:     %{primary_python}-tree-sitter-swift >= 0.7
Recommends:     %{primary_python}-tree-sitter-typescript >= 0.23
Recommends:     %{primary_python}-tree-sitter-verilog >= 1.0
Recommends:     %{primary_python}-tree-sitter-zig >= 1.0
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
# Transitional aid from the python-graphifyy multibuild package: take over
# every flavored binary name it shipped.
Provides:       python-graphifyy = %{version}
Obsoletes:      python-graphifyy < %{version}
Provides:       python313-graphifyy = %{version}-%{release}
Obsoletes:      python313-graphifyy < %{version}
Provides:       python314-graphifyy = %{version}-%{release}
Obsoletes:      python314-graphifyy < %{version}
Provides:       python313-graphifyy-mcp = %{version}-%{release}
Obsoletes:      python313-graphifyy-mcp < %{version}
Provides:       python314-graphifyy-mcp = %{version}-%{release}
Obsoletes:      python314-graphifyy-mcp < %{version}
BuildArch:      noarch

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
Requires:       graphifyy = %{version}
Requires:       %{primary_python}-mcp >= 1
Requires:       %{primary_python}-starlette >= 1.3.1

%description mcp
The graphify-mcp entry point, exposing the graphify knowledge graph
to AI assistants over the Model Context Protocol.

%prep
%autosetup -n graphify-%{version} -p1
# a library module, never installed as a script: drop its stray shebang
sed -i '1{/^#!/d}' graphify/callflow_html.py

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
python%{python_version} -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{python_sitelib}/graphify
%fdupes %{buildroot}%{python_sitelib}

%check
# api/network-dependent tests are deselected: they exercise hosted LLM
# endpoints with credentials the build environment does not have
# test_skillgen.py imports tools/ and extra skillgen machinery not needed
# for the installed package
# the additionally ignored files need network access (DNS) or an
# unsandboxed HOME; both are unavailable in the build environment
# test_terraform.py / test_terraform_modules.py need python-tree-sitter-hcl
# (optional [terraform] extra), not in Factory
# test_{erlang,r,solidity,vbnet}_extractor.py need the matching grammar
# modules (upstream r/erlang/solidity/vbnet extras); R and Erlang have
# no standalone PyPI wheel at all, none are in Factory
# test_label_communities_batches_when_over_batch_size asserts batch
# completion order [100, 100, 50], but label_communities runs batches
# concurrently (max_concurrency=4), so the observed order is racy
# test_built_wheel_ships_the_full_skill_payload runs python -m build;
# OBS python3.14 has a conflicting build package without __main__
# PYTEST_ADDOPTS --basetemp avoids pytest-of-abuild: two query CLI
# tests assert "build" not in the output, which matches the OBS user
export PYTEST_ADDOPTS="--basetemp=%{_tmppath}/gfytmp"
%pytest --ignore tests/test_skillgen.py --ignore tests/test_hooks.py --ignore tests/test_terraform.py --ignore tests/test_terraform_modules.py --ignore tests/test_security.py --ignore tests/test_home_sandbox.py --ignore tests/test_manifest_ingest.py --ignore tests/test_llm_backends.py --ignore tests/test_install_strings.py --ignore tests/test_detect.py --ignore tests/test_erlang_extractor.py --ignore tests/test_r_extractor.py --ignore tests/test_solidity_extractor.py --ignore tests/test_vbnet_extractor.py -k "not (anthropic or openai or gemini or bedrock or ollama or test_label_communities_batches_when_over_batch_size or test_built_wheel_ships_the_full_skill_payload)"

%files
%doc README.md
%license LICENSE LICENSE-MIT NOTICE
%{_bindir}/graphify
%{python_sitelib}/graphify
%{python_sitelib}/graphifyy-%{version}.dist-info

%files mcp
%{_bindir}/graphify-mcp

%changelog
