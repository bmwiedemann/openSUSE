#
# spec file for package python-django-cacheops
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
Name:           python-django-cacheops
Version:        5.0.1
Release:        0
Summary:        Django ORM cache with automatic granular event-driven invalidation
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/Suor/django-cacheops
Source:         https://github.com/Suor/django-cacheops/archive/%{version}.tar.gz#/django-cacheops-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Requires:       python-django >= 1.8
Requires:       python-funcy >= 1.8
Requires:       python-redis >= 2.9.1
Requires:       python-six >= 1.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module before-after}
BuildRequires:  %{python_module django >= 1.8}
BuildRequires:  %{python_module funcy >= 1.8}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module redis >= 2.9.1}
BuildRequires:  %{python_module six >= 1.4.0}
BuildRequires:  redis
# /SECTION
%python_subpackages

%description
A slick app that supports automatic or manual queryset caching and automatic
granular event-driven invalidation.

It uses `redis <http://redis.io/>`_ as backend for ORM cache and redis or
filesystem for simple time-invalidated one.

%prep
%setup -q -n django-cacheops-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
/usr/sbin/redis-server &
export DJANGO_SETTINGS_MODULE=tests.settings
%pytest

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
