#
# spec file for package python-pyzmq
#
# Copyright (c) 2020 SUSE LLC
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
# Disable tests, they are very slow/halt on many arch
%ifarch x86_64
%bcond_without  tests
%else
%bcond_with     tests
%endif
Name:           python-pyzmq
Version:        19.0.2
Release:        0
Summary:        Python bindings for 0MQ
License:        LGPL-3.0-or-later AND BSD-3-Clause
URL:            https://github.com/zeromq/pyzmq
Source:         https://files.pythonhosted.org/packages/source/p/pyzmq/pyzmq-%{version}.tar.gz
Source1:        python-pyzmq-rpmlintrc
# PATCH-FIX-OPENSUSE skip_test_tracker.patch
Patch1:         skip_test_tracker.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module gevent}
# Test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  zeromq-devel
Requires:       python
%if 0%{?suse_version} >= 1000 || 0%{?fedora_version} >= 24
Recommends:     python-cffi
Recommends:     python-gevent
Recommends:     python-numpy
Recommends:     python-paramiko
Recommends:     python-pexpect
Recommends:     python-py
Recommends:     python-simplejson
Recommends:     python-tornado
Recommends:     zeromq
%endif
%python_subpackages

%description
PyZMQ is a lightweight and super-fast messaging library built on top of
the ZeroMQ library (http://www.zeromq.org).

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       python-devel
Requires:       zeromq-devel

%description devel
Development libraries and headers needed to build software using %{name}.

%prep
%setup -q -n pyzmq-%{version}
# Fix non-executable script rpmlint warning:
find examples zmq -name "*.py" -exec sed -i "s|#\!\/usr\/bin\/env python||" {} \;

# Remove non-deterministic authentication test
# This fails to connect randomly
rm -rf zmq/tests/test_auth.py
sed -i '/from zmq.tests.test_auth/d' zmq/tests/asyncio/_test_asyncio.py
sed -i 's/TestThreadAuthentication/object/' zmq/tests/asyncio/_test_asyncio.py

%patch1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with tests}
%check
export LANG=en_US.UTF-8
# skipped tests because of gh#zeromq/pyzmq#1431
SKIPPED_TESTS="test_buffer_numpy or test_bytes or test_curve or test_frame_more or "
SKIPPED_TESTS+="test_large_send or test_lifecycle1 or test_lifecycle2 or "
SKIPPED_TESTS+="test_memoryview_shape or test_multi_tracker or test_plain or test_tracker"
# gh#zeromq/pyzmq#1432
SKIPPED_TESTS+=" or TestSocketGreen"
%pytest_arch -k "not (${SKIPPED_TESTS})"
%endif

%files %{python_files}
%license COPYING.BSD COPYING.LESSER
%doc AUTHORS.md README.md examples
%{python_sitearch}/zmq/
%{python_sitearch}/pyzmq-%{version}-py*.egg-info
%exclude %{python_sitearch}/zmq/utils/*.h
%exclude %{python_sitearch}/zmq/backend/cffi/_verify.c
%exclude %{python_sitearch}/zmq/backend/cffi/_cdefs.h

%files %{python_files devel}
%{python_sitearch}/zmq/utils/*.h
%{python_sitearch}/zmq/backend/cffi/_verify.c
%{python_sitearch}/zmq/backend/cffi/_cdefs.h

%changelog
