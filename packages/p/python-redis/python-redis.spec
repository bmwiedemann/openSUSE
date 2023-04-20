#
# spec file for package python-redis
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-redis
Version:        4.5.4
Release:        0
Summary:        Python client for Redis key-value store
License:        MIT
URL:            https://github.com/redis/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/redis/redis-%{version}.tar.gz
Source1:        https://github.com/redis/redis-py/raw/v%{version}/tox.ini
BuildRequires:  %{python_module async-timeout >= 4.0.2}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
BuildRequires:  redis
Requires:       python-async-timeout >= 4.0.2
Requires:       redis
Recommends:     python-hiredis >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
The Python interface to the Redis key-value store.

%prep
%autosetup -p1 -n redis-%{version}
# tox.ini for pytest markers
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# upstream's tox testsuite starts several servers in docker containers listening on different ports.
# We just start two of them locally
# master
# https://github.com/redis/redis/pull/9920
%{_sbindir}/redis-server --version | grep ' v=7\.' && redis7args="--enable-debug-command yes --enable-module-command yes"
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
if [ $(getconf LONG_BIT) -ne 64 ]; then
  # reference precision issues on 32-bit
  donttest=" or test_geopos"
fi
# gh#redis/redis-py#2554 and gh#redis/redis-py#2679
donttest="$donttest or test_xautoclaim or test_acl_list"
%pytest -m 'not (onlycluster or redismod)' -k "not (dummyprefix $donttest)" --ignore tests/test_ssl.py --ignore tests/test_asyncio/test_cluster.py --redis-url=redis://localhost:6379/

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/redis/
%{python_sitelib}/redis-%{version}*-info

%changelog
