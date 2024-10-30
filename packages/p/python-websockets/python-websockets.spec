#
# spec file for package python-websockets
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


%{?sle15_python_module_pythons}
Name:           python-websockets
Version:        13.1
Release:        0
Summary:        An implementation of the WebSocket Protocol (RFC 6455)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/aaugustin/websockets
Source:         https://github.com/aaugustin/websockets/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
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
%python_expand rm -f %{buildroot}%{$python_sitearch}/websockets/speedups.c

%check
# Test execution speed depends on BS load and architecture, relax
export WEBSOCKETS_TESTS_TIMEOUT_FACTOR=10
# Disable flaky tests gh#python-websockets/websockets#1322
donttest="test_close_waits_for_close_frame"
# Disable broken tests with openssl 3.2 and python < 3.11
donttest+=" or test_reject_invalid_server_certificate"
%pytest_arch -v -k "not ($donttest)" tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/websockets
%{python_sitearch}/websockets-%{version}-py*.egg-info

%changelog
