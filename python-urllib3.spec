#
# spec file for package python-urllib3
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
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-urllib3%{psuffix}
Version:        1.26.2
Release:        0
Summary:        HTTP library with thread-safe connection pooling, file post, and more
License:        MIT
Group:          Development/Languages/Python
URL:            https://urllib3.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/u/urllib3/urllib3-%{version}.tar.gz
# Wrapper for ssl to unbundle ssl_match_hostname
Source1:        ssl_match_hostname_py3.py
# PATCH-FIX-UPSTREAM remove_mock.patch gh#urllib3/urllib3#2108 mcepl@suse.com
# remove dependency on the external module mock
Patch0:         remove_mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#!BuildIgnore:  python-requests
Requires:       ca-certificates-mozilla
Requires:       python-certifi
Requires:       python-cryptography >= 1.3.4
Requires:       python-idna >= 2.0.0
Requires:       python-pyOpenSSL >= 0.14
Requires:       python-six >= 1.12.0
Recommends:     python-PySocks >= 1.5.6
Recommends:     python-brotlipy >= 0.6.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PySocks >= 1.5.6}
BuildRequires:  %{python_module brotlipy >= 0.6.0}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cryptography >= 1.3.4}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module idna >= 2.0.0}
BuildRequires:  %{python_module mock >= 1.3.0}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-freezegun}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module tornado >= 6}
BuildRequires:  %{python_module trustme >= 0.5.3}
BuildRequires:  %{python_module urllib3 >= %{version}}
%endif
%python_subpackages

%description
Highlights

- Re-use the same socket connection for multiple requests
  (HTTPConnectionPool and HTTPSConnectionPool)
  (with optional client-side certificate verification).
- File posting (encode_multipart_formdata).
- Built-in redirection and retries (optional).
- Supports gzip and deflate decoding.
- Thread-safe and sanity-safe.
- Works with AppEngine, gevent, and eventlib.
- Tested on Python 2.6+ and Python 3.3+, 100% unit test coverage.
- Small and easy to understand codebase perfect for extending and building upon.
  For a more comprehensive solution, have a look at
  Requests which is also powered by urllib3.

%prep
%autosetup -p1 -n urllib3-%{version}

find . -type f -exec chmod a-x '{}' \;
find . -name __pycache__ -type d -exec rm -fr {} +

# Drop the dummyserver tests, they fail in OBS
rm test/with_dummyserver/test_proxy_poolmanager.py
rm test/with_dummyserver/test_poolmanager.py
# Don't run the Google App Engine tests
rm -r test/appengine/

%build
%python_build

%install
%if !%{with test}
%python_install

# Unbundle the Python 3 build
rm %{buildroot}/%{python3_sitelib}/urllib3/packages/six.py
rm -r %{buildroot}/%{python3_sitelib}/urllib3/packages/ssl_match_hostname/

# Copy ssl_match_hostname.py before compilation, so we can have a pyc too
cp -a %{SOURCE1} %{buildroot}/%{python3_sitelib}/urllib3/packages/ssl_match_hostname.py

%{python_expand \
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/urllib3/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/urllib3/
}

ln -s %{python3_sitelib}/six.py %{buildroot}/%{python3_sitelib}/urllib3/packages/six.py
ln -sf %{python3_sitelib}/__pycache__/six.cpython-%{python3_version_nodots}.opt-1.pyc \
       %{buildroot}/%{python3_sitelib}/urllib3/packages/__pycache__/
ln -sf %{python3_sitelib}/__pycache__/six.cpython-%{python3_version_nodots}.pyc \
       %{buildroot}/%{python3_sitelib}/urllib3/packages/__pycache__/

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# gh#urllib3/urllib3#2109
export CI="true"
# still broken with new ssl
skiplist='test_import_urllib3'
# skip some randomly failing tests (mostly on i586, but sometimes they fail on other architectures)
skiplist+=" or test_ssl_read_timeout or test_ssl_failed_fingerprint_verification or test_ssl_custom_validation_failure_terminates"
# gh#urllib3/urllib3#1752 and others: upstream's way of checking that the build
# system has a correct system time breaks (re-)building the package after too
# many months have passed since the last release.
skiplist+=" or test_recent_date"
%pytest -k "not (${skiplist})"
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%{python_sitelib}/urllib3
%{python_sitelib}/urllib3-%{version}-py*.egg-info
%endif

%changelog
