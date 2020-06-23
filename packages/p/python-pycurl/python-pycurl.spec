#
# spec file for package python-pycurl
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pycurl%{psuffix}
Version:        7.43.0.5
Release:        0
Summary:        PycURL -- cURL library module
License:        LGPL-2.1-or-later AND MIT
URL:            http://pycurl.io/
Source:         https://files.pythonhosted.org/packages/source/p/pycurl/pycurl-%{version}.tar.gz
# PATCH-FIX-OPENSUSE increase_test_timeout.diff -- Increase the timeout in a test so it doesn't fail when obs is overloaded
Patch0:         increase_test_timeout.diff
# PATCH-FIX-UPSTREAM handle difference between libssh and libssh2
Patch1:         pycurl-libssh.patch
# PATCH-FIX-OPENSUSE python-pycurl-7.43.0-tls-backend.patch -- do not run runtime tests to compare linked libs
Patch2:         python-pycurl-7.43.0-tls-backend.patch
Patch3:         disable_randomly_failing_tests.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libcurl) >= 7.19.0
BuildRequires:  pkgconfig(openssl)
%if %{with test}
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module nose}
%endif
%ifpython2
Provides:       %{oldpython}-curl = %{version}
Obsoletes:      %{oldpython}-curl < %{version}
%endif
%python_subpackages

%description
This module provides bindings for the cURL library.

%package -n %{name}-doc
Summary:        Documentation for python-curl
Provides:       %{python_module pycurl-doc = %{version}}
BuildArch:      noarch

%description -n %{name}-doc
This module provides bindings for the cURL library.

This package contains documentation and examples.

%prep
%setup -q -n pycurl-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export PYCURL_SSL_LIBRARY=openssl
%python_build --with-openssl

%install
export PYCURL_SSL_LIBRARY=openssl
%python_install --with-openssl

rm -rf %{buildroot}%{_datadir}/doc # Remove wrongly installed junk

%{python_expand \
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}
$python -O -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%if %{with test}
export LANG=en_US.UTF-8
export PYCURL_SSL_LIBRARY=openssl
# taken from "make test" because we only need to run nosetests,
# not the rest of the mess in the upstream runner
pushd tests/fake-curl/libcurl
rm -f *.so
make %{?_smp_mflags}
popd
# exclude certain tests
test_flags='!online,!occasionally_failing'
if ! pkg-config --variable=supported_features libcurl|grep -qw HTTP2; then
    test_flags="$test_flags,\!http2"
fi
if ! pkg-config --variable=supported_protocols libcurl|grep -qw SCP; then
    test_flags="$test_flags,\!ssh"
fi
# test_getinfo are failing with new bottle
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} \
nosetests-%{$python_bin_suffix} -v --with-flaky -a "$test_flags" -e 'test_getinfo'
}
rm -rf %{buildroot}%{_prefix}/lib/debug %{buildroot}%{_libdir}/python*
%endif # test

%if ! %{with test}
%files %{python_files}
%license COPYING-LGPL COPYING-MIT
%doc AUTHORS ChangeLog README.rst
%{python_sitearch}/*

%files -n %{name}-doc
%doc examples doc/*.rst
%endif

%changelog
