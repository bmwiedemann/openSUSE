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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-httpcore%{psuffix}
Version:        0.15.0
Release:        0
Summary:        Minimal low-level Python HTTP client
License:        BSD-3-Clause
URL:            https://github.com/encode/httpcore
Source:         https://github.com/encode/httpcore/archive/%{version}.tar.gz#/httpcore-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3
Requires:       python-certifi
Requires:       python-h11 >= 0.11.0
Requires:       python-sniffio >= 1.0
Recommends:     python-h2 >= 3.0
Recommends:     python-socksio >= 1.0
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module h2 >= 3.0}
BuildRequires:  %{python_module httpcore = %{version}}
BuildRequires:  %{python_module pytest >= 7.0.1}
BuildRequires:  %{python_module pytest-asyncio >= 0.16.0}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest-trio >= 0.7.0}
BuildRequires:  %{python_module trio >= 0.19.0}
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
# gh#encode/httpcore#622 - test_request_with_content
%if %{with test}
%pytest -rs -k 'not (test_interfaces or test_no_retries or test_retries or test_threadsafe_basic or test_request_with_content or socks5)' --asyncio-mode=strict
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/httpcore
%{python_sitelib}/httpcore-%{version}*-info
%endif

%changelog
