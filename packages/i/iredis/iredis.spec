#
# spec file for package iredis
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


Name:           iredis
Version:        1.13.0
Release:        0
Summary:        Terminal client for Redis with auto-completion and syntax highlighting
License:        BSD-3-Clause
URL:            https://iredis.io/
Source:         https://files.pythonhosted.org/packages/source/i/iredis/iredis-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
# SECTION tests
# for killall
BuildRequires:  psmisc
BuildRequires:  python3-Pygments >= 2
BuildRequires:  python3-click >= 7.0
BuildRequires:  python3-configobj >= 5.0
BuildRequires:  python3-importlib-resources >= 5.1.0
BuildRequires:  python3-mistune >= 2.0
BuildRequires:  python3-pendulum >= 2.0
BuildRequires:  python3-pexpect
BuildRequires:  python3-pip
BuildRequires:  python3-prompt_toolkit >= 3
BuildRequires:  python3-pytest
BuildRequires:  python3-redis >= 3
BuildRequires:  python3-wcwidth >= 0.1.9
BuildRequires:  python3-wheel
BuildRequires:  redis
# /SECTION
Requires:       python3-Pygments >= 2
Requires:       python3-click >= 7.0
Requires:       python3-configobj >= 5.0
Requires:       python3-importlib-resources >= 5.1.0
Requires:       python3-mistune >= 2.0
Requires:       python3-pendulum >= 2.0
Requires:       python3-prompt_toolkit >= 3
Requires:       python3-redis >= 3
Requires:       python3-wcwidth >= 0.1.9
Recommends:     redis
BuildArch:      noarch

%description
A terminal client for redis with auto-completion and syntax
highlighting. IRedis lets one type Redis commands, and it displays results.

IRedis is an alternative for redis-cli. In most cases, IRedis behaves
exactly the same as redis-cli. IRedis will prevent accidentally
running dangerous commands.

%prep
%setup -q -n iredis-%{version}
# remove the <= version limitations
sed -E -i 's/,<[0-9.]+//' setup.py
# replace == version limitations with >=
sed -E -i 's/==/>=/' setup.py

%build
%python3_build

%install
%python3_install
rm -r %{buildroot}%{python3_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{python3_sitelib}

%check
# increase the timeouts
sed -i 's/timeout=1/timeout=5/' tests/cli_tests/test_*.py
sed -i 's/timeout=2/timeout=5/' tests/cli_tests/test_*.py
sed -i 's/timeout=10/timeout=20/' tests/cli_tests/test_*.py
# the tests are extremely flaky on i586 (hitting timeouts)long as x86_64 succeeds, we don't care as this is noarch
%ifnarch %ix86
%{_sbindir}/redis-server --port 6379 &
# skip test_abort_reading_connection as it fails frequently (timeout) on OBS for no apparent reason, others are bugs upstream: https://github.com/laixintao/iredis/issues/417
# skip test_peek_zset_fetch_all, test_peek_zset_fetch_part, reported upstream: https://github.com/laixintao/iredis/issues/432
# skip test_auto_select_db_and_auth_for_reconnect_only_6 needs further inspection
REDIS_VERSION=$(%{_sbindir}/redis-server --version | grep -o '[0-9]' | head -n 1) PATH=${PATH:+$PATH:}%{buildroot}%{_bindir} PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 pytest --ignore=_build.python3 -vv -k 'not (test_abort_reading_connection or test_peek_set_fetch_part or test_peek_stream or test_timestamp_completer_humanize_time_completion or test_peek_zset_fetch_all or test_peek_zset_fetch_part or test_auto_select_db_and_auth_for_reconnect_only_6)'
killall redis-server
%endif

%files
%{python3_sitelib}/iredis*
%{_bindir}/iredis
%license LICENSE

%changelog
