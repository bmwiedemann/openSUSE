#
# spec file for package python-gql
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


Name:           python-gql
Version:        3.5.2
Release:        0
Summary:        GraphQL client for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://gql.readthedocs.io
Source:         https://github.com/graphql-python/gql/archive/refs/tags/v%{version}.tar.gz#/gql-%{version}.tar.gz
Patch0:         fix-tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aiofiles}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module backoff >= 1.10.0}
BuildRequires:  %{python_module botocore}
BuildRequires:  %{python_module flake8-import-order}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module graphql-core >= 3.2 with %python-graphql-core < 3.4}
BuildRequires:  %{python_module httpx}
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
BuildRequires:  %{python_module yarl}
# /SECTION
Requires:       python-anyio
Requires:       python-backoff >= 1.11.1
Requires:       (python-graphql-core >= 3.2 with python-graphql-core < 3.4)
Requires:       python-yarl >= 1.6
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
GraphQL client for Python.

%prep
%setup -q -n gql-%{version}
%autopatch -p1

# remove not needed gql-checker subproject
rm -Rf gql-checker

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/gql-cli

%check
# skip some non-functional tests
%pytest -k "not (test_aiohttp_using_cli_ep or test_cli_ep_version or test_httpx_using_cli_ep or test_async_client_validation)"

%files %{python_files}

%post
%python_install_alternative gql-cli

%postun
%python_uninstall_alternative gql-cli

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/gql-cli
%{python_sitelib}/gql
%{python_sitelib}/gql-%{version}*-py*.egg-info

%changelog
