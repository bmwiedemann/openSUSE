#
# spec file for package mcp-server-cockpit
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


%define pythons %{primary_python}
Name:           mcp-server-cockpit
Version:        0.1.2
Release:        0
Summary:        MCP server exposing Cockpit bundle actions as tools
License:        MIT
URL:            https://github.com/mslacken/cockpit-mcp
Source0:        %{url}/archive/v%{version}/cockpit-mcp-%{version}.tar.gz
BuildRequires:  %{python_module mcp >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module tree-sitter >= 0.25}
BuildRequires:  %{python_module tree-sitter-javascript >= 0.23}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{primary_python}-mcp >= 1.0
# cockpit_js_parser uses tree_sitter.QueryCursor, which needs 0.25;
# upstream's metadata only declares >= 0.23
Requires:       %{primary_python}-tree-sitter >= 0.25
Requires:       %{primary_python}-tree-sitter-javascript >= 0.23
BuildRequires:  tree-sitter
BuildRequires:  tree-sitter-javascript
Requires:       tree-sitter
Requires:       tree-sitter-javascript
Provides:       cockpit-mcp = %{version}-%{release}
BuildArch:      noarch

%description
cockpit-mcp extracts the actions the Cockpit web console bundles perform on
a Linux host (spawned commands, D-Bus calls, file accesses) by parsing the
JavaScript bundles, and serves them as tools over the Model Context Protocol
(MCP). It can fetch the bundles from a running Cockpit instance and perform
the calls over the cockpit-bridge session WebSocket.

%prep
%autosetup -p1 -n cockpit-mcp-%{version}
# the modules are installed into site-packages, not run directly
sed -i '1{/^#!/d}' cockpit_*.py
chmod -x cockpit_*.py

%build
%pyproject_wheel

%install
%pyproject_install
# /usr/bin/cockpit-bridge belongs to cockpit-bridge from the cockpit package
mv %{buildroot}%{_bindir}/cockpit-bridge %{buildroot}%{_bindir}/cockpit-mcp-bridge
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -P -c "import cockpit_bridge, cockpit_js_parser, cockpit_list_tools, cockpit_mcp_server_ng"
PYTHONPATH=%{buildroot}%{python_sitelib} %{buildroot}%{_bindir}/cockpit-mcp --version

%files
%license LICENSE
%doc README.md
%{_bindir}/cockpit-mcp
%{_bindir}/cockpit-mcp-bridge
%{_bindir}/cockpit-js-parser
%{_bindir}/cockpit-list-tools
%{python_sitelib}/cockpit_bridge.py
%{python_sitelib}/cockpit_js_parser.py
%{python_sitelib}/cockpit_list_tools.py
%{python_sitelib}/cockpit_mcp_server_ng.py
%{python_sitelib}/__pycache__/cockpit_*.pyc
%{python_sitelib}/cockpit_mcp-%{version}.dist-info

%changelog
