#
# spec file for package python-django-polymorphic
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
Name:           python-django-polymorphic
Version:        3.0.0
Release:        0
Summary:        Polymorphic inheritance for Django models
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django-polymorphic/django-polymorphic
Source:         https://github.com/django-polymorphic/django-polymorphic/archive/%{version}.tar.gz#/django-polymorphic-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/django-polymorphic/django-polymorphic/master/runtests.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module dj-database-url}
# /SECTION
%python_subpackages

%description
Seamless polymorphic inheritance for Django models.

%prep
%setup -q -n django-polymorphic-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
