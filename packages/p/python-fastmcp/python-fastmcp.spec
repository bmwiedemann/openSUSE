#
# spec file for package python-fastmcp
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


Name:           python-fastmcp
Version:        3.4.4
Release:        0
Summary:        The fast, Pythonic way to build MCP servers and clients
License:        Apache-2.0
URL:            https://github.com/jlowin/fastmcp
Source:         https://files.pythonhosted.org/packages/source/f/fastmcp/fastmcp-%{version}.tar.gz
BuildRequires:  %{python_module fastmcp-slim = %{version}}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-dynamic-versioning}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-fastmcp-slim = %{version}
BuildArch:      noarch
%python_subpackages

%description
FastMCP is the fast, Pythonic way to build Model Context Protocol (MCP)
servers and clients. This is the full distribution, pulling in fastmcp-slim
with the client and server integrations enabled; the importable "fastmcp"
module is provided by fastmcp-slim.

%prep
%autosetup -p1 -n fastmcp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import fastmcp"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fastmcp-%{version}.dist-info

%changelog
