#
# spec file for package python-graphql-core
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-graphql-core
Version:        3.1.1
Release:        0
Summary:        GraphQL implementation for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/graphql-python/graphql-core
Source:         https://files.pythonhosted.org/packages/source/g/graphql-core/graphql-core-%{version}.tar.gz
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-benchmark >= 3.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Conflicts:      python-graphql
BuildArch:      noarch
%python_subpackages

%description
GraphQL implementation for Python, a port of GraphQL.js,
the JavaScript reference implementation for GraphQL.

%prep
%setup -q -n graphql-core-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
