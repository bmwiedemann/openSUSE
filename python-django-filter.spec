#
# spec file for package python-django-filter
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
Name:           python-django-filter
Version:        2.3.0
Release:        0
Summary:        Reusable Django app to allow users to filter queryset dynamically
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/carltongibson/django-filter
Source:         https://files.pythonhosted.org/packages/source/d/django-filter/django-filter-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module django-crispy-forms}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-djangorestframework
Recommends:     python-django-crispy-forms
BuildArch:      noarch
%python_subpackages

%description
Django-filter is a reusable Django application for allowing users to filter queryset dynamically. It
requires Python 2.7 or higher. For usage and installation instructions, consult the docs directory.

%prep
%setup -q -n django-filter-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py -v 2 

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES.rst README.rst docs/{*.txt,ref/*.txt}
%{python_sitelib}/*

%changelog
