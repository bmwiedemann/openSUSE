#
# spec file for package python-django-jinja
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
%bcond_without python2
Name:           python-django-jinja
Version:        2.6.0
Release:        0
Summary:        Jinja2 templating language integrated in Django
License:        BSD-3-Clause
URL:            https://github.com/niwinz/django-jinja
Source:         https://github.com/niwinz/django-jinja/archive/%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Jinja2 >= 2.5}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-mock
%endif
Requires:       python-Django >= 1.11
Requires:       python-Jinja2 >= 2.5
BuildArch:      noarch
%python_subpackages

%description
Simple and nonobstructive jinja2 integration with Django.

%prep
%setup -q -n django-jinja-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests require old pipeline package, while upstream does not support it
# anymore and it is hardwired so we can't just run the tests without it...
#%%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" $python testing/runtests.py

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES.adoc
%{python_sitelib}/*

%changelog
