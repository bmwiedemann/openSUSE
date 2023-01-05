#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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

%define skip_python2 1
Name:           python-starlette%{psuffix}
Version:        0.23.1
Release:        0
Summary:        Lightweight ASGI framework/toolkit
License:        BSD-3-Clause
URL:            https://github.com/encode/starlette
Source:         https://github.com/encode/starlette/archive/refs/tags/%{version}.tar.gz#/starlette-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3.4.0
Requires:       (python-typing_extensions >= 3.10.0 if python-base < 3.10)
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module anyio >= 3.4.0}
# typing_extensions, see below
# SECTION [full]
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module httpx >= 0.22}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module python-multipart}
# /SECTION
# SECTION test
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trio}
# testing requires it for all flavors
BuildRequires:  %{python_module typing_extensions}
# /SECITON
%endif
%python_subpackages

%description
Starlette is a lightweight ASGI framework/toolkit, which is ideal for
building high performance asyncio services.

%prep
%autosetup -n starlette-%{version}

%build
%pyproject_wheel

%install
%if ! %{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# Remove unrecognized arguments: --strict-config --strict-markers
sed -i "s|--strict-config||" setup.cfg
sed -i "s|--strict-markers||" setup.cfg
sed -i "s| error$||" setup.cfg
%pytest --asyncio-mode=strict
%endif

%if ! %{with test}
%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/starlette
%{python_sitelib}/starlette-%{version}*-info
%endif

%changelog
