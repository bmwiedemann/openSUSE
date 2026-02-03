#
# spec file for package python-mcp
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           python-mcp
Version:        1.23.3
Release:        0
Summary:        Python implementation of the Model Context Protocol
License:        MIT
Group:          Development/Languages/Python
# GitHub repo https://github.com/modelcontextprotocol/python-sdk
URL:            https://modelcontextprotocol.io/introduction
Source:         https://files.pythonhosted.org/packages/source/m/mcp/mcp-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 4.5
Requires:       python-httpx >= 0.27
Requires:       python-httpx-sse >= 0.4
Requires:       python-pydantic >= 2.7.2
Requires:       python-pydantic-settings >= 2.5.2
Requires:       python-python-multipart >= 0.0.9
Requires:       python-sse-starlette >= 1.6.1
Requires:       python-starlette >= 0.27
Requires:       python-uvicorn >= 0.23.1
BuildArch:      noarch
%python_subpackages

%description
Model Context Protocol (or Master Control Program?) implementation
for python.

%package devel
Summary:        Executables for %{name}
Conflicts:      mmv
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description devel
This package contains the executables for %{name}.

%prep
%autosetup -p1 -n mcp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python_sitelib}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/mcp

%post devel
%python_expand %python_install_alternative mcp

%postun devel
%python_expand %python_uninstall_alternative mcp

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/mcp
%{python_sitelib}/mcp-%{version}*-info

%files %{python_files devel}
%license LICENSE
%python_alternative %{_bindir}/mcp

%changelog
