#
# spec file for package python-eventlet
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
Name:           python-eventlet
Version:        0.26.1
Release:        0
Summary:        Concurrent networking library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            http://eventlet.net
Source:         https://files.pythonhosted.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove_nose.patch gh#eventlet/eventlet#638 mcepl@suse.com
# Removes dependency on nose
Patch0:         remove_nose.patch
# PATCH-FIX-UPSTREAM newdnspython.patch gh#eventlet/eventlet#638 mcepl@suse.com
# patch is from gh#rthalley/dnspython#519
Patch1:         newdnspython.patch
# PATCH-FEATURE-UPSTREAM pr_639.patch gh#eventlet/eventlet#639 jayvdb@gmail.com
Patch2:         pr_639.patch
# Really remove the dependency on nose
Patch3:         remove_nose_part_2.patch
BuildRequires:  %{python_module dnspython >= 1.15.0}
BuildRequires:  %{python_module greenlet >= 0.3}
BuildRequires:  %{python_module monotonic >= 1.4}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
# eventlet parses /etc/protocols which is not available in normal build envs
# Tests
BuildRequires:  sysconfig-netconfig
Requires:       netcfg
Requires:       python-dnspython >= 1.15.0
Requires:       python-greenlet >= 0.3
Requires:       python-monotonic >= 1.4
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
Eventlet is a concurrent networking library for Python that allows
changing how code is run.

It uses epoll or libevent for scalable non-blocking I/O. Coroutines
ensure that the developer uses a blocking style of programming that is similar
to threading, but provide the benefits of non-blocking I/O. The event dispatch
is implicit, which means Eventlet can be used from the Python
interpreter, or as part of a larger application.

%prep
%setup -q -n eventlet-%{version}
%autopatch -p1

sed -i "s|^#!.*||" eventlet/support/greendns.py # Fix non-executable script
# https://github.com/eventlet/eventlet/issues/638
sed -i "/assert num_readers/ i \    return" tests/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# python2 is required to build for Leap, but tests fail (even upstream)
python2_skipall='--collect-only'
# dnspython 1 and 2: backdoor tests fail with "take too long"
skiptests="(BackdoorTest and test_server)"
# fail only with dnspython 2:
skiptests+=" or test_dns_methods_are_green or test_noraise_dns_tcp"

# Unknown openSUSE 15.x specific errors
# TypeError: _wrap_socket() argument 1 must be _socket.socket, not SSLSocket
# https://github.com/rthalley/dnspython/issues/559#issuecomment-675274960
%if %python3_version_nodots == 36
  skiptests+=" or test_connect_ssl or test_ssl_sending_messages or test_wrap_ssl"
  skiptests+=" or ssl_test or wsgi_test"
%endif
# no subdir recursion https://github.com/eventlet/eventlet/issues/638#issuecomment-676085599
%pytest -o norecursedirs="tests/*" -k "not ($skiptests)" ${$python_skipall}

%files %{python_files}
%license LICENSE
%doc AUTHORS NEWS README.rst
%{python_sitelib}/*

%changelog
