#
# spec file for package python-django-cacheops
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-django-cacheops
Version:        7.2
Release:        0
Summary:        Django ORM cache with automatic granular event-driven invalidation
License:        BSD-3-Clause
URL:            http://github.com/Suor/django-cacheops
Source:         https://files.pythonhosted.org/packages/source/d/django_cacheops/django_cacheops-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 3.2
Requires:       python-funcy >= 1.8
Requires:       python-redis >= 3.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module before-after}
BuildRequires:  %{python_module dill}
BuildRequires:  %{python_module funcy >= 1.8}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module redis >= 3.0.0}
BuildRequires:  redis
# /SECTION
%python_subpackages

%description
A slick app that supports automatic or manual queryset caching and automatic
granular event-driven invalidation.

It uses `redis <http://redis.io/>`_ as backend for ORM cache and redis or
filesystem for simple time-invalidated one.

%prep
%autosetup -p1 -n django_cacheops-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
/usr/sbin/redis-server &
export DJANGO_SETTINGS_MODULE=tests.settings
%pytest

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/cacheops
%{python_sitelib}/django_cacheops-%{version}*-info

%changelog
