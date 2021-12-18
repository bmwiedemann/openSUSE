#
# spec file for package python-tornado5
#
# Copyright (c) 2021 SUSE LLC
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
%define         oldpython python
%define         skip_python310 1
%bcond_without python2
Name:           python-tornado5
Version:        5.1.1
Release:        0
Summary:        Open source version of scalable, non-blocking web server that power FriendFeed
License:        Apache-2.0
URL:            http://www.tornadoweb.org
Source:         https://files.pythonhosted.org/packages/source/t/tornado/tornado-%{version}.tar.gz
Source99:       python-tornado5-rpmlintrc
Patch1:         tornado-testsuite_timeout.patch
Patch2:         openssl-cert-size.patch
Patch3:         skip-failing-tests.patch
Patch4:         py38-0001-test-silence-deprecation-warning.patch
Patch5:         py38-0002-dont-log-CancelledError.patch
Patch6:         py2-dont-log-cryptographywarning.patch
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pycurl}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplejson}
%if 0%{?suse_version} >= 1550
BuildRequires:  %{python_module pycares}
%else
BuildRequires:  python3-pycares
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-simplejson
Conflicts:      python-tornado-impl
Provides:       python-tornado = %{version}
Provides:       python-tornado-impl = %{version}
Provides:       python-toro = %{version}
Obsoletes:      python-toro < %{version}
%ifpython2
Provides:       %{oldpython}-tornado = %{version}
%endif
%if 0%{?suse_version} || 0%{?fedora_version} || 0%{?rhel} >= 8
Recommends:     python-Twisted
Recommends:     python-pycares
Recommends:     python-pycurl
Recommends:     python-service_identity
%endif
%if %{with python2}
BuildRequires:  python-backports_abc
BuildRequires:  python-futures
BuildRequires:  python-mock
BuildRequires:  python-service_identity
BuildRequires:  python-singledispatch
%endif
%if %{python3_version_nodots} < 35
BuildRequires:  python3-backports_abc
%endif
%if %{python_version_nodots} < 35
Requires:       python-backports_abc
%endif
%ifpython2
Requires:       python-futures
Requires:       python-singledispatch
Provides:       %{oldpython}-tornado = %{version}
%endif
%python_subpackages

%description
Tornado is an open source version of the scalable, non-blocking web server and
tools that power FriendFeed. The FriendFeed application is written using a web
framework that looks a bit like web.py or Google's webapp, but with additional
tools and optimizations to take advantage of the underlying non-blocking
infrastructure.

The framework is distinct from most mainstream web server frameworks (and
certainly most Python frameworks) because it is non-blocking and reasonably
fast. Because it is non-blocking and uses epoll, it can handle thousands of
simultaneous standing connections, which means it is ideal for real-time web
services. We built the web server specifically to handle FriendFeed's real-time
features — every active user of FriendFeed maintains an open connection to the
FriendFeed servers. (For more information on scaling servers to support
thousands of clients, see The C10K problem.)

%prep
%setup -q -n tornado-%{version}
# Fix non-executable script rpmlint issue:
find demos tornado -name "*.py" -exec sed -i "/#\!\/usr\/bin\/.*/d" {} \;
%autopatch -p1

%pre
# remove egg-info _file_, being replaced by an egg-info directory
if [ -f %{python_sitearch}/tornado-%{version}-py%{python_version}.egg-info ]; then
    rm %{python_sitearch}/tornado-%{version}-py%{python_version}.egg-info
fi

%build
%python_build

%install
%python_install
%{python_expand #
rm -r %{buildroot}%{$python_sitearch}/tornado/test
%fdupes %{buildroot}%{$python_sitearch}
pdocdir=%{buildroot}%{_docdir}/%{$python_prefix}-tornado5
mkdir -p ${pdocdir}
cp -r demos ${pdocdir}/
find ${pdocdir} -type f -exec chmod a-x '{}' ';'
%fdupes ${pdocdir}
}

%check
export ASYNC_TEST_TIMEOUT=30
export TRAVIS=1
%{python_expand # merge the compiled sitearch and the test directory into testenv dir
mkdir testenv-%{$python_bin_suffix}
pushd testenv-%{$python_bin_suffix}
cp -r %{buildroot}%{$python_sitearch}/tornado ./
cp -r ../tornado/test tornado/
$python -Bm tornado.test.runtests --verbose
popd
}

%files %{python_files}
%license LICENSE
%doc README.rst
%doc %{_docdir}/%{python_prefix}-tornado5/demos/
%{python_sitearch}/tornado/
%{python_sitearch}/tornado-%{version}-py*.egg-info

%changelog
