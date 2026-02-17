#
# spec file for package python-a2wsgi
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


Name:           python-a2wsgi
Version:        1.10.10
Release:        0
Summary:        Convert WSGI app to ASGI app or ASGI app to WSGI app
License:        Apache-2.0
URL:            https://github.com/abersheeran/a2wsgi
Source:         https://files.pythonhosted.org/packages/source/a/a2wsgi/a2wsgi-%{version}.tar.gz
BuildRequires:  %{python_module baize >= 0.20.8}
BuildRequires:  %{python_module httpx >= 0.22}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module starlette >= 0.37.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Convert WSGI app to ASGI app or ASGI app to WSGI app.

Pure Python. Only depend on the standard library.

Compared with other converters, the advantage is that a2wsgi will not accumulate the requested content or response content in the memory, so you don't have to worry about the memory limit caused by a2wsgi. This problem exists in converters implemented by uvicorn/startlette or hypercorn.

%prep
%autosetup -p1 -n a2wsgi-%{version}

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
%{python_sitelib}/a2wsgi
%{python_sitelib}/a2wsgi-%{version}.dist-info

%changelog
