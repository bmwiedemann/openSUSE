#
# spec file for package python-tiny-proxy
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
Name:           python-tiny-proxy%{psuffix}
Version:        0.2.1
Release:        0
Summary:        Simple proxy server (SOCKS4(a), SOCKS5(h), HTTP tunnel)
License:        Apache-2.0
URL:            https://github.com/romis2012/tiny-proxy
# gh#romis2012/tiny-proxy#2
Source:         https://github.com/romis2012/tiny-proxy/archive/refs/tags/v%{version}.tar.gz#/tiny-proxy-%{version}.tar.gz
# Source:         https://files.pythonhosted.org/packages/source/t/tiny-proxy/tiny_proxy-%%{version}.tar.gz
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module anyio >= 3.6.1}
BuildRequires:  %{python_module pytest}
# BuildRequires:  %%{python_module aiohttp-socks}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module httpx-socks}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module trustme}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-anyio >= 3.6.1
Requires:       python-httpx
BuildArch:      noarch
%python_subpackages

%description
Simple proxy server (SOCKS4(a), SOCKS5(h), HTTP tunnel)

%prep
%autosetup -p1 -n tiny-proxy-%{version}

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
%pytest
%endif

%if %{without test}
%files %{python_files}
%{python_sitelib}/tiny_proxy
%{python_sitelib}/tiny_proxy-%{version}.dist-info
%endif

%changelog
