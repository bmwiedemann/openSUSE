#
# spec file for package python-pymemcache
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2014 Thomas Bechtold <thomasbechtold@jpberlin.de>
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
Name:           python-pymemcache
Version:        3.4.4
Release:        0
Summary:        A pure Python memcached client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Pinterest/pymemcache
Source:         https://files.pythonhosted.org/packages/source/p/pymemcache/pymemcache-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/pinterest/pymemcache/pull/327.patch#/merged_pr_327.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  memcached
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-memcached}
BuildRequires:  %{python_module six}
# /SECTION
%if %{with python2}
BuildRequires:  python-future
%endif
%ifpython2
Requires:       python-future
%endif
%python_subpackages

%description
A pure-Python memcached client.

pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the speed of writes.
* Flexible, simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache misses.

%prep
%setup -q -n pymemcache-%{version}
%patch0 -p1
# Disable pytest-cov
sed -i 's/tool:pytest/tool:ignore-pytest-cov/' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{_sbindir}/memcached &
# TLS tests depend on setting up a memcached equivalent to
# https://github.com/scoriacorp/docker-tls-memcached
%pytest -rs -k 'not tls'


%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
