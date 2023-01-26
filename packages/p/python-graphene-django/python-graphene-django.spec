#
# spec file for package python-graphene-django
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-graphene-django
Version:        3.0.0
Release:        0
Summary:        Graphene Django integration
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/graphql-python/graphene-django
Source:         https://github.com/graphql-python/graphene-django/archive/v%{version}.tar.gz#/graphene-django-%{version}.tar.gz
# https://github.com/graphql-python/graphene-django/issues/1321
Patch0:         python-graphene-django-no-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  tree
Requires:       python-Django >= 3.2
Requires:       python-graphene >= 2.9.9
Requires:       python-graphql-core >= 3.1.0
Requires:       python-graphql-relay
Requires:       python-promise >= 2.1
Requires:       python-six
Requires:       python-text-unidecode
Suggests:       python-django-filter >= 2
Suggests:       python-djangorestframework >= 3.6.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module django-filter >= 2}
BuildRequires:  %{python_module djangorestframework >= 3.6.3}
BuildRequires:  %{python_module graphene >= 2.9.9}
BuildRequires:  %{python_module graphql-core >= 3.1.0}
BuildRequires:  %{python_module graphql-relay}
BuildRequires:  %{python_module promise >= 2.1}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-django >= 3.3.2}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module text-unidecode}
# /SECTION
%python_subpackages

%description
Graphene Django integration.

%prep
%setup -q -n graphene-django-%{version}
%patch0 -p1
sed -i 's/from mock import MagicMock/from unittest.mock import MagicMock/' graphene_django/filter/tests/conftest.py

sed -i 's/py\.test/pytest/g' graphene_django/tests/*.py graphene_django/tests/issues/*.py graphene_django/*/tests/*.py

rm setup.cfg
sed -i '/pytest-runner/d' setup.py

%build
%python_build

%install
%python_install
%python_expand find %{buildroot}%{$python_sitelib}/graphene_django -name tests | xargs rm -r
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=examples.django_test_settings

# The following started failing in 4.1 with b8
skips="test_integer_field_filter_type or test_other_filter_types or test_generate_graphql_file_on_call_graphql_schema or test_schema_representation"
skips="$skips or test_django_objecttype_convert_choices_enum or test_django_objecttype_choices_custom_enum_name"
skips="$skips or test_reports_validation_errors or test_errors_when_missing_operation_name or test_handles_syntax_errors_caught_by_graphql"

%pytest -k "not ($skips)"

%files %{python_files}
%doc README.rst README.md
%license LICENSE
%{python_sitelib}/graphene[_-]django*/

%changelog
