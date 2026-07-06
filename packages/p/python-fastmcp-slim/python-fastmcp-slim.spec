#
# spec file for package python-fastmcp-slim
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


Name:           python-fastmcp-slim
Version:        3.4.3
Release:        0
Summary:        The fast, Pythonic way to build MCP servers and clients (slim)
License:        Apache-2.0
URL:            https://github.com/jlowin/fastmcp
Source:         https://files.pythonhosted.org/packages/source/f/fastmcp_slim/fastmcp_slim-%{version}.tar.gz
BuildRequires:  %{python_module Authlib >= 1.6.11}
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module cyclopts >= 4.0.0}
BuildRequires:  %{python_module email-validator}
BuildRequires:  %{python_module exceptiongroup >= 1.2.2}
BuildRequires:  %{python_module griffelib >= 2.0.0}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module joserfc >= 1.1.0}
BuildRequires:  %{python_module jsonref >= 1.1.0}
BuildRequires:  %{python_module jsonschema-path >= 0.3.4}
BuildRequires:  %{python_module mcp >= 1.24.0}
BuildRequires:  %{python_module openapi-pydantic >= 0.5.1}
BuildRequires:  %{python_module opentelemetry-api >= 1.20.0}
BuildRequires:  %{python_module packaging >= 24.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs >= 4.0.0}
BuildRequires:  %{python_module py-key-value-aio >= 0.4.4}
BuildRequires:  %{python_module pydantic >= 2.11.7}
BuildRequires:  %{python_module pydantic-settings >= 2.0.0}
BuildRequires:  %{python_module pyperclip >= 1.9.0}
BuildRequires:  %{python_module python-dotenv >= 1.1.0}
BuildRequires:  %{python_module python-multipart >= 0.0.26}
BuildRequires:  %{python_module rich >= 13.9.4}
BuildRequires:  %{python_module starlette >= 1.0.1}
BuildRequires:  %{python_module typing_extensions >= 4.0.0}
BuildRequires:  %{python_module uncalled-for >= 0.2.0}
BuildRequires:  %{python_module uv-dynamic-versioning >= 0.7.0}
BuildRequires:  %{python_module uvicorn >= 0.35}
BuildRequires:  %{python_module watchfiles >= 1.0.0}
BuildRequires:  %{python_module websockets >= 15.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# uv-backend wheels don't expose deps to pythondistdeps, so require them by hand
Requires:       python-Authlib >= 1.6.11
Requires:       python-PyYAML >= 6.0
Requires:       python-cyclopts >= 4.0.0
Requires:       python-email-validator
Requires:       python-exceptiongroup >= 1.2.2
Requires:       python-griffelib >= 2.0.0
Requires:       python-httpx >= 0.28.1
Requires:       python-joserfc >= 1.1.0
Requires:       python-jsonref >= 1.1.0
Requires:       python-jsonschema-path >= 0.3.4
Requires:       python-mcp >= 1.24.0
Requires:       python-openapi-pydantic >= 0.5.1
Requires:       python-opentelemetry-api >= 1.20.0
Requires:       python-packaging >= 24.0
Requires:       python-platformdirs >= 4.0.0
Requires:       python-py-key-value-aio >= 0.4.4
Requires:       python-pydantic >= 2.11.7
Requires:       python-pydantic-settings >= 2.0.0
Requires:       python-pyperclip >= 1.9.0
Requires:       python-python-dotenv >= 1.1.0
Requires:       python-python-multipart >= 0.0.26
Requires:       python-rich >= 13.9.4
Requires:       python-starlette >= 1.0.1
Requires:       python-typing_extensions >= 4.0.0
Requires:       python-uncalled-for >= 0.2.0
Requires:       python-uvicorn >= 0.35
Requires:       python-watchfiles >= 1.0.0
Requires:       python-websockets >= 15.0.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
FastMCP is the fast, Pythonic way to build Model Context Protocol (MCP)
servers and clients. This "slim" distribution provides the full client
and server stack with the standard set of optional integrations enabled.

%prep
%autosetup -p1 -n fastmcp_slim-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/fastmcp
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/fastmcp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import fastmcp"

%post
%python_install_alternative fastmcp

%postun
%python_uninstall_alternative fastmcp

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/fastmcp
%{python_sitelib}/fastmcp
%{python_sitelib}/fastmcp_slim-%{version}.dist-info

%changelog
