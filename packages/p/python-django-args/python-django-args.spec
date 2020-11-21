#
# spec file for package python-django-args
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-django-args
Version:        1.4.0
Release:        0
Summary:        Django wrappers for python-args functions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jyveapp/django-args
Source:         https://files.pythonhosted.org/packages/source/d/django-args/django-args-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jyveapp/django-args/master/settings.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2
Requires:       python-django-formtools >= 2.2
Requires:       python-python-args >= 1.0.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2}
BuildRequires:  %{python_module dj-database-url}
BuildRequires:  %{python_module django-dynamic-fixture}
BuildRequires:  %{python_module django-formtools >= 2.2}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module python-args >= 1.0.2}
# /SECTION
%python_subpackages

%description
Django wrappers for python-args functions.

%prep
%setup -q -n django-args-%{version}
cp %{SOURCE1} .

echo 'DDF_DEFAULT_DATA_FIXTURE="sequential"' >> settings.py
cat settings.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=settings
export DATABASE_URL=sqlite://./db.sqlite3
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
