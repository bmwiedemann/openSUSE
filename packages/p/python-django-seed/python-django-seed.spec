#
# spec file for package python-django-seed
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
Name:           python-django-seed
Version:        0.3.1
Release:        0
Summary:        Django project fake data seeder
License:        MIT
URL:            https://github.com/brobin/django-seed
Source0:        https://github.com/brobin/django-seed/archive/refs/tags/%{version}.tar.gz#/django-seed-%{version}.tar.gz
Source1:        settings.py
# PATCH-FIX-UPSTREAM gh#Brobin/django-seed#120
Patch0:         do-not-use-is-dst.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-Faker
Requires:       python-toposort
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module django-jsonfield}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toposort}
# /SECTION
%python_subpackages

%description
A module to seed Django projects with fake data.

%prep
%autosetup -p1 -n django-seed-%{version}
sed -i 's/fake-factory/Faker/' setup.py
cp %SOURCE1 django_seed

sed -i '/alphabet_detector/d' django_seed/tests.py
sed -i 's/assertEquals/assertEqual/g' django_seed/tests.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=django_seed.settings
%pytest -k "not (test_locale or test_auto_now)" %{buildroot}%{$python_sitelib}/django_seed/tests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/django_seed
%{python_sitelib}/django_seed-%{version}.dist-info

%changelog
