#
# spec file for package python-pytest-django
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
%bcond_without python2
Name:           python-pytest-django
Version:        3.9.0
Release:        0
Summary:        A Django plugin for py.test
License:        BSD-3-Clause
URL:            https://github.com/pytest-dev/pytest-django
Source:         https://files.pythonhosted.org/packages/source/p/pytest-django/pytest-django-%{version}.tar.gz
# fix tests
Patch0:         ignore-warnings.patch
# PATCH-FIX-UPSTREAM fix test failure with pytest 6, is part of https://github.com/pytest-dev/pytest-django/pull/855
Patch1:         https://github.com/pytest-dev/pytest-django/commit/3f03d0a7890e987086042b42db346e47398ffed3.patch#/pytest-django-pytest6.patch
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm >= 1.11.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sqlite3
Requires:       python-Django
Requires:       python-pytest
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-pathlib2
%endif
%ifpython2
Requires:       python-pathlib2
%endif
%python_subpackages

%description
pytest-django allows testing Django projects/applications with the
pytest testing tool.

Running the test suite with pytest-django allows tapping into the features
that are already present in pytest:

* Manage test dependencies with pytest fixtures.
* Less boilerplate tests: no need to import unittest and creating a
  subclass with methods. Tests can be written as regular functions.
* Database re-use: no need to re-create the test database for every test run.
* Run tests in multiple processes for increased speed (with the pytest-xdist plugin).
* Make use of other pytest plugins.
* Works with both worlds: Existing unittest-style TestCase's still work without any modifications.

%prep
%setup -q -n pytest-django-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# memory operations failed in OBS not localy, thus skip them
export DJANGO_SETTINGS_MODULE=pytest_django_test.settings_sqlite
export PYTHONPATH=$(pwd)
%pytest -v tests/ -k 'not (test_sqlite_in_memory_used or test_django_assert_num_queries_db or test_django_assert_max_num_queries_db)'

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst docs/*.rst
%{python_sitelib}/*

%changelog
