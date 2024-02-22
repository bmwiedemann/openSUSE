#
# spec file for package python-django-reversion
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


Name:           python-django-reversion
Version:        5.0.12
Release:        0
Summary:        A Django extension that provides version control for model instances
License:        BSD-3-Clause
URL:            https://github.com/etianen/django-reversion
Source:         https://files.pythonhosted.org/packages/source/d/django-reversion/django-reversion-%{version}.tar.gz
Patch0:         only-sqlite-test-db.patch
BuildRequires:  %{python_module Django > 2.0}
BuildRequires:  %{python_module base > 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django > 2.0
Obsoletes:      python-django-reversion-doc
Obsoletes:      python-django-reversion-lang
BuildArch:      noarch
%python_subpackages

%description
Django-reversion is an extension to the Django web framework that provides
version control for model instances.

-  Roll back to any point in a model instance's history.
-  Recover deleted model instances.
-  Simple admin integration.

%prep
# Tests need running PGSQL and MYSQL
# https://github.com/etianen/django-reversion/issues/902
%autosetup -p1 -n django-reversion-%{version}
sed -i 's/databases = {"default", .*"postgres"}/databases = {"default"}/' tests/test_app/tests/test_*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd tests
export DJANGO_SETTINGS_MODULE=test_project.settings
%pytest -k 'not (testAddMetaMultDb or MultiDb or MySQL or MySql or Postgres or testCreateInitialRevisionsDb or testCreateInitialRevisionsModelDb or testDeleteRevisionsDb or testGetForModelDb or testGetForObjectDb or testGetForObjectModelDb or testGetForObjectReferenceModelDb or testGetDeletedDb or testGetDeletedModelDb or testDeleteRevisionsModelDb)'

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE
%{python_sitelib}/reversion
%{python_sitelib}/django_reversion-%{version}.dist-info

%changelog
