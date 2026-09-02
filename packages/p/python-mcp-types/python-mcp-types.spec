#
# spec file for package python-mcp-types
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


Name:           python-mcp-types
Version:        2.1.1
Release:        0
Summary:        Model Context Protocol wire types
License:        MIT
URL:            https://github.com/modelcontextprotocol/python-sdk
# mcp-types is a subproject of the python-sdk monorepo; its PyPI sdist ships no
# tests, so build from the tag archive, which carries tests/types/.
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/python-sdk-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-dynamic-versioning}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 2.12.0
Requires:       python-typing_extensions >= 4.13.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module inline-snapshot}
BuildRequires:  %{python_module pydantic >= 2.12.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 4.13.0}
# /SECTION
%python_subpackages

%description
The wire types for the Model Context Protocol: the protocol message models,
JSON-RPC envelope types, per-version surface validators and the protocol
version registry. Its only runtime dependencies are pydantic and
typing-extensions, so MCP traffic can be (de)serialized without pulling in the
full mcp SDK.

%prep
%autosetup -p1 -n python-sdk-%{version}
# only tests/types/ covers mcp_types; the rest of the tree (and the root
# conftest) needs the full mcp SDK, which this package does not build
find tests -mindepth 1 -maxdepth 1 -not -name types -not -name __init__.py -exec rm -rf {} +

%build
# no git checkout in the tarball, so the vcs version source has nothing to read
export UV_DYNAMIC_VERSIONING_BYPASS=%{version}
pushd src/mcp-types
%pyproject_wheel
popd

%install
pushd src/mcp-types
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# addopts pulls in the SDK's pytest plugins and filterwarnings names
# mcp.MCPDeprecationWarning; neither exists without the full mcp package
%pytest -o addopts= -o filterwarnings=error tests/types

%files %{python_files}
%doc src/mcp-types/README.md
%license LICENSE
%{python_sitelib}/mcp_types
%{python_sitelib}/mcp_types-%{version}.dist-info

%changelog
