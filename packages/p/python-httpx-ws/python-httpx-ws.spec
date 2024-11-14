#
# spec file for package python-httpx-ws
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


Name:           python-httpx-ws
Version:        0.6.2
Release:        0
Summary:        WebSockets support for HTTPX
License:        MIT
URL:            https://github.com/frankie567/httpx-ws
Source:         https://files.pythonhosted.org/packages/source/h/httpx_ws/httpx_ws-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 4
Requires:       python-httpcore >= 1.0.4
Requires:       python-httpx >= 0.23.1
Requires:       python-wsproto
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module anyio >= 4}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module httpcore >= 1.0.4}
BuildRequires:  %{python_module httpx >= 0.23.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module uvicorn}
BuildRequires:  %{python_module wsproto}
# /SECTION
%python_subpackages

%description
WebSockets support for HTTPX
* [X] Sync and async client
* [X] Helper methods to send text, binary and JSON data
* [X] Helper methods to receive text, binary and JSON data
* [X] Automatic ping/pong answers
* [X] HTTPX transport to test WebSockets defined in ASGI apps
* [X] Automatic keepalive ping
* [X] asyncio and Trio support through AnyIO

%prep
%autosetup -p1 -n httpx_ws-%{version}
sed -i /addopts/d pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# hangs inside obs
donttest="websockets"
# flaky
donttest="$donttest or test_async_keepalive_ping"
%pytest -k "not ($donttest)"

%files %{python_files}
%{python_sitelib}/httpx_ws
%{python_sitelib}/httpx_ws-%{version}.dist-info

%changelog
