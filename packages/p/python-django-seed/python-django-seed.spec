#
# spec file for package python-django-seed
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
Name:           python-django-seed
Version:        0.2.2
Release:        0
Summary:        Django project fake data seeder
License:        MIT
URL:            https://github.com/brobin/django-seed
Source0:        https://files.pythonhosted.org/packages/source/d/django-seed/django-seed-%{version}.tar.gz
Source1:        settings.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-Faker >= 0.7.7
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Faker >= 0.7.7}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A module to seed Django projects with fake data.

%prep
%setup -q -n django-seed-%{version}
sed -i 's/fake-factory/Faker/' setup.py
cp %SOURCE1 django_seed

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=django_seed.settings
%pytest %{buildroot}%{$python_sitelib}/django_seed/tests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
