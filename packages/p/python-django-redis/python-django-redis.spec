#
# spec file for package python-django-redis
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-django-redis
Version:        6.0.0
Release:        0
Summary:        A redis cache backend for Django
License:        BSD-3-Clause
URL:            https://github.com/jazzband/django-redis
Source:         https://files.pythonhosted.org/packages/source/d/django_redis/django_redis-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module lz4 >= 0.15}
BuildRequires:  %{python_module msgpack >= 0.6.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock >= 3.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis >= 4.0.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
BuildRequires:  redis
Requires:       python-Django >= 4.2
Requires:       python-redis >= 4.0.2
BuildArch:      noarch
%python_subpackages

%description
A redis cache backend for Django.

%prep
%setup -q -n django_redis-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
/usr/sbin/redis-server --port 6379 &
export PYTHONPATH=${PWD}:${PWD}/tests
%pytest -rs -n auto tests
killall redis-server

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/django_redis
%{python_sitelib}/django_redis-%{version}.dist-info

%changelog
