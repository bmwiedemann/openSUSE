#
# spec file for package python-django-import-export
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


%{?sle15_python_module_pythons}
Name:           python-django-import-export
Version:        4.2.1
Release:        0
Summary:        Django data importing and exporting
License:        BSD-2-Clause
URL:            https://github.com/django-import-export/django-import-export
Source:         https://files.pythonhosted.org/packages/source/d/django-import-export/django_import_export-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Requires:       python-diff-match-patch
Requires:       python-tablib >= 3.7
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module diff-match-patch}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module tablib >= 3.7}
# /SECTION
%python_subpackages

%description
Django application and library for importing and exporting data with included admin integration.

%prep
%setup -q -n django_import_export-%{version}
# Fix postgres specific field
sed -i '/data_field/d' tests/core/migrations/0004_bookwithchapters.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}:${PWD}/tests/
export LANG=en_US.UTF-8
%python_exec tests/manage.py test core

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/import_export
%{python_sitelib}/django_import_export-%{version}.dist-info

%changelog
