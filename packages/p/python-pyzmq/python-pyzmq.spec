#
# spec file for package python-pyzmq
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


%define skip_python2 1
%define plainpython python
%ifarch x86_64
%bcond_without  tests
%else
# Disable tests, they are very slow/halt on many arch
%bcond_with     tests
%endif
Name:           python-pyzmq
Version:        24.0.1
Release:        0
Summary:        Python bindings for 0MQ
License:        BSD-3-Clause AND LGPL-3.0-or-later
URL:            https://github.com/zeromq/pyzmq
Source:         https://files.pythonhosted.org/packages/source/p/pyzmq/pyzmq-%{version}.tar.gz
# For test markers
Source1:        https://raw.githubusercontent.com/zeromq/pyzmq/v%{version}/pytest.ini
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  zeromq-devel
Recommends:     python-gevent
Recommends:     python-numpy
Recommends:     python-pexpect
Recommends:     python-simplejson
Recommends:     python-tornado
Suggests:       python-paramiko
# SECTION Test requirements
%if 0%{?suse_version} >= 1550
BuildRequires:  %{python_module numpy}
%endif
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module tornado}
%if 0%{?suse_version} >= 1550
# SLE/Leap <= 15.4 has incompatible gevent API # https://www.gevent.org/api/gevent.timeout.html#gevent.Timeout.close
BuildRequires:  %{python_module gevent >= 1.3a1}
%endif
# /SECTION
# SECTION pypy3 is not in openSUSE at the moment, it would use the cffi backend
BuildRequires:  %{python_module cffi if (%python with pypy3)}
BuildRequires:  %{python_module py   if (%python with pypy3)}
%if "%{python_flavor}" == "pypy3"
Requires:       python-cffi
Requires:       python-py
%endif
# /SECTION
%python_subpackages

%description
PyZMQ is a lightweight and super-fast messaging library built on top of
the ZeroMQ library (http://www.zeromq.org).

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       python-devel
Requires:       zeromq-devel
Requires:       %plainpython(abi) = %{python_version}

%description devel
Development libraries and headers needed to build software using %{name}.

%prep
%autosetup -n pyzmq-%{version} -p1
cp %{SOURCE1} ./

# Fix non-executable script rpmlint warning:
find examples zmq -name "*.py" -exec sed -i "s|#\!\/usr\/bin\/env python||" {} \;
chmod -x examples/pubsub/topics_pub.py examples/pubsub/topics_sub.py

# See https://github.com/zeromq/pyzmq/blob/master/setup.cfg.template
echo '
[global]
skip_check_zmq = False
zmq_prefix = %{_prefix}
no_libzmq_extension = True
'>> setup.cfg

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with tests}
%check
export LANG=en_US.UTF-8
# This test wants to build a custom cython extension, but does
# not have the source files installed into the buildroot
SKIPPED_TESTS+=" or test_cython"
# unreliable socket handling in obs environment
SKIPPED_TESTS+=" or test_log"
%if 0%{?suse_version} < 1550
# tries to open a network connection on older distributions
SKIPPED_TESTS+=" or test_null or test_int_sockopts"
%endif
# temporarily disable to build with OpenSSL 3.0 bsc#1205042
SKIPPED_TESTS+=" or test_on_recv_basic"
mkdir cleantest
pushd cleantest
%pytest_arch --pyargs zmq -k "not (${SKIPPED_TESTS:4})" --timeout 1200
popd
%endif

%files %{python_files}
%license COPYING.BSD COPYING.LESSER
%doc AUTHORS.md README.md examples
%{python_sitearch}/zmq
%{python_sitearch}/pyzmq-%{version}-py*.egg-info
%exclude %{python_sitearch}/zmq/utils/*.h
%exclude %{python_sitearch}/zmq/backend/cffi/_cdefs.h

%files %{python_files devel}
%{python_sitearch}/zmq/utils/*.h
%{python_sitearch}/zmq/backend/cffi/_cdefs.h

%changelog
