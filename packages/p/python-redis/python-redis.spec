#
# spec file for package python-redis
#
# Copyright (c) 2025 SUSE LLC and contributors
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

# Add needed cli opts when running redis-server if redis/valkey version >= 7.0.0
%define redis_opts %[v"%(%{_sbindir}/redis-server --version | cut -d " " -f "3" | tr -d "v=")" >= v"7.0.0" ? "--enable-debug-command yes --enable-module-command yes" : ""]

%{?sle15_python_module_pythons}
Name:           python-redis%{psuffix}
Version:        7.0.1
Release:        0
Summary:        Python client for Redis key-value store
License:        MIT
URL:            https://github.com/redis/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/redis/redis-%{version}.tar.gz
# Based on https://github.com/redis/redis-py/blob/master/dockers/sentinel.conf
Source1:        sentinel.conf
Source2:        skipped_tests
Patch0:         increase-test-timeout.patch
# PATCH-FIX-UPSTREAM Based on gh#redis/redis-py#3830
Patch1:         remove-mock.patch
Patch2:         test_add_elem_no_quant.patch
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
BuildRequires:  %{python_module pybreaker >= 1.4}
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
%patch -P 2 -p1

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
%{_sbindir}/redis-server --port 6379 --save "" %redis_opts &
victims="$!"
# replica
%{_sbindir}/redis-server --port 6380 --save "" --replicaof localhost 6379  &
victims="$victims $!"
# sentinel
cp %{SOURCE1} .
%{_sbindir}/redis-sentinel sentinel.conf &
victims="$victims $!"
trap "kill $victims || true" EXIT
sleep 2

# load list of tests to skip from skipped_tests
source %{SOURCE2}

%pytest "${skipped_tests[@]}" $(%{_sbindir}/redis-server --version | grep -q 'Valkey' && echo "${valkey_skipped_tests[@]}") --redis-url=redis://localhost:6379/
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/redis/
%{python_sitelib}/redis-%{version}.dist-info
%endif

%changelog
