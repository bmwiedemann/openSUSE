#
# spec file for package python-pycrdt-websocket
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pycrdt-websocket%{?psuffix}
Version:        0.15.5
Release:        0
Summary:        WebSocket connector for pycrdt
License:        MIT
URL:            https://github.com/jupyter-server/pycrdt-websocket
Source:         https://files.pythonhosted.org/packages/source/p/pycrdt_websocket/pycrdt_websocket-%{version}.tar.gz
# for testing, not installed; create through `npm install ws y-websocket && tar cJf node_modules.tar.xz node_modules package.json`
Source10:       node_modules.tar.xz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3.6.2
Requires:       (python-pycrdt >= 0.10.3 with python-pycrdt < 0.13)
Requires:       (python-sqlite-anyio >= 0.2.3 with python-sqlite-anyio < 0.3.0)
Provides:       python-pycrdt_websocket = %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module httpx-ws >= 0.5.2}
BuildRequires:  %{python_module hypercorn if %python-base >= 3.11}
BuildRequires:  %{python_module pycrdt-websocket = %{version}}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trio}
BuildRequires:  nodejs
%endif
BuildArch:      noarch
%python_subpackages

%description
Pycrdt-websocket is a Python library for building WebSocket servers
and clients that connect and synchronize shared documents.
It can be used to create collaborative web applications.

%prep
%autosetup -p1 -n pycrdt_websocket-%{version} -a10

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/pycrdt_websocket
%{python_sitelib}/pycrdt_websocket-%{version}.dist-info
%endif

%changelog
