#
# spec file for package skillspector
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


# Build the application against the distribution's primary python flavor
# only (this is an application, not a multi-flavour python library); follow
# %%{primary_python} so it stays correct as the primary interpreter moves.
%define pythons %{primary_python}
Name:           skillspector
Version:        2.3.9~git20260701.326a2b48
Release:        0
Summary:        Security scanner for AI agent skills
License:        Apache-2.0
URL:            https://github.com/NVIDIA/skillspector
Source:         %{name}-%{version}.tar.gz
# Test suite - exercises the full langchain/langgraph runtime cone
BuildRequires:  %{python_module PyYAML >= 6.0.1}
BuildRequires:  %{python_module anthropic}
BuildRequires:  %{python_module boto3 >= 1.34.0}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module httpx >= 0.28.0}
BuildRequires:  %{python_module langchain-anthropic >= 1.4.5}
BuildRequires:  %{python_module langchain-aws >= 0.2.0}
BuildRequires:  %{python_module langchain-core >= 1.2.17}
BuildRequires:  %{python_module langchain-openai >= 1.1.10}
BuildRequires:  %{python_module langgraph >= 1.0.10}
BuildRequires:  %{python_module langgraph-cli >= 0.4.14}
BuildRequires:  %{python_module langsmith >= 0.7.30}
BuildRequires:  %{python_module mcp >= 1.2.0}
BuildRequires:  %{python_module openai >= 2.25.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 2.12.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 14.3.0}
BuildRequires:  %{python_module typer >= 0.23.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module yara >= 4.5.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Runtime stack
Requires:       %{primary_python}-PyYAML >= 6.0.1
Requires:       %{primary_python}-boto3 >= 1.34.0
Requires:       %{primary_python}-httpx >= 0.28.0
Requires:       %{primary_python}-langchain-anthropic >= 1.4.5
Requires:       %{primary_python}-langchain-aws >= 0.2.0
Requires:       %{primary_python}-langchain-core >= 1.2.17
Requires:       %{primary_python}-langchain-openai >= 1.1.10
Requires:       %{primary_python}-langgraph >= 1.0.10
Requires:       %{primary_python}-langgraph-cli >= 0.4.14
Requires:       %{primary_python}-langsmith >= 0.7.30
Requires:       %{primary_python}-openai >= 2.25.0
Requires:       %{primary_python}-pydantic >= 2.12.0
Requires:       %{primary_python}-rich >= 14.3.0
# Upstream caps typer < 0.24 to avoid a click clash with semgrep; that cap is
# environment-specific, so only the floor is enforced here.
Requires:       %{primary_python}-typer >= 0.23.0
Requires:       %{primary_python}-yara >= 4.5.0
BuildArch:      noarch

%description
SkillSpector is a security scanner for AI agent skills (Claude Code,
Cursor, and similar). It scans skills for vulnerabilities, malicious
patterns and security risks before installation.

It supports Git repositories, URLs, zip archives and local directories,
runs static pattern checks (YARA rules, supply-chain/OSV lookups) and
optional LLM-based semantic analysis, and produces terminal, JSON, SARIF
and Markdown reports with risk scoring.

%package mcp
Summary:        MCP server mode for SkillSpector
Requires:       %{name} = %{version}
Requires:       %{primary_python}-mcp >= 1.2.0

%description mcp
This subpackage enables the Model Context Protocol (MCP) server mode of
SkillSpector, exposed through the "skillspector mcp" subcommand. It pulls
in the optional MCP runtime dependency so the FastMCP-based server can be
started for local CLI agents or over HTTP.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python_sitelib}
# Ship the baseline/suppression example under a non-hidden name.
cp -a .skillspector-baseline.example.yaml skillspector-baseline.example.yaml

%check
# The default addopts in pyproject.toml deselect the "integration" and
# "provider" markers (live LLM/provider endpoints); the offline unit suite
# exercises "import skillspector" against the full packaged langchain cone.
# The SSRF "allowed-host" positive tests need live DNS to resolve public
# hosts (github.com, gitlab.com, raw.githubusercontent.com); in the offline
# build chroot those names do not resolve and the SSRF guard blocks them, so
# they are deselected here (not skillspector bugs): the four in
# test_input_handler_ssrf.py plus three equivalents added upstream in
# test_input_handler.py.
%pytest --deselect tests/unit/test_input_handler_ssrf.py::TestGitCloneSSRF::test_github_url_allowed --deselect tests/unit/test_input_handler_ssrf.py::TestGitCloneSSRF::test_gitlab_url_allowed --deselect tests/unit/test_input_handler_ssrf.py::TestDownloadSSRF::test_raw_githubusercontent_allowed --deselect tests/unit/test_input_handler_ssrf.py::TestDownloadSSRF::test_download_does_not_follow_redirects --deselect tests/unit/test_input_handler.py::test_validate_url_host_scp_extracts_github --deselect tests/unit/test_input_handler.py::test_scp_valid_host_clones --deselect tests/unit/test_input_handler.py::test_https_url_unchanged

%files
%license LICENSE
%doc README.md skillspector-baseline.example.yaml
%{_bindir}/skillspector
%{python_sitelib}/skillspector
# Upstream pyproject pins a static version = 2.3.9, so the wheel dist-info
# keeps the release version, not the ~git snapshot RPM %%{version}.
%{python_sitelib}/skillspector-2.3.9.dist-info

%files mcp

%changelog
