#
# spec file for package python-python-memcached
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
%define oldpython python
Name:           python-python-memcached
Version:        1.59
Release:        0
Summary:        Pure python memcached client
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/linsomniac/python-memcached
Source:         https://github.com/linsomniac/python-memcached/archive/%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  memcached
BuildRequires:  python-rpm-macros
BuildRequires:  util-linux
Requires:       memcached
Requires:       python-six
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-memcached = %{version}
Obsoletes:      %{oldpython}-memcached < %{version}
%endif
%python_subpackages

%description
This package was originally written by Evan Martin of Danga.
Sean Reifschneider of tummy.com, ltd. has taken over maintenance of it.

This software is a 100% Python interface to the memcached memory cache
daemon.  It is the client side software which allows storing values in one
or more, possibly remote, memcached servers.  Search google for memcached
for more information.

%prep
%setup -q -n python-memcached-%{version}
sed -i \
    -e 's:#!/usr/bin/env python::' \
    memcache.py

%build
%python_build

%install
%python_install

%check
%if 0%{?fedora} || 0%{?rhel}
/usr/bin/memcached -dv -P $PWD/memcached.pid
%else
/usr/sbin/memcached -dv -P $PWD/memcached.pid
%endif
%pytest
kill -9 $(cat $PWD/memcached.pid)

%files %{python_files}
%license PSF.LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
