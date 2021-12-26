#
# spec file for package python-django-sortedm2m
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
Name:           python-django-sortedm2m
Version:        3.1.1
Release:        0
Summary:        Drop-in replacement for django's many to many field with sorted relations
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/django-sortedm2m
Source:         https://files.pythonhosted.org/packages/source/d/django-sortedm2m/django-sortedm2m-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
Drop-in replacement for Django's many to many field with sorted relations.

%prep
%setup -q -n django-sortedm2m-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=test_project.settings
export DB_ENGINE=sqlite3 DB_NAME=":memory:"
%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*sortedm2m*/

%changelog
