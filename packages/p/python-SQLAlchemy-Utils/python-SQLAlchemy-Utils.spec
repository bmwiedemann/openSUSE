#
# spec file for package python-SQLAlchemy-Utils
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
Name:           python-SQLAlchemy-Utils
Version:        0.41.2
Release:        0
Summary:        Various utility functions for SQLAlchemy
License:        BSD-3-Clause
URL:            https://github.com/kvesteri/sqlalchemy-utils
Source:         https://files.pythonhosted.org/packages/source/S/SQLAlchemy-Utils/SQLAlchemy-Utils-%{version}.tar.gz
BuildRequires:  %{python_module Babel >= 1.3}
BuildRequires:  %{python_module Jinja2 >= 2.3}
BuildRequires:  %{python_module Pygments >= 1.2}
BuildRequires:  %{python_module SQLAlchemy >= 1.0}
BuildRequires:  %{python_module arrow >= 0.3.4}
BuildRequires:  %{python_module backports.zoneinfo if %python-base < 3.9}
BuildRequires:  %{python_module colour >= 0.0.4}
BuildRequires:  %{python_module cryptography >= 0.6}
BuildRequires:  %{python_module docutils >= 0.10}
BuildRequires:  %{python_module flexmock >= 0.9.7}
BuildRequires:  %{python_module furl >= 0.4.1}
BuildRequires:  %{python_module intervals >= 0.7.1}
BuildRequires:  %{python_module passlib >= 1.6}
BuildRequires:  %{python_module pendulum >= 2.0.5 if %python-base < 3.13}
BuildRequires:  %{python_module phonenumbers >= 5.9.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psycopg2 >= 2.5.1}
BuildRequires:  %{python_module psycopg2cffi >= 2.8.1}
BuildRequires:  %{python_module pyodbc}
BuildRequires:  %{python_module pytest >= 2.7.1}
BuildRequires:  %{python_module python-dateutil >= 2.6}
BuildRequires:  %{python_module pytz >= 2014.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy >= 1.0
Recommends:     python-Babel >= 1.3
Recommends:     python-arrow >= 0.3.4
Recommends:     python-colour >= 0.0.4
Recommends:     python-cryptography >= 0.6
Recommends:     python-dateutil
Recommends:     python-furl >= 0.4.1
Recommends:     python-intervals >= 0.7.1
Recommends:     python-passlib >= 1.6
Recommends:     python-phonenumbers >= 5.9.2
Suggests:       python-pendulum >= 2.0.5
BuildArch:      noarch
%if 0%{?python_version_nodots} < 39
Requires:       python-backports.zoneinfo
%endif
%python_subpackages

%description
Various utility functions and custom data types for SQLAlchemy.

%prep
%autosetup -p1 -n SQLAlchemy-Utils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# needs running pgsql / mssql / mysql
rm tests/test_asserts.py
rm tests/test_translation_hybrid.py
rm tests/aggregate/test_o2m_o2m_o2m.py
rm tests/aggregate/test_search_vectors.py
rm tests/aggregate/test_with_ondelete_cascade.py
rm tests/observes/test_column_property.py
rm tests/observes/test_m2m_m2m_m2m.py
rm tests/observes/test_o2m_o2o_o2m.py
rm tests/observes/test_o2m_o2m_o2m.py
rm tests/observes/test_o2o_o2o.py
rm tests/observes/test_o2o_o2o_o2o.py
rm tests/relationships/test_select_correlated_expression.py
rm tests/types/test_composite.py
rm tests/types/test_ltree.py
rm tests/types/test_tsvector.py
rm tests/types/test_uuid.py
%pytest -rs -k 'not (TestDatabasePostgres or TestDatabaseMssql or OnPostgres or OnMysql or TestPostgres or TestMysql or TestSortQueryRelationshipCounts or TestSortQueryWithPolymorphicInheritance or TestMaterializedViews or TestLazyEvaluatedSelectExpressionsForAggregates or TestAggregatesWithManyToManyRelationships or TestAggregateManyToManyAndManyToMany or TestAggregateOneToManyAndOneToMany or TestJSONSQL or TestJSONBSQL or TestSortQueryWithCustomPolymorphic or TestAggregateOneToManyAndManyToMany or test_timezone or test_add_observed_object or test_render_mock_ddl)'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/sqlalchemy_utils
%{python_sitelib}/SQLAlchemy_Utils-%{version}.dist-info

%changelog
