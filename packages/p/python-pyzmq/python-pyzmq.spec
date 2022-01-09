#
# spec file for package python-pyzmq
#
# Copyright (c) 2022 SUSE LLC
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
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Disable tests, they are very slow/halt on many arch
%ifarch x86_64
%bcond_without  tests
%else
%bcond_with     tests
%endif
Name:           python-pyzmq
Version:        22.3.0
Release:        0
Summary:        Python bindings for 0MQ
License:        BSD-3-Clause AND LGPL-3.0-or-later
URL:            https://github.com/zeromq/pyzmq
Source:         https://files.pythonhosted.org/packages/source/p/pyzmq/pyzmq-%{version}.tar.gz
Source1:        python-pyzmq-rpmlintrc
# PATCH-FIX-UPSTREAM less-flaky.patch bsc#[0-9]+ mcepl@suse.com
# Make test suite less flaky
Patch0:         less-flaky.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  zeromq-devel
# SECTION Test requirements
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
# /SECTION
# SECTION pypy3 is not in openSUSE at the moment, it would use the cffi backend
BuildRequires:  %{python_module cffi if (%python with pypy3)}
BuildRequires:  %{python_module py   if (%python with pypy3)}
%if "%{python_flavor}" == "pypy3"
Requires:       python-cffi
Requires:       python-py
%endif
# /SECTION
%if 0%{?suse_version} >= 1000 || 0%{?fedora_version} >= 24
Recommends:     python-gevent
Recommends:     python-numpy
Recommends:     python-pexpect
Recommends:     python-simplejson
Recommends:     python-tornado
Suggests:       python-paramiko
%endif
%python_subpackages

%description
PyZMQ is a lightweight and super-fast messaging library built on top of
the ZeroMQ library (http://www.zeromq.org).

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       python-base
Requires:       python-devel
Requires:       zeromq-devel

%description devel
Development libraries and headers needed to build software using %{name}.

%prep
%autosetup -n pyzmq-%{version} -p1

# Fix non-executable script rpmlint warning:
find examples zmq -name "*.py" -exec sed -i "s|#\!\/usr\/bin\/env python||" {} \;

%build
# See https://github.com/zeromq/pyzmq/blob/master/setup.cfg.template
echo '
[global]
skip_check_zmq = False
zmq_prefix = %{_prefix}
no_libzmq_extension = True
'>> setup.cfg
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
SKIPPED_TESTS+=" or test_null"
%endif
mkdir cleantest
pushd cleantest
%pytest_arch --pyargs zmq -k "not (${SKIPPED_TESTS:4})" --timeout 1200
popd
%endif

%files %{python_files}
%license COPYING.BSD COPYING.LESSER
%doc AUTHORS.md README.md examples
%{python_sitearch}/zmq/
%{python_sitearch}/pyzmq-%{version}-py*.egg-info
%exclude %{python_sitearch}/zmq/utils/*.h
%exclude %{python_sitearch}/zmq/backend/cffi/_cdefs.h

%files %{python_files devel}
%{python_sitearch}/zmq/utils/*.h
%{python_sitearch}/zmq/backend/cffi/_cdefs.h

%changelog
