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


# DON'T USE FOR SLE, USES BUNDLED VERSION OF LIBEV!!!
%define use_bundled_libev 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modversion 1.5a3
%define modname gevent
Name:           python-gevent
Version:        1.5.0~a3
Release:        0
Summary:        Python network library that uses greenlet and libevent
License:        MIT
Group:          Development/Languages/Python
URL:            http://www.gevent.org/
# Source:         https://files.pythonhosted.org/packages/source/g/gevent/gevent-%%{version}.tar.gz
Source0:        https://github.com/gevent/%{modname}/archive/%{modversion}.tar.gz#/%{modname}-%{modversion}.tar.gz
Source100:      %{name}-rpmlintrc
Patch1:         fix-tests.patch
Patch2:         use-libev-cffi.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module greenlet >= 0.4.14}
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
%if 0%{?use_bundled_libev}
BuildRequires:  pkgconfig(libev)
%endif
BuildRequires:  pkgconfig(libuv)
Requires:       python-cffi
Requires:       python-dnspython
Requires:       python-greenlet
Requires:       python-requests
%if 0%{?suse_version} || 0%{?fedora_version} ||  0%{?rhel} >= 8
Recommends:     python-psutil
Recommends:     python-zope.event
%else
Requires:       python-psutil
Requires:       python-zope.event
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
%patch1 -p1
%patch2 -p1
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
# test_ssl.py is fragile as it expect specific responses from ssl and
#  does not account to our local changes
# Also, gh#gevent/gevent#1390
# Also, gh#gevent/gevent#1501
# Test threading problems may be problem of bpo#36402, which has been
# fixed in 3.7.5.
cat <<'EOF' >> network_tests.txt
test__all__.py
test___config.py
test__doctests.py
test__examples.py
test__execmodules.py
test__getaddrinfo_import.py
test_httplib.py
test__socket_dns.py
test_socket.py
test__socket_ssl.py
test__ssl.py
test_ssl.py
test_threading.py
test_urllib2_localnet.py
test_urllib2net.py
test_wsgiref.py
EOF
export GEVENT_RESOLVER=thread
# Setting the TRAVIS environment variable makes some different configuration
# for tests that use the network so they don't fail on travis (or obs)
export TRAVIS=1
# Setting the APPVEYOR environment variable makes the tests use a workaround
# for Appveyor that we also need in obs for "wait_threads() failed to cleanup 1 threads"
export APPVEYOR=1
export LANG=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m gevent.tests --ignore network_tests.txt

%files %{python_files}
%doc AUTHORS README.rst TODO CHANGES.rst CONTRIBUTING.rst
%license LICENSE*
%{python_sitearch}/gevent-%{modversion}-py*.egg-info
%{python_sitearch}/gevent/

%files -n python-gevent-doc
%license LICENSE*
%doc examples/

%changelog
