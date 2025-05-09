#
# spec file for package python-elastic-transport
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


%{?sle15_python_module_pythons}
Name:           python-elastic-transport
Version:        8.17.1
Release:        0
Summary:        Transport classes and utilities shared among Python Elastic client libraries
License:        Apache-2.0
URL:            https://github.com/elastic/elastic-transport-python
Source:         https://github.com/elastic/elastic-transport-python/archive/refs/tags/v%{version}.tar.gz#/elastic-transport-python-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       python-urllib3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module opentelemetry-api}
BuildRequires:  %{python_module opentelemetry-sdk}
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module respx}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module urllib3}
# /SECTION
%python_subpackages

%description
Transport classes and utilities shared among Python Elastic client libraries

%prep
%autosetup -p1 -n elastic-transport-python-%{version}
sed -i '/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# these tests fail without proper name resolution or online connection to httpbin.org and badssl.com
donttest="(test_http_aiohttp and not TestAiohttpHttpNode)"
donttest="$donttest or test_tls_versions"
donttest="$donttest or test_assert_fingerprint_in_cert_chain"
donttest="$donttest or (test_ssl_assert_fingerprint and httpx)"
# Fails in 3.12 with DeprecationWarning
donttest="$donttest or test_simple_request"
# Mocking error with httpx 0.28 / patched respx
donttest="$donttest or (TestHttpxAsyncNode and not Creation)"
# Flaky test
donttest="$donttest or test_decimal_serialization[OrjsonSerializer]"
donttest="$donttest or test_sniff_before_requests or test_sniffed_nodes_added_to_pool or test_sniff_on_node_failure"
%pytest -W ignore::DeprecationWarning -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/elastic_transport
%{python_sitelib}/elastic_transport-%{version}.dist-info

%changelog
