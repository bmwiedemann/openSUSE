#
# spec file for package python-django-tables2
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
Name:           python-django-tables2
Version:        2.7.0
Release:        0
Summary:        Table/data-grid framework for Django
License:        BSD-2-Clause
URL:            https://github.com/jieter/django-tables2/
Source:         https://github.com/jieter/django-tables2/archive/v%{version}.tar.gz#/django-tables2-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE python-django-tables2-tests-noxls.patch -- Disable XLS export tests
Patch0:         python-django-tables2-tests-noxls.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Suggests:       python-tablib
BuildArch:      noarch
# SECTION test requirements, see requirements/common.pip
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module django-filter >= 2.3.0}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module tablib}
# /SECTION
%python_subpackages

%description
Simplifies the task of turning sets of data into HTML tables. It has native
support for pagination and sorting. It does for HTML tables what django.forms
does for HTML forms.

%prep
%autosetup -p1 -n django-tables2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_find_lang django

%check
%python_exec ./manage.py test -v 2

%files %{python_files} -f %{python_prefix}-django.lang
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/django_tables2
%{python_sitelib}/django_tables2-%{version}.dist-info

%changelog
