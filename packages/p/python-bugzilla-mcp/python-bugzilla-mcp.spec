#
# spec file for package python-bugzilla-mcp
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


# upstream requires Python >= 3.13
%define pythons python313
Name:           python-bugzilla-mcp
Version:        0.14.0
Release:        0
Summary:        Model Context Protocol server for Bugzilla
License:        Apache-2.0
URL:            https://github.com/mcp-bugzilla/mcp-bugzilla
Source:         https://files.pythonhosted.org/packages/source/m/mcp-bugzilla/mcp_bugzilla-%{version}.tar.gz
BuildRequires:  %{python_module fastmcp >= 3.4.0}
BuildRequires:  %{python_module httpx-retries >= 0.5.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-fastmcp >= 3.4.0
Requires:       python-httpx-retries >= 0.5.0
BuildArch:      noarch
%python_subpackages

%description
An MCP (Model Context Protocol) server exposing Bugzilla as a set of tools,
so MCP-capable clients can search, read and act on Bugzilla bugs.

%prep
%autosetup -p1 -n mcp_bugzilla-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mcp-bugzilla
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/mcp_bugzilla
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import mcp_bugzilla"

%post
%python_install_alternative mcp-bugzilla

%postun
%python_uninstall_alternative mcp-bugzilla

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/mcp-bugzilla
%{python_sitelib}/mcp_bugzilla
%{python_sitelib}/mcp_bugzilla-%{version}.dist-info

%changelog
