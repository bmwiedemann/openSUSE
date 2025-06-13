#
# spec file for package python-redis
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%endif

%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-redis%{psuffix}
Version:        6.2.0
Release:        0
Summary:        Python client for Redis key-value store
License:        MIT
URL:            https://github.com/redis/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/redis/redis-%{version}.tar.gz
Patch0:         increase-test-timeout.patch
Patch1:         remove-mock.patch
BuildRequires:  %{python_module async-timeout >= 4.0.2 if %python-base < 3.11.3}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module redis = %{version}}
BuildRequires:  %{python_module redis-entraid}
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
%ifarch s390x
%patch -P 0 -p1
%endif
%patch -P 1 -p1

# These tests pass locally but fail in obs with different
# environment, like ALP build...
rm tests/test_commands.py*
rm tests/test_asyncio/test_commands.py
# The openSUSE redis json, bloom, ts
# are missing in the repos
rm tests/test_bloom.py
rm tests/test_json.py
rm tests/test_timeseries.py

%if %{without test}
%build
%pyproject_wheel
%endif

%if %{without test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
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
# gh#python/cpython#70654 -- Fix only present in python313 so disable the tests
donttest+=" or test_re_auth_pub_sub_in_resp3 or test_do_not_re_auth_pub_sub_in_resp2"
# gh#redis/redis-py#2679
donttest+=" or test_acl_getuser_setuser or test_acl_log"
%pytest -m 'not (onlycluster or redismod or ssl or graph)' -k "not ($donttest)" --ignore tests/test_ssl.py --ignore tests/test_asyncio/test_cluster.py --redis-url=redis://localhost:6379/
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/redis/
%{python_sitelib}/redis-%{version}.dist-info
%endif

%changelog
