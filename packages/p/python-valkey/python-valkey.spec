#
# spec file for package python-valkey
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


Name:           python-valkey
Version:        6.1.1
Release:        0
Summary:        Python client for Valkey forked from redis-py
License:        MIT
URL:            https://github.com/valkey-io/valkey-py
Source0:        https://github.com/valkey-io/valkey-py/archive/refs/tags/v%{version}.tar.gz#/valkey-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/valkey-io/valkey-py/refs/heads/main/dockers/cluster.valkey.conf#/server.conf
# Based on https://github.com/valkey-io/valkey-py/blob/main/dockers/sentinel.conf
Source2:        sentinel.conf
# PATCH-FIX-UPSTREAM fix-tests-valkey-9.0.patch
# https://github.com/valkey-io/valkey-py/pull/239
Patch0:         fix-tests-valkey-9.0.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Tests
BuildRequires:  %{python_module cachetools}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  valkey
Suggests:       python-cryptography >= 36.0.1
Suggests:       python-PyOpenSSL >= 23.2.1
Suggests:       python-requests >= 2.31.0
BuildArch:      noarch
%python_subpackages

%description
Python client for Valkey forked from redis-py

%prep
%autosetup -p1 -n valkey-py-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Start a server
valkey-server %SOURCE1 --port 6379 &
server_pid=$!
# We also need a sentinel service running
cp %SOURCE2 .
valkey-sentinel sentinel.conf &
sentinel_pid=$!
# Requires entire stunnel setup and certs
ignore="--ignore tests/test_ssl.py"
# Requires a replica setup
donttest="test_psync"
# Requires module setting
donttest+=" or test_module"
%pytest $ignore -m 'not onlycluster' -k "not ($donttest)"
kill -9 $server_pid $sentinel_pid

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/valkey
%{python_sitelib}/valkey-%{version}.dist-info

%changelog
