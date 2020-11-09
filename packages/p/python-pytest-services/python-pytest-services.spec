#
# spec file for package python-pytest-services
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
Name:           python-pytest-services
Version:        2.2.1
Release:        0
Summary:        Services plugin for pytest testing framework
License:        MIT
URL:            https://github.com/pytest-dev/pytest-services
Source:         https://github.com/pytest-dev/pytest-services/archive/%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zc.lockfile >= 2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python-subprocess32
%endif
Requires:       python-psutil
Requires:       python-pytest
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-zc.lockfile >= 2.0
Recommends:     python-pylibmc
BuildArch:      noarch
%ifpython2
Requires:       python-subprocess32
%endif
%python_subpackages

%description
The plugin provides a set of fixtures and utility functions to start service
processes for your tests with pytest.

%prep
%setup -q -n pytest-services-%{version}
# we don't test mysql anway
sed -i -e '/import MySQLdb/d' tests/test_plugin.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_memcached test_mysql test_xvfb - need running X/mysql/memcache servers
%pytest -k 'not (test_memcached or test_mysql or test_xvfb)'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
