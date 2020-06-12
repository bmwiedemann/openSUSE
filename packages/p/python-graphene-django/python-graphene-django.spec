#
# spec file for package python-graphene-django
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
Name:           python-graphene-django
Version:        3.0.0b3
Release:        0
Summary:        Graphene Django integration
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/graphql-python/graphene-django
Source:         https://github.com/graphql-python/graphene-django/archive/v%{version}.tar.gz#/graphene-django-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module django-filter}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module graphene}
BuildRequires:  %{python_module graphql-core}
BuildRequires:  %{python_module graphql-relay}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  tree
Requires:       python-Django
Requires:       python-graphene
Requires:       python-graphql-core
Requires:       python-graphql-relay
Requires:       python-promise
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Graphene Django integration.

%prep
%setup -q -n graphene-django-%{version}
rm setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=django_test_settings
%pytest

%files %{python_files}
%doc README.rst README.md
%license LICENSE
%{python_sitelib}/*

%changelog
