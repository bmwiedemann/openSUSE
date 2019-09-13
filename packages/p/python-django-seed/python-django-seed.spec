#
# spec file for package python-django-seed
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.1.9
Release:        0
Summary:        Django project fake data seeder
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/brobin/django-seed
Source:         https://files.pythonhosted.org/packages/source/d/django-seed/django-seed-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Brobin/django-seed/master/runtests.py
Source2:        https://raw.githubusercontent.com/Brobin/django-seed/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Faker >= 0.7.7}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module django-nose}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 1.11
Requires:       python-Faker >= 0.7.7
BuildArch:      noarch

%python_subpackages

%description
A module to seed Django projects with fake data.

%prep
%setup -q -n django-seed-%{version}
sed -i 's/fake-factory/Faker/' setup.py
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
