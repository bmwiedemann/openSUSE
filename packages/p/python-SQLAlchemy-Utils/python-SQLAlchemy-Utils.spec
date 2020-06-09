#
# spec file for package python-SQLAlchemy-Utils
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
Name:           python-SQLAlchemy-Utils
Version:        0.36.6
Release:        0
Summary:        Various utility functions for SQLAlchemy
License:        BSD-3-Clause
URL:            https://github.com/kvesteri/sqlalchemy-utils
Source:         https://files.pythonhosted.org/packages/source/S/SQLAlchemy-Utils/SQLAlchemy-Utils-%{version}.tar.gz
BuildRequires:  %{python_module Babel >= 1.3}
BuildRequires:  %{python_module Jinja2 >= 2.3}
BuildRequires:  %{python_module Pygments >= 1.2}
BuildRequires:  %{python_module SQLAlchemy >= 1.0}
BuildRequires:  %{python_module anyjson >= 0.3.3}
BuildRequires:  %{python_module arrow >= 0.3.4}
BuildRequires:  %{python_module colour >= 0.0.4}
BuildRequires:  %{python_module cryptography >= 0.6}
BuildRequires:  %{python_module docutils >= 0.10}
BuildRequires:  %{python_module flexmock >= 0.9.7}
BuildRequires:  %{python_module furl >= 0.4.1}
BuildRequires:  %{python_module intervals >= 0.7.1}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module passlib >= 1.6}
BuildRequires:  %{python_module pendulum >= 2.0.5}
BuildRequires:  %{python_module phonenumbers >= 5.9.2}
BuildRequires:  %{python_module psycopg2 >= 2.5.1}
BuildRequires:  %{python_module psycopg2cffi >= 2.8.1}
BuildRequires:  %{python_module pyodbc}
BuildRequires:  %{python_module pytest >= 2.7.1}
BuildRequires:  %{python_module python-dateutil >= 2.6}
BuildRequires:  %{python_module pytz >= 2014.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy >= 1.0
Requires:       python-six
Recommends:     python-Babel >= 1.3
Recommends:     python-anyjson >= 0.3.3
Recommends:     python-arrow >= 0.3.4
Recommends:     python-colour >= 0.0.4
Recommends:     python-cryptography >= 0.6
Recommends:     python-dateutil
Recommends:     python-furl >= 0.4.1
Recommends:     python-intervals >= 0.7.1
Recommends:     python-passlib >= 1.6
Recommends:     python-pendulum >= 2.0.5
Recommends:     python-phonenumbers >= 5.9.2
BuildArch:      noarch
%python_subpackages

%description
Various utility functions and custom data types for SQLAlchemy.

%prep
%setup -q -n SQLAlchemy-Utils-%{version}

%build
%python_build

%install
%python_install
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
%pytest -k 'not (TestDatabasePostgres or TestDatabaseMssql or OnPostgres or OnMysql or TestPostgres or TestMysql or TestSortQueryRelationshipCounts or TestSortQueryWithPolymorphicInheritance or TestMaterializedViews or TestLazyEvaluatedSelectExpressionsForAggregates or TestAggregatesWithManyToManyRelationships or TestAggregateManyToManyAndManyToMany or TestAggregateOneToManyAndOneToMany or TestJSONSQL or TestJSONBSQL or TestSortQueryWithCustomPolymorphic or TestAggregateOneToManyAndManyToMany or test_timezone)'

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitelib}/sqlalchemy_utils
%{python_sitelib}/sqlalchemy_utils/*
%{python_sitelib}/SQLAlchemy_Utils-%{version}-py*.egg-info

%changelog
