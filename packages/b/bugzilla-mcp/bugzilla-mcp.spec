#
# spec file for package bugzilla-mcp
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


# Build the application against the distribution's primary Python flavour
# (upstream requires Python >= 3.13); this is a single-flavour application,
# not a multi-flavour module.
%define pythons %{primary_python}
Name:           bugzilla-mcp
Version:        0.15.1
Release:        0
Summary:        Model Context Protocol server for Bugzilla
License:        Apache-2.0
URL:            https://github.com/mcp-bugzilla/mcp-bugzilla
Source:         https://files.pythonhosted.org/packages/source/m/mcp_bugzilla/mcp_bugzilla-%{version}.tar.gz
BuildRequires:  %{primary_python}-fastmcp >= 3.4.2
BuildRequires:  %{primary_python}-httpx-retries >= 0.5.0
BuildRequires:  %{primary_python}-pip
BuildRequires:  %{primary_python}-uv-build
BuildRequires:  %{primary_python}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{primary_python}-fastmcp >= 3.4.2
Requires:       %{primary_python}-httpx-retries >= 0.5.0
Provides:       python313-bugzilla-mcp = %{version}-%{release}
Obsoletes:      python313-bugzilla-mcp < %{version}
BuildArch:      noarch

%description
An MCP (Model Context Protocol) server exposing Bugzilla as a set of tools,
so MCP-capable clients can search, read and act on Bugzilla bugs.

%prep
%autosetup -p1 -n mcp_bugzilla-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
python%{python_version} -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{python_sitelib}/mcp_bugzilla
%fdupes %{buildroot}%{python_sitelib}

%check
PYTHONPATH=%{buildroot}%{python_sitelib} python%{python_version} -Bc "import mcp_bugzilla"

%files
%doc README.md
%{_bindir}/mcp-bugzilla
%{python_sitelib}/mcp_bugzilla
%{python_sitelib}/mcp_bugzilla-%{version}.dist-info

%changelog
