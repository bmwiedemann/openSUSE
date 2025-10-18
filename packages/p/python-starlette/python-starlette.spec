#
# spec file for package python-starlette
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

%{?sle15_python_module_pythons}
Name:           python-starlette%{psuffix}
Version:        0.48.0
Release:        0
Summary:        Lightweight ASGI framework/toolkit
License:        BSD-3-Clause
URL:            https://github.com/encode/starlette
Source:         https://github.com/encode/starlette/archive/refs/tags/%{version}.tar.gz#/starlette-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3.6.2
Requires:       (python-typing_extensions >= 4.10.0 if python-base < 3.13)
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module anyio >= 3.6.2}
# typing_extensions, see below
# SECTION [full]
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module httpx >= 0.28}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module python-multipart >= 0.0.18}
# /SECTION
# SECTION test
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module asyncio}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trio}
# testing requires it for all flavors
BuildRequires:  %{python_module typing_extensions >= 4.10.0}
BuildRequires:  %{python_module importlib-metadata >= 7.0.1}
# /SECITON
%endif
%python_subpackages

%description
Starlette is a lightweight ASGI framework/toolkit, which is ideal for
building high performance asyncio services.

%prep
%autosetup -p1 -n starlette-%{version}

%build
%if ! %{with test}
%pyproject_wheel
%endif

%install
%if ! %{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# The following tests don't work in some archs because time_t cannot
# hold the values the test expect, as they go beyond the maximum
# value in i586 and armv7l. As we are using Buildarch: noarch, we
# cannot just use ifarch conditionals here...
ignored_tests="test_set_cookie"
ignored_tests="$ignored_tests or test_expires_on_set_cookie"
# fails to raise a deprecation warning as of 2024/04/25
##ignored_tests="$ignored_tests or test_lifespan_with_on_events"
%pytest -W ignore::PendingDeprecationWarning --asyncio-mode=strict -k "not ($ignored_tests)"

%endif

%if ! %{with test}
%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/starlette
%{python_sitelib}/starlette-%{version}.dist-info
%endif

%changelog
