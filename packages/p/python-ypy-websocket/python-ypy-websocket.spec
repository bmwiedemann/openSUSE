#
# spec file for package python-ypy-websocket
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-ypy-websocket
Version:        0.12.4
Release:        0
Summary:        WebSocket connector for Ypy
License:        MIT
URL:            https://github.com/y-crdt/ypy-websocket
Source:         https://files.pythonhosted.org/packages/source/y/ypy_websocket/ypy_websocket-%{version}.tar.gz
# for testing, not installed; create through `npm install yjs y-websocket && tar cJf node_modules.tar.xz node_modules package.json`
Source10:       node_modules.tar.xz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-aiosqlite >= 0.18.0 with python-aiosqlite < 1)
Requires:       (python-anyio >= 3.6.2 with python-anyio < 5)
Requires:       (python-typing_extensions if python-base < 3.8)
Requires:       (python-y-py >= 0.6 with python-y-py < 0.7)
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module anyio >= 3.6.2 with %python-anyio < 5}
BuildRequires:  %{python_module aiosqlite >= 0.18.0 with %python-aiosqlite < 1}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.8}
BuildRequires:  %{python_module uvicorn}
BuildRequires:  %{python_module websockets >= 10.0}
BuildRequires:  %{python_module y-py >= 0.6 with %python-y-py < 0.7}
BuildRequires:  nodejs
# /SECTION
%python_subpackages

%description
An async WebSocket connector for Ypy.

%prep
%autosetup -p1 -n ypy_websocket-%{version} -a10

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ypy_websocket
%{python_sitelib}/ypy_websocket-%{version}.dist-info

%changelog
