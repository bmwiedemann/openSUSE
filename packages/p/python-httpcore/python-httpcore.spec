#
# spec file
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-httpcore%{psuffix}
Version:        0.14.5
Release:        0
Summary:        Minimal low-level Python HTTP client
License:        BSD-3-Clause
URL:            https://github.com/encode/httpcore
Source:         https://github.com/encode/httpcore/archive/%{version}.tar.gz#/httpcore-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3.1.0
Requires:       python-certifi
Requires:       python-chardet >= 3.0
Requires:       python-h11 >= 0.11.0
Requires:       python-h2 >= 3.0
Requires:       python-idna >= 2.0
Requires:       python-rfc3986 >= 1.0
Requires:       python-sniffio >= 1.0
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module anyio >= 3.1.0}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module chardet >= 3.0}
BuildRequires:  %{python_module h11 >= 0.11.0}
BuildRequires:  %{python_module h2 >= 3.0}
BuildRequires:  %{python_module idna >= 2.0}
BuildRequires:  %{python_module mitmproxy}
BuildRequires:  %{python_module pproxy >= 2.7.8}
BuildRequires:  %{python_module pytest >= 6.2.4}
BuildRequires:  %{python_module pytest-asyncio >= 0.15.1}
BuildRequires:  %{python_module pytest-curio}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest-trio >= 0.7.0}
BuildRequires:  %{python_module pytest-twisted}
BuildRequires:  %{python_module rfc3986 >= 1.0}
BuildRequires:  %{python_module trustme >= 0.7.0}
BuildRequires:  %{python_module uvicorn >= 0.12.1}
%endif
# /SECTION
%python_subpackages

%description
Python minimal low-level HTTP client.

%prep
%setup -q -n httpcore-%{version}
#sed -i 's/"localhost"/"127.0.0.1"/' tests/*sync_tests/test_interfaces.py tests/conftest.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
# ulimit -n 50000
# test_no_retries and test_retries are very slow and fails
# tests/async_tests + tests/sync_tests causes open file limit
# socks5 -- we don't ship socksio
%if %{with test}
%pytest -rs -k 'not (test_interfaces or test_no_retries or test_retries or test_threadsafe_basic or socks5)'
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/*
%endif

%changelog
