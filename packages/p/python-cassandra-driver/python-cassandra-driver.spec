#
# spec file for package python-cassandra-driver
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
Name:           python-cassandra-driver
Version:        3.20.2
Release:        0
Summary:        Python driver for Cassandra
License:        Apache-2.0
URL:            https://github.com/datastax/python-driver
Source:         https://github.com/datastax/python-driver/archive/%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module scales}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six} >= 1.6
BuildRequires:  %{python_module sure}
BuildRequires:  fdupes
BuildRequires:  libev-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python2-futures
Requires:       python-Cython
Requires:       python-blist
Requires:       python-six >= 1.6
Recommends:     python-Twisted
Recommends:     python-eventlet
Recommends:     python-gevent
%ifpython2
Requires:       python2-futures
%endif
%python_subpackages

%description
A tunable Python client library for Apache Cassandra (1.2+) and
DataStax Enterprise (3.1+) using exclusively Cassandra's binary
protocol and Cassandra Query Language v3.
A list of features may be found at https://github.com/datastax/python-driver#features .

%prep
%setup -q -n python-driver-%{version}
# do not run integration tests
rm -rf tests/integration
rm -rf tests/stress_tests
# do not run cython tests
rm -rf tests/unit/cython
# fix hardcoded cython dep
sed -i -e 's:Cython>=0.20,!=0.25,<0.29:Cython:g' setup.py

%build
export CFLAGS="%{optflags}"
export CASS_DRIVER_NO_EXTENSIONS=1
%python_build

%install
export CASS_DRIVER_NO_EXTENSIONS=1
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH="$(pwd)" nosetests-%{$python_version} -v

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitearch}/cassandra
%dir %{python_sitearch}/cassandra_driver-%{version}-py*.egg-info
%{python_sitearch}/cassandra/*
%{python_sitearch}/cassandra_driver-%{version}-py*.egg-info/*

%changelog
