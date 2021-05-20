#
# spec file for package python-django-import-export
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python36 1
Name:           python-django-import-export
Version:        2.5.0
Release:        0
Summary:        Django data importing and exporting
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django-import-export/django-import-export
Source:         https://github.com/django-import-export/django-import-export/archive/%{version}.tar.gz#/django-import-export-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.0
Requires:       python-diff-match-patch
Requires:       python-tablib >= 0.14.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module diff-match-patch}
BuildRequires:  %{python_module tablib >= 0.14.0}
# /SECTION
%python_subpackages

%description
Django application and library for importing and exporting data with included admin integration.

%prep
%setup -q -n django-import-export-%{version}
# Fix postgres specific field
sed -i '/data_field/d' tests/core/migrations/0004_bookwithchapters.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}:${PWD}/tests/
export LANG=en_US.UTF-8
%python_exec -m django test core -v2 --settings=settings

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
