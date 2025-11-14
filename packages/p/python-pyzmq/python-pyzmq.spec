#
# spec file for package python-pyzmq
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


%define skip_python2 1
%define plainpython python
%ifarch x86_64
%bcond_without  tests
%else
# Disable tests, they are very slow/halt on many arch
%bcond_with     tests
%endif
%{?sle15_python_module_pythons}
Name:           python-pyzmq
Version:        27.1.0
Release:        0
Summary:        Python bindings for 0MQ
License:        BSD-3-Clause AND LGPL-3.0-or-later
URL:            https://github.com/zeromq/pyzmq
Source:         https://files.pythonhosted.org/packages/source/p/pyzmq/pyzmq-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-build-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  zeromq-devel
Recommends:     python-gevent
Recommends:     python-numpy
Recommends:     python-pexpect
Recommends:     python-simplejson
Recommends:     python-tornado
Suggests:       python-paramiko
# SECTION Test requirements
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module tornado}
%if 0%{?suse_version} >= 1550
BuildRequires:  %{python_module numpy}
%endif
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

# Fix non-executable script rpmlint warning:
find examples zmq -name "*.py" -exec sed -i "s|#\!\/usr\/bin\/env python||" {} \;
find . -name ".gitignore" -exec rm {} \;
chmod -x examples/pubsub/topics_pub.py examples/pubsub/topics_sub.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with tests}
%check
# make tests importable
dir=$(mktemp -d)
cp -a tests $dir
export PYTHONPATH=$dir
export LANG=en_US.UTF-8
# unreliable socket handling in obs environment
SKIPPED_TESTS+=" or test_log"
%if 0%{?suse_version} < 1550
# tries to open a network connection on older distributions
SKIPPED_TESTS+=" or test_null or test_int_sockopts"
%endif
%pytest_arch -v -k "not (${SKIPPED_TESTS:4})"
%endif

%files %{python_files}
%license LICENSE.md
%doc AUTHORS.md README.md examples
%{python_sitearch}/zmq
%{python_sitearch}/pyzmq-%{version}.dist-info
%exclude %{python_sitearch}/zmq/backend/cffi/*.c
%exclude %{python_sitearch}/zmq/utils/*.h
%exclude %{python_sitearch}/zmq/backend/cffi/_cdefs.h

%files %{python_files devel}
%{python_sitearch}/zmq/utils/*.h
%{python_sitearch}/zmq/backend/cffi/*.c
%{python_sitearch}/zmq/backend/cffi/_cdefs.h

%changelog
