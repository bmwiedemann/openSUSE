#
# spec file for package python-graphql-relay
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
Name:           python-graphql-relay
Version:        3.2.0
Release:        0
Summary:        Relay implementation for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/graphql-python/graphql-relay-py
Source:         https://files.pythonhosted.org/packages/source/g/graphql-relay/graphql-relay-%{version}.tar.gz
BuildRequires:  %{python_module graphql-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module promise}
BuildRequires:  %{python_module pytest >= 6.2}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-describe}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-promise
Requires:       (python-graphql-core >= 3.2)
BuildArch:      noarch
%python_subpackages

%description
Relay Library for GraphQL Python.

This is a library to allow the easy creation of Relay-compliant servers using
the GraphQL Python reference implementation of a GraphQL server.

%prep
%setup -q -n graphql-relay-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/graphql[-_]relay*/

%changelog
