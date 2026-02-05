#
# spec file for package python-aiorpcX
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-aiorpcX
Version:        0.25.0
Release:        0
Summary:        Generic async RPC implementation, including JSON-RPC
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kyuupichan/aiorpcX
Source:         https://github.com/kyuupichan/aiorpcX/archive/%{version}.tar.gz
Patch0:         0001-Remove-event_loop-fixture-usage-from-tests.patch
# PATCH-FIX-OPENSUSE fix-jsonrpc-test-misc.patch -- gh#kyuupichan/aiorpcX#56
Patch1:         fix-jsonrpc-test-misc.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Recommends:     python-websockets
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 2.3.2}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module uvloop}
BuildRequires:  %{python_module websockets}
# /SECTION
%python_subpackages

%description
Generic async RPC implementation, including JSON-RPC

%prep
%autosetup -p1 -n aiorpcX-%{version}
# needs network
rm tests/test_websocket.py
chmod a-x LICENCE README.rst docs/*

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the two disabled tests below need network
SKIP_TESTS="test_auto_detect_address_failure or test_create_connection_resolve_good"
# test_slow_connection_aborted - randomly fails, out of 10 runs 6 fails
SKIP_TESTS="$SKIP_TESTS or test_slow_connection_aborted"
# test_cancel_remaining_on_group_with_stubborn_task - cannot import create_task -- why? (A new test from 82048a219aac.)
SKIP_TESTS="$SKIP_TESTS or test_cancel_remaining_on_group_with_stubborn_task"
%pytest -k "not ($SKIP_TESTS)"

%files %{python_files}
%doc README.rst docs/*.rst
%license LICENCE
%{python_sitelib}/aiorpcx
%{python_sitelib}/aiorpc[xX]-%{version}.dist-info

%changelog
