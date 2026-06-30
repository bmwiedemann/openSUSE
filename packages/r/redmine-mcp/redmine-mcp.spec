#
# spec file for package redmine-mcp
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


# This is a single-flavour application, not a multi-flavour module, so build
# it against the distribution's primary Python flavour.
%define pythons %{primary_python}
Name:           redmine-mcp
Version:        2026.1.13.152335
Release:        0
Summary:        Model Context Protocol server for Redmine
License:        MPL-2.0
URL:            https://github.com/runekaagaard/mcp-redmine
Source:         https://files.pythonhosted.org/packages/source/m/mcp_redmine/mcp_redmine-%{version}.tar.gz
BuildRequires:  %{primary_python}-PyYAML >= 6.0.2
BuildRequires:  %{primary_python}-hatchling
BuildRequires:  %{primary_python}-httpx >= 0.28.1
BuildRequires:  %{primary_python}-mcp >= 1.9.0
BuildRequires:  %{primary_python}-openapi-core >= 0.19.4
BuildRequires:  %{primary_python}-pip
BuildRequires:  %{primary_python}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{primary_python}-PyYAML >= 6.0.2
Requires:       %{primary_python}-httpx >= 0.28.1
Requires:       %{primary_python}-mcp >= 1.9.0
Requires:       %{primary_python}-openapi-core >= 0.19.4
BuildArch:      noarch

%description
An MCP (Model Context Protocol) server exposing a Redmine instance as a set
of tools, so MCP-capable clients can search, read and act on Redmine issues,
projects, wikis and time entries through Redmine's REST API.

%prep
%autosetup -p1 -n mcp_redmine-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
python%{python_version} -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{python_sitelib}/mcp_redmine
%fdupes %{buildroot}%{python_sitelib}

%check
# server.py reads REDMINE_URL/REDMINE_API_KEY at import time; provide dummies
# for this smoke-import test (upstream ships no test suite)
REDMINE_URL=http://localhost REDMINE_API_KEY=dummy \
    PYTHONPATH=%{buildroot}%{python_sitelib} python%{python_version} -Bc "import mcp_redmine.server"

%files
%license LICENSE
%doc README.md
%{_bindir}/mcp-redmine
%{python_sitelib}/mcp_redmine
%{python_sitelib}/mcp_redmine-%{version}.dist-info

%changelog
