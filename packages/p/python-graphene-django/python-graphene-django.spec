#
# spec file for package python-graphene-django
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
Name:           python-graphene-django
Version:        3.0.0b7
Release:        0
Summary:        Graphene Django integration
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/graphql-python/graphene-django
Source:         https://github.com/graphql-python/graphene-django/archive/v%{version}.tar.gz#/graphene-django-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module django-filter >= 2}
BuildRequires:  %{python_module djangorestframework >= 3.6.3}
BuildRequires:  %{python_module graphene >= 3.0.0b5}
BuildRequires:  %{python_module graphql-core >= 3.1.0}
BuildRequires:  %{python_module graphql-relay}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module promise >= 2.1}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytest-django >= 3.3.2}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module text-unidecode}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  tree
Requires:       python-Django >= 2.2
Requires:       python-graphene >= 3.0.0b5
Requires:       python-graphql-core >= 3.1.0
Requires:       python-graphql-relay
Requires:       python-promise >= 2.1
Requires:       python-six
Requires:       python-text-unidecode
Suggests:       python-django-filter >= 2
Suggests:       python-djangorestframework >= 3.6.3
BuildArch:      noarch
%python_subpackages

%description
Graphene Django integration.

%prep
%setup -q -n graphene-django-%{version}
rm setup.cfg
sed -i '/pytest-runner/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=examples.django_test_settings
%pytest

%files %{python_files}
%doc README.rst README.md
%license LICENSE
%{python_sitelib}/*

%changelog
