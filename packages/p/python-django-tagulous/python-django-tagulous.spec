#
# spec file for package python-django-tagulous
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


Name:           python-django-tagulous
Version:        2.1.0
Release:        0
License:        BSD-3-Clause
Summary:        Fabulous Tagging for Django
URL:            http://radiac.net/projects/django-tagulous/
Group:          Development/Languages/Python
Source:         https://github.com/radiac/django-tagulous/archive/refs/tags/v%{version}.tar.gz#/django-tagulous-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/radiac/django-tagulous/pull/188 Fix issue with serializers monkeypatching in Django 5.2b1
Patch:          django52b1.patch
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Suggests:       python-jasmine
Suggests:       python-psycopg2
Suggests:       python-mysqlclient
Suggests:       python-unidecode
BuildArch:      noarch

%python_subpackages

%description
Fabulous Tagging for Django.

%prep
%autosetup -p1 -n django-tagulous-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
# two of test_dump_load tests fail with Django 5.2 https://github.com/radiac/django-tagulous/issues/187
%pytest -k "not test_dump_load"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/tagulous/
%{python_sitelib}/django_tagulous-%{version}*info/

%changelog
