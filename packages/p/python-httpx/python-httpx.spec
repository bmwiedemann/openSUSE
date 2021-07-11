#
# spec file for package python-httpx
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-httpx
Version:        0.18.0
Release:        0
Summary:        Python HTTP client with async support
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/encode/httpx
Source:         https://github.com/encode/httpx/archive/%{version}.tar.gz#/httpx-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli >= 0.7.0
Requires:       python-certifi
Requires:       python-chardet >= 3.0
Requires:       python-h11 >= 0.8.0
Requires:       python-h2 >= 3.0
Requires:       python-hstspreload >= 2019.8.27
Requires:       python-httpcore >= 0.13.0
Requires:       python-idna >= 2.0
Requires:       python-rfc3986 >= 1.3
Requires:       python-sniffio
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Brotli >= 0.7.0}
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module chardet >= 3.0}
BuildRequires:  %{python_module h11 >= 0.8.0}
BuildRequires:  %{python_module h2 >= 3.0}
BuildRequires:  %{python_module hstspreload >= 2019.8.27}
BuildRequires:  %{python_module httpcore >= 0.13.0}
BuildRequires:  %{python_module idna >= 2.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rfc3986 >= 1.3}
BuildRequires:  %{python_module sniffio}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module uvicorn}
BuildRequires:  %{python_module uvloop}
# /SECTION
%python_subpackages

%description
Python HTTP client with async support.

%prep
%setup -q -n httpx-%{version}
rm setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_start_tls_on_*_socket_stream and test_connect_timeout require network
%pytest -k 'not (test_start_tls_on_tcp_socket_stream or test_start_tls_on_uds_socket_stream or test_connect_timeout or test_async_proxy_close or test_sync_proxy_close)'

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{python_sitelib}/httpx*

%changelog
