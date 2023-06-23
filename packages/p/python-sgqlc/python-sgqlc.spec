#
# spec file for package python-sgqlc
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-sgqlc
Version:        16.3
Release:        0
Summary:        Simple GraphQL Client
License:        ISC
URL:            http://github.com/profusion/sgqlc
Source:         https://files.pythonhosted.org/packages/source/s/sgqlc/sgqlc-%{version}.tar.gz
# PATCH-FIX-OPENSUSE No coverage options in pyproject.toml
Patch0:         no-coverage.patch
BuildRequires:  %{python_module graphql-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module websocket-client}
BuildRequires:  python-rpm-macros
Requires:       python-graphql-core
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-requests
Recommends:     python-websocket-client
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
This package offers an easy to use GraphQL client. GraphQL is a query
language for APIs and a runtime for fulfilling those queries with your
existing data.

%prep
%autosetup -p1 -n sgqlc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sgqlc-codegen
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative sgqlc-codegen

%postun
%python_uninstall_alternative sgqlc-codegen

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%python_alternative %{_bindir}/sgqlc-codegen
%{python_sitelib}/sgqlc
%{python_sitelib}/sgqlc-%{version}.dist-info

%changelog
