#
# spec file for package python-redis
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


%bcond_without testing

%{?sle15_python_module_pythons}
Name:           python-redis
Version:        5.2.0
Release:        0
Summary:        Python client for Redis key-value store
License:        MIT
URL:            https://github.com/redis/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/redis/redis-%{version}.tar.gz
Source1:        https://github.com/redis/redis-py/raw/refs/tags/v%{version}/pytest.ini
Patch0:         increase-test-timeout.patch
BuildRequires:  %{python_module async-timeout >= 4.0.2 if %python-base < 3.11.3}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio < 0.24}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
%if %{with testing}
BuildRequires:  redis
%endif
Requires:       (python-async-timeout >= 4.0.2 if python-base < 3.11.3)
Recommends:     python-hiredis >= 1.0.0
Recommends:     redis
BuildArch:      noarch
%python_subpackages

%description
The Python interface to the Redis key-value store.

%prep
%autosetup -N -n redis-%{version}
# pytest.ini for pytest markers but without coverage
sed /coverage/d  %SOURCE1 > pytest.ini
%ifarch s390x
%patch -P 0 -p1
%endif

# These tests pass locally but fail in obs with different
# environment, like ALP build...
rm tests/test_commands.py*
rm tests/test_asyncio/test_commands.py
# The openSUSE redis json, bloom, ts and
# graph are missing in the repos
rm tests/test_bloom.py
rm tests/test_graph.py
rm tests/test_json.py
rm tests/test_timeseries.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with testing}
%check
# upstream's tox testsuite starts several servers in docker containers listening on different ports.
# We just start two of them locally
# master
# https://github.com/redis/redis/pull/9920
%{_sbindir}/redis-server --version | grep ' v=[78]\.' && redis7args="--enable-debug-command yes --enable-module-command yes"
%{_sbindir}/redis-server --port 6379 --save "" $redis7args &
victims="$!"
trap "kill $victims || true" EXIT
sleep 2
# replica
%{_sbindir}/redis-server --port 6380 --save "" --replicaof localhost 6379  &
victims="$victims $!"
trap "kill $victims || true" EXIT
sleep 2
# onlycluster: skip tests which require a full cluster
# redismod: Not available (https://github.com/RedisLabsModules/redismod)
# ssl: no stunnel with certs from docker container, fails at test collection
#
# broken tests in ppc64le
donttest="test_geopos or test_georadius"
# gh#redis/redis-py#2554
donttest="$donttest or test_xautoclaim"
# gh#redis/redis-py#2679
donttest+=" or test_acl_getuser_setuser or test_acl_log"
%pytest -m 'not (onlycluster or redismod or ssl)' -k "not ($donttest)" --ignore tests/test_ssl.py --ignore tests/test_asyncio/test_cluster.py --redis-url=redis://localhost:6379/
%endif

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/redis/
%{python_sitelib}/redis-%{version}.dist-info

%changelog
