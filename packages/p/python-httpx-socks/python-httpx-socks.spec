#
# spec file for package python-httpx-socks
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
Name:           python-httpx-socks%{psuffix}
Version:        0.10.0
Release:        0
Summary:        Proxy (HTTP, SOCKS) transports for httpx
License:        Apache-2.0
URL:            https://github.com/romis2012/httpx-socks
Source:         https://files.pythonhosted.org/packages/source/h/httpx-socks/httpx_socks-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module async-timeout}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module httpx-socks = %{version}}
BuildRequires:  %{python_module hypercorn}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module tiny-proxy}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module yarl}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-httpcore >= 0.17.3
Requires:       python-httpx >= 0.21.0
Requires:       python-python-socks >= 2.0.0
Suggests:       python-async-timeout >= 3.0.1
Suggests:       python-trio >= 0.16.0
BuildArch:      noarch
%python_subpackages

%description
Proxy (HTTP, SOCKS) transports for httpx

%prep
%autosetup -p1 -n httpx_socks-%{version}

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
%doc README.md
%license LICENSE.txt
%{python_sitelib}/httpx_socks
%{python_sitelib}/httpx_socks-%{version}.dist-info
%endif

%changelog
