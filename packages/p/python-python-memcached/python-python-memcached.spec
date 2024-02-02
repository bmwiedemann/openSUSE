#
# spec file for package python-python-memcached
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-python-memcached
Version:        1.62
Release:        0
Summary:        Pure python memcached client
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/linsomniac/python-memcached
Source:         https://github.com/linsomniac/python-memcached/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  memcached
BuildRequires:  python-rpm-macros
BuildRequires:  util-linux
Requires:       memcached
BuildArch:      noarch
%python_subpackages

%description
This package was originally written by Evan Martin of Danga.
Sean Reifschneider of tummy.com, ltd. has taken over maintenance of it.

This software is a 100% Python interface to the memcached memory cache
daemon.  It is the client side software which allows storing values in one
or more, possibly remote, memcached servers.  Search google for memcached
for more information.

%prep
%autosetup -p1 -n python-memcached-%{version}
sed -i \
    -e 's:#!%{_bindir}/env python::' \
    memcache.py
sed -i -e '/__version__/s/[0-9.]\+/%{version}/' memcache.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{_bindir}/memcached -dv -P $PWD/memcached.pid
%pytest
kill -9 $(cat $PWD/memcached.pid)

%files %{python_files}
%license PSF.LICENSE
%doc README.md
%{python_sitelib}/memcache.py
%pycache_only %{python_sitelib}/__pycache__/memcache.*.pyc
%{python_sitelib}/python_memcached-%{version}.dist-info

%changelog
