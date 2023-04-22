#
# spec file for package python-websockets
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
%{?sle15_python_module_pythons}
Name:           python-websockets
Version:        10.4
Release:        0
Summary:        An implementation of the WebSocket Protocol (RFC 6455)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/aaugustin/websockets
Source:         https://github.com/aaugustin/websockets/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
WebSockets is a library for developing WebSocket servers_ and clients_ in
Python. It implements RFC 6455 with a focus on correctness and simplicity.
It passes the Autobahn Testsuite.

Built on top of Python's asynchronous I/O support introduced in PEP 3156,
it provides an API based on coroutines, making it easy to write highly
concurrent applications.

%prep
%autosetup -p1 -n websockets-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Test execution speed depends on BS load and architecture, relax
export WEBSOCKETS_TESTS_TIMEOUT_FACTOR=10
# https://github.com/aaugustin/websockets/issues/855 is an intermittent failure
# for test_keepalive_ping_does_not_crash_when_connection_lost on s390x
# export PYTHONWARNINGS=default
# test suite temporarily broken on python 3.9.7: gh#aaugustin/websockets#1051
python39_donttest=(-k testnothing)
%pyunittest_arch -v "${$python_donttest[@]}"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/websockets
%{python_sitearch}/websockets-%{version}-py*.egg-info

%changelog
