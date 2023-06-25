#
# spec file for package python-django-timezone-field
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-django-timezone-field
Version:        5.1
Release:        0
Summary:        Django app providing database and form fields for pytz timezone objects
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mfogel/django-timezone-field/
Source:         https://github.com/mfogel/django-timezone-field/archive/%{version}.tar.gz#/django-timezone-field-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest-lazy-fixture}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
# /SECTION
%python_subpackages

%description
A Django app providing database and form fields for pytz timezone objects.

%prep
%setup -q -n django-timezone-field-%{version}
sed -Ei 's/_(TZChoicesDisplayModel|ZIChoicesDisplayModel)/\1/g' tests/test_choices_display_option.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=tests.settings
export TEST_DB_ENGINE=sqlite
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/timezone_field
%{python_sitelib}/django[-_]timezone[-_]field*/

%changelog
