#
# spec file for package python-django-braces
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
Name:           python-django-braces
Version:        1.14.0
Release:        0
Summary:        Reusable, generic mixins for Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/brack3t/django-braces/
Source:         https://files.pythonhosted.org/packages/source/d/django-braces/django-braces-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/brack3t/django-braces/pull/265 feat: remove support for python 2.7 and add support for Django 3.1
Patch0:         remove-py2-add-django3.patch
Patch1:         testhack.patch
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
Reusable, generic mixins for Django.

%prep
%setup -q -n django-braces-%{version}
%autopatch -p1
# do not mess with the test setup and rely on pytest defaults
rm tox.ini
rm conftest.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
PYTHONPATH=.
%pytest --nomigrations

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
