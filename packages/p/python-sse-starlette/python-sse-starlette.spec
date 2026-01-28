#
# spec file for package python-sse-starlette
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


%{?sle15_python_module_pythons}
Name:           python-sse-starlette
Version:        3.2.0
Release:        0
Summary:        SSE plugin for Starlette
License:        BSD-3-Clause
URL:            https://github.com/sysid/sse-starlette
Source:         https://github.com/sysid/sse-starlette/archive/refs/tags/v%{version}.tar.gz#/sse_starlette-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module anyio >= 4.7.0}
BuildRequires:  %{python_module asgi-lifespan}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module starlette >= 0.41.3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-anyio >= 4.7.0
Requires:       python-starlette >= 0.41.3
Suggests:       python-uvicorn >= 0.34.0
Suggests:       python-fastapi >= 0.115.12
Suggests:       python-sqlalchemy >= 2.0.41
Suggests:       python-starlette >= 0.41.3
Suggests:       python-aiosqlite >= 0.21.0
Suggests:       python-uvicorn >= 0.34.0
Suggests:       python-granian >= 2.3.1
Suggests:       python-daphne >= 4.2.0
BuildArch:      noarch
%python_subpackages

%description
SSE plugin for Starlette

%prep
%autosetup -p1 -n sse-starlette-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
%pytest tests/test*.py

%files %{python_files}
%license LICENSE AUTHORS
%{python_sitelib}/sse_starlette
%{python_sitelib}/sse_starlette-%{version}.dist-info

%changelog
