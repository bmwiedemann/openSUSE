#
# spec file for package python-gevent
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


# on TW, gevent is able to use system libev, Leaps et.al. need the bundled version
%if 0%{?suse_version} <= 1500
%define use_bundled_libev 1
%else
%define use_bundled_libev 0
%endif
# get colored test output on local osc build
%bcond_with colortest
%{?sle15_python_module_pythons}
Name:           python-gevent
Version:        25.9.1
Release:        0
Summary:        Python network library that uses greenlet and libevent
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.gevent.org/
Source0:        https://github.com/gevent/gevent/archive/%{version}.tar.gz#/gevent-%{version}.tar.gz
Source100:      %{name}-rpmlintrc
# PATCH-FEATURE-OPENSUSE gevent-opensuse-nocolor-tests.patch code@bnavigator.de -- Avoid colorization of test output in obs runners
Patch2:         gevent-opensuse-nocolor-tests.patch
BuildRequires:  %{python_module Cython >= 3.0.11}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module greenlet >= 3.2.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.event}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libuv)
Requires:       python-greenlet >= 3.2.2
Requires:       python-zope.event
Requires:       python-zope.interface
%if ! 0%{use_bundled_libev}
BuildRequires:  pkgconfig(libev)
%endif
%if 0%{?suse_version} || 0%{?fedora_version} ||  0%{?rhel} >= 8
Recommends:     python-cffi
Recommends:     python-dnspython
Recommends:     python-psutil
%else
Requires:       python-cffi
Requires:       python-dnspython
Requires:       python-psutil
%endif
# SECTION test requirements
# these are optional but not strict runtime requirements
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module psutil}
# (cffi is already a build requirement)
# these are extra test requirements or recommendations
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module objgraph}
BuildRequires:  %{python_module testsuite}
# (we don't need to check coverage)
# /etc/protocols needed for tests
BuildRequires:  netcfg
# /SECTION
%python_subpackages

%description
Gevent is a Python networking library that uses greenlet to provide synchronous
API on top of a libevent event loop. Features include:

  * Fast event loop based on libevent.
  * Lightweight execution units based on greenlet.
  * Familiar API that re-uses concepts from the Python standard library.
  * Cooperative sockets with ssl support.
  * DNS queries performed through libevent-dns.
  * Ability to use standard library and 3rd party modules written for standard
    blocking sockets
  * Fast WSGI server based on libevent-http.

gevent is inspired by eventlet but features more consistent API, simpler
implementation and better performance. Read why others use gevent and check
out the list of the open source projects based on gevent.

%if 0%{?suse_version} > 1500
%package -n python-gevent-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module gevent-doc = %{version}}
BuildArch:      noarch

%description -n python-gevent-doc
Documentation and examples for %{name}.
%endif

%prep
%autosetup -p1 -n gevent-%{version}
sed -i -e '1s!bin/env python!bin/python!' examples/*.py
sed -i -e '1{/bin.*python/d}' src/gevent/tests/*.py

%build
export LIBEV_EMBED=%{use_bundled_libev}
export CARES_EMBED=0
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
export LIBEV_EMBED=%{use_bundled_libev}
export CARES_EMBED=0
%pyproject_install
%{?python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# https://www.gevent.org/development/running_tests.html
#
# create ignore list of tests, e.g. because they reach out to the net despite -u-network
cat << EOF > skip_tests.txt
test__core_stat.py
# this one fails occasionally with: Address already in use: ('127.0.0.1', 16000)
test__example_portforwarder.py
# no dns resolver in obs
test__getaddrinfo_import.py
test__resolver_dnspython.py
# Flaky tests in s390x architecture
%ifarch s390x
test__util.py
%endif
EOF

export GEVENT_RESOLVER=thread
# Setting the TRAVIS environment variable makes some different configuration
# for tests that use the network so they don't fail on travis (or obs)
export TRAVIS=1
# Setting the APPVEYOR environment variable makes the tests use a workaround
# for Appveyor that we also need in obs for "wait_threads() failed to cleanup 1 threads"
export APPVEYOR=1
export LANG=en_US.UTF-8
# Relax the crypto policies for the test-suite
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=xyz_nonexistent_file
export OPENSSL_CONF=''
# TOLERATING FAILING TEST SUITE (gh#gevent/gevent#2118)
%{!?_with_colortest:export TEST_NOCOLOR=1}
%{python_expand #
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -m gevent.tests \
  --ignore skip_tests.txt \
  -u-network \
  --verbose \
  %{?_smp_mflags} || true
}

%files %{python_files}
%doc AUTHORS README.rst TODO CHANGES.rst CONTRIBUTING.rst
%license LICENSE*
%{python_sitearch}/gevent-%{version}*-info
%{python_sitearch}/gevent

%if 0%{?suse_version} > 1500
%files -n python-gevent-doc
%license LICENSE*
%endif
%doc examples/

%changelog
