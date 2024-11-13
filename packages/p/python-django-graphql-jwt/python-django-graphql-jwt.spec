#
# spec file for package python-django-graphql-jwt
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


Name:           python-django-graphql-jwt
Version:        0.4.0
Release:        0
Summary:        JSON Web Token for Django GraphQL
License:        MIT
URL:            https://github.com/flavors/django-graphql-jwt
Source:         https://github.com/flavors/django-graphql-jwt/archive/refs/tags/%{version}.tar.gz#/django-graphql-jwt-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module PyJWT >= 2}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module graphene >= 2.1}
BuildRequires:  %{python_module graphene-django >= 2.0}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.0
Requires:       python-PyJWT >= 2
Requires:       python-graphene >= 2.1
Requires:       python-graphene-django >= 2.0
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
JSON Web Token for Django GraphQL

%prep
%autosetup -p1 -n django-graphql-jwt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
PYTHONPATH=.
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/graphql_jwt
%{python_sitelib}/django_graphql_jwt-%{version}.dist-info

%changelog
