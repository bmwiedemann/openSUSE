#
# spec file for package python-graphene
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-graphene
Version:        3.4.3
Release:        0
Summary:        GraphQL Framework for Python
License:        MIT
URL:            https://github.com/graphql-python/graphene
Source:         https://github.com/graphql-python/graphene/archive/v%{version}.tar.gz#/graphene-%{version}.tar.gz
BuildRequires:  %{python_module graphql-core >= 3.1}
BuildRequires:  %{python_module graphql-relay >= 3.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module promise}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.7}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 4.7.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-graphql-core >= 3.1
Requires:       python-graphql-relay >= 3.1
Requires:       python-python-dateutil >= 2.7
Requires:       python-typing-extensions >= 4.7.1
BuildArch:      noarch
%python_subpackages

%description
Graphene is a Python library for building GraphQL schemas/types.

%prep
%autosetup -p1 -n graphene-%{version}

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
%{python_sitelib}/graphene
%{python_sitelib}/graphene-%{version}.dist-info

%changelog
