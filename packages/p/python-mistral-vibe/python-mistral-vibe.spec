#
# spec file for package python-mistral-vibe
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

%define skip_python311 1
Name:           python-mistral-vibe
Version:        2.0.2
Release:        0
Summary:        Minimal CLI coding agent by Mistral
License:        Apache-2.0
URL:            https://github.com/mistralai/mistral-vibe
Source0:        https://files.pythonhosted.org/packages/source/m/mistral_vibe/mistral_vibe-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module editables}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module agent-client-protocol >= 0.6.3}
BuildRequires:  %{python_module anyio >= 4.12.0}
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module jinja2}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module syrupy}
BuildRequires:  %{python_module tree-sitter}
BuildRequires:  %{python_module tree-sitter-bash}
BuildRequires:  %{python_module mcp >= 1.14.0}
BuildRequires:  %{python_module mistralai >= 1.9.11}
BuildRequires:  %{python_module packaging >= 24.1}
BuildRequires:  %{python_module pexpect >= 4.9.0}
BuildRequires:  %{python_module pydantic-settings >= 2.12.0}
BuildRequires:  %{python_module pydantic >= 2.12.4}
BuildRequires:  %{python_module pyperclip >= 1.11.0}
BuildRequires:  %{python_module pytest-asyncio >= 1.2.0}
BuildRequires:  %{python_module pytest-textual-snapshot >= 1.1.0}
BuildRequires:  %{python_module pytest-timeout >= 2.4.0}
BuildRequires:  %{python_module pytest-xdist >= 3.8.0}
BuildRequires:  %{python_module python-dotenv >= 1.0.0}
BuildRequires:  %{python_module PyYAML >= 6.0.0}
BuildRequires:  %{python_module respx >= 0.22.0}
BuildRequires:  %{python_module rich >= 14.0.0}
BuildRequires:  %{python_module textual >= 6.3.0}
BuildRequires:  %{python_module textual-speedups >= 0.2.1}
BuildRequires:  %{python_module tomli-w >= 1.2.0}
BuildRequires:  %{python_module watchfiles >= 1.1.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-agent-client-protocol >= 0.6.3
Requires:       python-aiofiles >= 24.1.0
Requires:       python-httpx >= 0.28.1
Requires:       python-mcp >= 1.14.0
Requires:       python-mistralai >= 1.9.11
Requires:       python-packaging >= 24.1
Requires:       python-pexpect >= 4.9.0
Requires:       python-pydantic >= 2.12.4
Requires:       python-pydantic-settings >= 2.12.0
Requires:       python-pyperclip >= 1.11.0
Requires:       python-pytest-xdist >= 3.8.0
Requires:       python-python-dotenv >= 1.0.0
Requires:       python-rich >= 14.0.0
Requires:       python-textual >= 6.3.0
Requires:       python-textual-speedups >= 0.2.1
Requires:       python-tomli-w >= 1.2.0
Requires:       python-watchfiles >= 1.1.1
Requires:       python-tree-sitter
Requires:       python-tree-sitter-bash
BuildArch:      noarch
%python_subpackages

%description
Mistral Vibe is a command-line coding assistant powered by Mistral's
models. It provides a conversational interface to your codebase,
allowing you to use natural language to explore, modify, and interact
with your projects through a powerful set of tools.

%prep
%autosetup -p1 -n mistral_vibe-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/vibe
%python_clone -a %{buildroot}%{_bindir}/vibe-acp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest || true

%post
%python_install_alternative vibe vibe-acp

%postun
%python_uninstall_alternative vibe

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/vibe
%python_alternative %{_bindir}/vibe-acp
%{python_sitelib}/vibe
%{python_sitelib}/mistral_vibe-%{version}.dist-info

%changelog
