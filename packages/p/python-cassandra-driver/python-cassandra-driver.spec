#
# spec file for package python-cassandra-driver
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


%{?sle15_python_module_pythons}
Name:           python-cassandra-driver
Version:        3.29.2
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
BuildRequires:  %{python_module geomet >= 0.1}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pure-sasl}
BuildRequires:  %{python_module pyasyncore if %python-base >= 3.12}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libev-devel
BuildRequires:  python-rpm-macros
Requires:       python-Cython
Requires:       python-geomet >= 0.1
Recommends:     python-Twisted
Recommends:     python-eventlet
Recommends:     python-gevent
%if 0%{?python_version_nodots} > 311
Requires:       python-pyasyncore
%endif
%if %{with python2}
BuildRequires:  python2-futures
%endif
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
%autosetup -p1 -n python-driver-%{version}
# do not run integration tests
rm -rf tests/integration
rm -rf tests/stress_tests
# do not run cython tests
rm -rf tests/unit/cython
# fail on 32bit as it overflows
rm -f tests/unit/test_types.py
# fix hardcoded cython dep
sed -i -e 's:Cython>=0.20,!=0.25,<0.29:Cython:g' setup.py
# fix tests on Python 3.12
sed -i 's/assertRaisesRegexp/assertRaisesRegex/' tests/unit/test_response_future.py
# remove C sources
rm -f cassandra/cmurmur3.c cassandra/io/libevwrapper.c cassandra/numpyFlags.h

%build
export CFLAGS="%{optflags}"
export CASS_DRIVER_NO_EXTENSIONS=1
%pyproject_wheel

%install
export CASS_DRIVER_NO_EXTENSIONS=1
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# https://datastax-oss.atlassian.net/browse/PYTHON-1273
%pytest -k 'not (test_connection_initialization or test_nts_token_performance or test_host_connection_pool)'
# https://datastax-oss.atlassian.net/browse/PYTHON-1300
pytest tests/unit/test_host_connection_pool.py -k "HostConnectionTests"
pytest tests/unit/test_host_connection_pool.py -k "HostConnectionPoolTests"

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitearch}/cassandra
%dir %{python_sitearch}/cassandra_driver-%{version}.dist-info
%{python_sitearch}/cassandra/*
%{python_sitearch}/cassandra_driver-%{version}.dist-info/*

%changelog
