#
# spec file for package python-gevent
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


# on TW, gevent is able to use system libev, Leaps et.al. need the bundled version
%if 0%{?suse_version} <= 1500
%define use_bundled_libev 1
%else
%define use_bundled_libev 0
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modversion 20.9.0
%define modname gevent
Name:           python-gevent
Version:        20.9.0
Release:        0
Summary:        Python network library that uses greenlet and libevent
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.gevent.org/
# Source:         https://files.pythonhosted.org/packages/source/g/gevent/gevent-%%{version}.tar.gz
Source0:        https://github.com/gevent/%{modname}/archive/%{modversion}.tar.gz#/%{modname}-%{modversion}.tar.gz
Source100:      %{name}-rpmlintrc
# gcc7 for 15.1 produces no-return-in-nonvoid-function, but the same compiler for 15.2 not
# usually, as long as no return value is used, this shouldn't be treated as an error
# let's selectively disable the warning around the offending code
Patch0:         fix-no-return-in-nonvoid-function.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module greenlet >= 0.4.17}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module objgraph}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.event}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
# /etc/protocols needed for tests
BuildRequires:  netcfg
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-testsuite
BuildRequires:  pkgconfig(libcares)
%if ! 0%{use_bundled_libev}
BuildRequires:  pkgconfig(libev)
%endif
BuildRequires:  pkgconfig(libuv)
Requires:       python-cffi
Requires:       python-dnspython
Requires:       python-greenlet
Requires:       python-requests
Requires:       python-zope.event
Requires:       python-zope.interface
%if 0%{?suse_version} || 0%{?fedora_version} ||  0%{?rhel} >= 8
Recommends:     python-psutil
%else
Requires:       python-psutil
%endif
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

%package -n python-gevent-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module gevent-doc = %{version}}
BuildArch:      noarch

%description -n python-gevent-doc
Documentation and examples for %{name}.

%prep
%setup -q -n gevent-%{modversion}
%if 0%{?sle_version} <= 150100 && 0%{?is_opensuse}
%patch0 -p1
%endif
sed -i -e '1s!bin/env python!bin/python!' examples/*.py

%build
export LIBEV_EMBED=%{use_bundled_libev}
export CARES_EMBED=0
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
export LIBEV_EMBED=%{use_bundled_libev}
export CARES_EMBED=0
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# create ignore list of tests that reach out to the net
cat << EOF > network_tests.txt
test__core_stat.py
%if 0%{?sle_version} <= 150200 && 0%{?is_opensuse}
test__destroy_default_loop.py
test__example_echoserver.py
test_socket.py
%endif
%if %{python3_version_nodots} < 37
test__threading_2.py
%endif
test__examples.py
# this one fails occasionally with: Address already in use: ('127.0.0.1', 16000)
test__example_portforwarder.py
test__getaddrinfo_import.py
test__resolver_dnspython.py
test__socket_dns.py
EOF
export GEVENT_RESOLVER=thread
# Setting the TRAVIS environment variable makes some different configuration
# for tests that use the network so they don't fail on travis (or obs)
export TRAVIS=1
# Setting the APPVEYOR environment variable makes the tests use a workaround
# for Appveyor that we also need in obs for "wait_threads() failed to cleanup 1 threads"
export APPVEYOR=1
export LANG=en_US.UTF-8
# don't bother with python2 tests
%{python_expand if [ "$python" != "python2" ]; then
    PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m gevent.tests --ignore network_tests.txt
fi
}

%files %{python_files}
%doc AUTHORS README.rst TODO CHANGES.rst CONTRIBUTING.rst
%license LICENSE*
%{python_sitearch}/gevent-%{modversion}-py*.egg-info
%{python_sitearch}/gevent/

%files -n python-gevent-doc
%license LICENSE*
%doc examples/

%changelog
