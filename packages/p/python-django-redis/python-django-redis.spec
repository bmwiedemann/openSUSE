#
# spec file for package python-django-redis
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-django-redis
Version:        4.10.0
Release:        0
Summary:        A redis cache backend for Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/niwibe/django-redis
Source:         https://files.pythonhosted.org/packages/source/d/django-redis/django-redis-%{version}.tar.gz
# Fix tests to be compatible with Python 3 url parser.
Patch0:         tests-fix-urls.patch
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module lz4 >= 0.15}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module msgpack >= 0.4.6}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module redis >= 2.10.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-lz4 >= 0.15
Requires:       python-msgpack >= 0.4.6
Requires:       python-redis >= 2.10.0
BuildArch:      noarch
%python_subpackages

%description
A redis cache backend for Django.

%prep
%setup -q -n django-redis-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
/usr/sbin/redis-server --port 6379 &
export PYTHONPATH=.:tests
%python_exec tests/runtests.py
# The first four are errors on Python 2
# The last three tests tests raise NotImplementedError
%{python_expand DJANGO_SETTINGS_MODULE=tests.test_sqlite_sharding \
  $python -m pytest \
    --deselect tests/test_backend.py::DjangoRedisCacheTestEscapePrefix::test_keys \
    --deselect tests/test_backend.py::DjangoRedisCacheTests::test_delete_pattern \
    --deselect tests/test_backend.py::DjangoRedisCacheTests::test_touch_missed_key \
    --deselect tests/test_backend.py::DjangoRedisCacheTests::test_touch_negative_timeout \
    --deselect tests/test_backend.py::DjangoRedisCacheTests::test_touch_positive_timeout \
    --deselect tests/test_backend.py::DjangoRedisCacheTests::test_touch_zero_timeout \
    tests
}
%python_exec tests/runtests-herd.py
%python_exec tests/runtests-json.py
%python_exec tests/runtests-msgpack.py
%python_exec tests/runtests-zlib.py
%python_exec tests/runtests-lz4.py
killall redis-server

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
