#
# spec file for package python-pytest-django
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-pytest-django
Version:        4.5.2
Release:        0
Summary:        A Django plugin for Pytest
License:        BSD-3-Clause
URL:            https://github.com/pytest-dev/pytest-django
Source:         https://files.pythonhosted.org/packages/source/p/pytest-django/pytest-django-%{version}.tar.gz
# PATCH-FIX-UPSTREAM autoclear_mailbox.patch gh#pytest-dev/pytest-django#993 mcepl@suse.com
# Protect against non-existant mail.outbox folder
# https://stackoverflow.com/q/5424498/164233
Patch0:         autoclear_mailbox.patch
# PATCH-FIX-UPSTREAM pytest-django-pr996-pytest7.patch -- gh#pytest-dev/pytest-django#996
Patch1:         https://github.com/pytest-dev/pytest-django/pull/996.patch#/pytest-django-pr996-pytest7.patch
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest > 5.4.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module setuptools_scm >= 5.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sqlite3
Requires:       python-Django
Requires:       python-pytest > 5.4.0
BuildArch:      noarch
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
%autosetup -p1 -n pytest-django-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# memory operations fail in OBS server-side, thus skip them
export DJANGO_SETTINGS_MODULE=pytest_django_test.settings_sqlite
export PYTHONPATH=$(pwd)
%pytest -v tests/ -k 'not (test_sqlite_in_memory_used or test_django_assert_num_queries_db or test_django_assert_max_num_queries_db)'

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst docs/*.rst
%{python_sitelib}/pytest_django
%{python_sitelib}/pytest_django-%{version}*-info

%changelog
