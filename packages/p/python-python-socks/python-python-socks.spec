#
# spec file for package python-python-socks
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-python-socks%{psuffix}
Version:        2.5.3
Release:        0
Summary:        Core proxy client functionality for Python
License:        Apache-2.0
URL:            https://github.com/romis2012/python-socks
# gh#romis2012/python-socks#30
Source:         https://github.com/romis2012/python-socks/archive/refs/tags/v%{version}.tar.gz#/python-socks-%{version}.tar.gz
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module async-timeout}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
# Source:         https://files.pythonhosted.org/packages/source/p/python-socks/python-socks-%%{version}.tar.gz
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module async_timeout}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tiny-proxy}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module yarl}
%endif
%python_subpackages

%description
The python-socks package provides a core proxy client functionality for Python.
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async
(asyncio, trio, curio) APIs. You probably don't need to use python-socks
directly. It is used internally by aiohttp-socks and httpx-socks packages.

%prep
%autosetup -p1 -n python-socks-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# try at least a simple import
%pytest
%endif

%if %{without test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/python_socks
%{python_sitelib}/python_socks-%{version}.dist-info
%endif

%changelog
