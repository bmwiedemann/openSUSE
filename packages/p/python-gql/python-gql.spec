#
# spec file for package python-gql
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-gql
Version:        4.0.0
Release:        0
Summary:        GraphQL client for Python
License:        MIT
URL:            https://gql.readthedocs.io
Source:         https://github.com/graphql-python/gql/archive/refs/tags/v%{version}.tar.gz#/gql-%{version}.tar.gz
# PATCH-FIX-UPSTEAM tests.patch gh#graphql-python/gql@3b2c396
Patch0:         tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  ca-certificates
BuildRequires:  %{python_module aiofiles}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module anyio >= 3.0 with %python-anyio  < 5}
BuildRequires:  %{python_module backoff >= 1.10.1 with %python-backoff < 3.0}
BuildRequires:  %{python_module botocore}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module flake8-import-order}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module graphql-core >= 3.2 with %python-graphql-core < 3.3}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module parse}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-vcr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module websockets}
BuildRequires:  %{python_module yarl >= 1.6 with %python-yarl < 2}
BuildRequires:  ca-certificates-mozilla
# /SECTION
Requires:       alts
Requires:       (python-anyio >= 3.0 with python-anyio < 5)
Requires:       (python-backoff >= 1.11.1 with python-backoff < 3.0)
Requires:       (python-graphql-core >= 3.2 with python-graphql-core < 3.3)
Requires:       (python-yarl >= 1.6 with python-yarl < 2)
BuildArch:      noarch
%python_subpackages

%description
GraphQL client for Python.

%prep
%autosetup -p1 -n gql-%{version}

# remove not needed gql-checker subproject
rm -Rf gql-checker

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/gql-cli

%check
# skip some non-functional tests
IGNORED_CHECKS='test_aiohttp_using_cli_ep'
IGNORED_CHECKS+=' or test_cli_ep_version'
IGNORED_CHECKS+=' or test_httpx_using_cli_ep'
IGNORED_CHECKS+=' or test_async_client_validation'

%pytest -k "not (network or ${IGNORED_CHECKS})"

%pre
%python_libalternatives_reset_alternative gql-cli

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/gql-cli
%{python_sitelib}/gql
%{python_sitelib}/gql-%{version}.dist-info

%changelog
