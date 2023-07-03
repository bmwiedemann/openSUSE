#
# spec file for package python-django-redis
#
# Copyright (c) 2023 SUSE LLC
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
Version:        5.3.0
Release:        0
Summary:        A redis cache backend for Django
License:        BSD-3-Clause
URL:            https://github.com/jazzband/django-redis
Source:         https://files.pythonhosted.org/packages/source/d/django-redis/django-redis-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module lz4 >= 0.15}
BuildRequires:  %{python_module msgpack >= 0.4.6}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest-mock >= 3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis >= 2.10.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-lz4 >= 0.15
Requires:       python-msgpack >= 0.4.6
Requires:       python-redis >= 2.10.0
BuildArch:      noarch
%python_subpackages

%description
A redis cache backend for Django.

%prep
%setup -q -n django-redis-%{version}
sed -i '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
/usr/sbin/redis-server --port 6379 &
export PYTHONPATH=${PWD}:${PWD}/tests
%{python_expand \
DJANGO_SETTINGS_MODULE=tests.settings.sqlite_sharding $python -m pytest -rs -v tests
DJANGO_SETTINGS_MODULE=tests.settings.sqlite_herd $python -m pytest -rs -v tests
DJANGO_SETTINGS_MODULE=tests.settings.sqlite_json $python -m pytest -rs -v tests
DJANGO_SETTINGS_MODULE=tests.settings.sqlite_msgpack $python -m pytest -rs -v tests
DJANGO_SETTINGS_MODULE=tests.settings.sqlite_zlib $python -m pytest -rs -v tests
DJANGO_SETTINGS_MODULE=tests.settings.sqlite_lz4 $python -m pytest -rs -v tests
}
killall redis-server

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/django[-_]redis*/

%changelog
