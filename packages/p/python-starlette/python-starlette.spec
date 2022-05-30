#
# spec file for package python-starlette
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-starlette
Version:        0.19.1
Release:        0
Summary:        Lightweight ASGI framework/toolkit
License:        BSD-3-Clause
URL:            https://github.com/encode/starlette
Source:         https://github.com/encode/starlette/archive/refs/tags/%{version}.tar.gz#/starlette-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aiofiles}
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module contextlib2}
BuildRequires:  %{python_module databases}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module graphene}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-multipart}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  (python3-aiocontextvars if python3-base < 3.7)
BuildRequires:  (python36-aiocontextvars if python36-base)
BuildArch:      noarch
%python_subpackages

%description
Starlette is a lightweight ASGI framework/toolkit, which is ideal for
building high performance asyncio services.

%prep
%autosetup -n starlette-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Remove unrecognized arguments: --strict-config --strict-markers
sed -i "s|--strict-config||" setup.cfg
sed -i "s|--strict-markers||" setup.cfg
sed -i "s| error$||" setup.cfg
%pytest --asyncio-mode=strict

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/starlette
%{python_sitelib}/starlette-%{version}*-info

%changelog
