#
# spec file for package python-websockets
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


%{?sle15_python_module_pythons}
Name:           python-websockets
Version:        14.2
Release:        0
Summary:        An implementation of the WebSocket Protocol (RFC 6455)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/aaugustin/websockets
Source:         https://github.com/aaugustin/websockets/archive/%{version}.tar.gz#/websockets-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm -f %{buildroot}%{$python_sitearch}/websockets/speedups.c

%check
# Test execution speed depends on BS load and architecture, relax
export WEBSOCKETS_TESTS_TIMEOUT_FACTOR=50
# Disable flaky tests gh#python-websockets/websockets#1322
donttest="test_close_waits_for_close_frame"
# Disable broken tests with openssl 3.2 and python < 3.11
donttest+=" or test_reject_invalid_server_certificate"

%ifarch s390x
# Skip flaky tests
donttest+=" or test_context_takeover"
donttest+=" or test_decompress_max_size"
donttest+=" or test_encode_decode_fragmented_binary_frame"
donttest+=" or test_encode_decode_fragmented_text_frame"
donttest+=" or test_remote_no_context_takeove"
donttest+=" or test_writing_in_send_context_fails"
%endif

%pytest_arch -v -k "not ($donttest)" tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/websockets
%{python_sitearch}/websockets-%{version}.dist-info

%changelog
