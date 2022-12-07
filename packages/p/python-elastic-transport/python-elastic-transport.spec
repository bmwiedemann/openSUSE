#
# spec file for package python-elastic-transport
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
Name:           python-elastic-transport
Version:        8.4.0
Release:        0
Summary:        Transport classes and utilities shared among Python Elastic client libraries
License:        Apache-2.0
URL:            https://github.com/elastic/elastic-transport-python
Source:         https://github.com/elastic/elastic-transport-python/archive/refs/tags/v%{version}.tar.gz#/elastic-transport-python-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       (python-urllib3 >= 1.26.2 with python-urllib3 < 2)
BuildArch:      noarch
%if 0%{python_version_nodots} < 37
Requires:       python-dataclasses
%endif
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module dataclasses if %python-base < 3.7}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module urllib3 >= 1.26.2 with %python-urllib3 < 2}
# /SECTION
%python_subpackages

%description
Transport classes and utilities shared among Python Elastic client libraries

%prep
%setup -q -n elastic-transport-python-%{version}
sed -i '/addopts/d' setup.cfg
sed -i 's/from mock/from unittest.mock/' tests/node/test_http_*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# these tests fail without proper name resolution or online connection to httpbin.org and badssl.com
donttest="(test_http_aiohttp and not TestAiohttpHttpNode)"
donttest="$donttest or test_tls_versions"
donttest="$donttest or test_assert_fingerprint_in_cert_chain"
# gh#elastic/elastic-transport-python#96
donttest="$donttest or test_url_to_node_config[https://[::1]:0/-https://[::1]:0-]"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/elastic_transport
%{python_sitelib}/elastic_transport-%{version}*-info

%changelog
