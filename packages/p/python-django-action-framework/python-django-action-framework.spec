#
# spec file for package python-django-action-framework
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
Name:           python-django-action-framework
Version:        1.4.0
Release:        0
Summary:        Easily create actions and various interfaces around them
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jyveapp/django-action-framework
Source:         https://files.pythonhosted.org/packages/source/d/django-action-framework/django-action-framework-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jyveapp/django-action-framework/master/settings.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2
Requires:       python-django-args >= 1.4.0
Requires:       python-djangorestframework >= 3.0.0
Requires:       python-python-args >= 1.0.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module dj-database-url}
BuildRequires:  %{python_module django-args >= 1.4.0}
BuildRequires:  %{python_module django-dynamic-fixture}
BuildRequires:  %{python_module django-extensions}
BuildRequires:  %{python_module djangorestframework >= 3.0.0}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module python-args >= 1.0.2}
# /SECTION
%python_subpackages

%description
Easily create actions and various interfaces around them.

%prep
%setup -q -n django-action-framework-%{version}
cp %{SOURCE1} .

echo 'DDF_DEFAULT_DATA_FIXTURE="sequential"' >> settings.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=settings
export DATABASE_URL=sqlite://./db.sqlite3
%pytest -k 'not test_atomicity'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
