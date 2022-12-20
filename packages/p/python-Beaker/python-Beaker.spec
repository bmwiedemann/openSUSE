#
# spec file for package python-Beaker
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-Beaker
Version:        1.12.0
Release:        0
Summary:        A Session and Caching library with WSGI Middleware
License:        BSD-3-Clause
URL:            https://github.com/bbangert/beaker
Source:         https://github.com/bbangert/beaker/archive/%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support pymemcache
Patch0:         support-pymemcache.patch
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-memcached}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  glibc-locale
BuildRequires:  python-rpm-macros
Requires:       python-dbm
Requires:       python-pylibmc
Requires:       python-setuptools
Recommends:     python-SQLAlchemy
Recommends:     python-cryptography
Recommends:     python-pycrypto
Recommends:     python-pycryptopp >= 0.5.12
Recommends:     python-pymemcache
Recommends:     python-pymongo
Recommends:     python-redis
BuildArch:      noarch
%python_subpackages

%description
Beaker is a web session and general caching library that includes WSGI
middleware for use in web applications.

As a general caching library, Beaker can handle storing for various times
any Python object that can be pickled with optional back-ends on a
fine-grained basis.

Beaker was built largely on the code from MyghtyUtils, then refactored and
extended with database support.

Beaker includes Cache and Session WSGI middleware to ease integration with
WSGI capable frameworks, and is automatically used by Pylons.

Features include:

* Fast, robust performance
* Multiple reader/single writer lock system to avoid duplicate simultaneous
  cache creation
* Cache back-ends include dbm, file, memory, memcached, and database (Using
  SQLAlchemy for multiple-db vendor support)
* Signed cookie's to prevent session hijacking/spoofing
* Cookie-only sessions to remove the need for a db or file backend (ideal
  for clustered systems)
* Extensible Container object to support new back-ends
* Cache's can be divided into namespaces (to represent templates, objects,
  etc.) then keyed for different copies
* Create functions for automatic call-backs to create new cache copies after
  expiration
* Fine-grained toggling of back-ends, keys, and expiration per Cache object

%prep
%autosetup -p1 -n beaker-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# needs mongo and redis running
rm -r tests/test_managers
rm tests/test_memcached.py
rm tests/test_cachemanager.py
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}
# gh#bbangert/beaker#172
rm -fv tests/test.db
pytest tests
}

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG
%{python_sitelib}/beaker/
%{python_sitelib}/Beaker-%{version}-py*.egg-info

%changelog
