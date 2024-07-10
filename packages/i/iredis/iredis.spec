#
# spec file for package iredis
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


%define pythons python3
Name:           iredis
Version:        1.14.1
Release:        0
Summary:        Terminal client for Redis with auto-completion and syntax highlighting
License:        BSD-3-Clause
URL:            https://iredis.xbin.io/
Source:         https://github.com/laixintao/iredis/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-poetry
BuildRequires:  python3-setuptools
# SECTION tests
# for killall
BuildRequires:  psmisc
BuildRequires:  python3-Pygments >= 2
BuildRequires:  python3-click >= 8.0
BuildRequires:  python3-configobj >= 5.0
BuildRequires:  python3-mistune >= 3.0
BuildRequires:  python3-packaging >= 23.0
BuildRequires:  python3-pendulum >= 2.1.0
BuildRequires:  python3-pexpect
BuildRequires:  python3-pip
BuildRequires:  python3-prompt_toolkit >= 3
BuildRequires:  python3-pytest
BuildRequires:  python3-redis >= 4.5.3
BuildRequires:  python3-wcwidth >= 0.1.9
BuildRequires:  python3-wheel
BuildRequires:  redis >= 5.0.0
# /SECTION
Requires:       python3-Pygments >= 2
Requires:       python3-click >= 8.0
Requires:       python3-configobj >= 5.0
Requires:       python3-mistune >= 2.0
Requires:       python3-packaging >= 23.0
Requires:       python3-pendulum >= 2.1.0
Requires:       python3-prompt_toolkit >= 3
Requires:       python3-redis >= 3
Requires:       python3-wcwidth >= 0.1.9
Recommends:     redis >= 5.0.0
BuildArch:      noarch

%description
A terminal client for redis with auto-completion and syntax
highlighting. IRedis lets one type Redis commands, and it displays results.

IRedis is an alternative for redis-cli. In most cases, IRedis behaves
exactly the same as redis-cli. IRedis will prevent accidentally
running dangerous commands.

%prep
%setup -q -n iredis-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
# increase the timeouts
sed -i 's/timeout=1/timeout=5/' tests/cli_tests/test_*.py
sed -i 's/timeout=2/timeout=5/' tests/cli_tests/test_*.py
sed -i 's/timeout=10/timeout=20/' tests/cli_tests/test_*.py
# the tests are extremely flaky on i586 (hitting timeouts), as long as x86_64 succeeds, we don't care as this is noarch
%ifnarch %ix86
%{_sbindir}/redis-server --port 6379 &
# wait for redis startup
sleep 2
# disable snapshots
redis-cli CONFIG SET save ""
# skip test_abort_reading_connection as it fails frequently (timeout) on OBS for no apparent reason, others are bugs upstream: https://github.com/laixintao/iredis/issues/417
# skip test_peek_zset_fetch_all, test_peek_zset_fetch_part, reported upstream: https://github.com/laixintao/iredis/issues/432
# skip test_auto_select_db_and_auth_for_reconnect_only_6 needs further inspection
# skip test_timer and test_command_completion_when_a_command_is_another_command_substring and test_trasaction_syntax_error and test_subscribe because of timeouts (too slow) on s390x
REDIS_VERSION=$(%{_sbindir}/redis-server --version | grep -o '[0-9]' | head -n 1) PATH=${PATH:+$PATH:}%{buildroot}%{_bindir} PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 pytest --ignore=_build.python3 -vv -k 'not (test_abort_reading_connection or test_peek_set_fetch_part or test_peek_stream or test_timestamp_completer_humanize_time_completion or test_peek_zset_fetch_all or test_peek_zset_fetch_part or test_auto_select_db_and_auth_for_reconnect_only_6 or test_timer or test_command_completion_when_a_command_is_another_command_substring) or test_trasaction_syntax_error or test_subscribe'
killall redis-server
%endif

%files
%{python3_sitelib}/iredis/
%{python3_sitelib}/iredis-%{version}*-info
%{_bindir}/iredis
%license LICENSE

%changelog
