#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-urllib3%{psuffix}
Version:        1.26.13
Release:        0
Summary:        HTTP library with thread-safe connection pooling, file post, and more
License:        MIT
Group:          Development/Languages/Python
URL:            https://urllib3.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/u/urllib3/urllib3-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove_mock.patch gh#urllib3/urllib3#2108 mcepl@suse.com
# remove dependency on the external module mock
Patch0:         remove_mock.patch
BuildRequires:  %{python_module base >= 3.7}
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
Recommends:     python-Brotli >= 1.0.9
Recommends:     python-PySocks >= 1.5.6
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Brotli >= 1.0.9}
BuildRequires:  %{python_module PySocks >= 1.5.6}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cryptography >= 1.3.4}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module idna >= 2.0.0}
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

%{python_expand # Unbundle six
rm %{buildroot}/%{$python_sitelib}/urllib3/packages/six.py
rm %{buildroot}/%{$python_sitelib}/urllib3/packages/__pycache__/six*.pyc

ln -s %{$python_sitelib}/six.py %{buildroot}/%{$python_sitelib}/urllib3/packages/six.py
ln -sf %{$python_sitelib}/__pycache__/six.cpython-%{$python_version_nodots}.opt-1.pyc \
       %{buildroot}/%{$python_sitelib}/urllib3/packages/__pycache__/
ln -sf %{$python_sitelib}/__pycache__/six.cpython-%{$python_version_nodots}.pyc \
       %{buildroot}/%{$python_sitelib}/urllib3/packages/__pycache__/

%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%if %{with test}
%check
# gh#urllib3/urllib3#2109
export CI="true"
# skip some randomly failing tests (mostly on i586, but sometimes they fail on other architectures)
skiplist="test_ssl_read_timeout or test_ssl_failed_fingerprint_verification or test_ssl_custom_validation_failure_terminates"
# gh#urllib3/urllib3#1752 and others: upstream's way of checking that the build
# system has a correct system time breaks (re-)building the package after too
# many months have passed since the last release.
skiplist+=" or test_recent_date"
# too slow to run in obs (checks 2GiB of data)
skiplist+=" or test_requesting_large_resources_via_ssl"
%pytest -k "not (${skiplist})"
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitelib}/urllib3
%{python_sitelib}/urllib3-%{version}*-info
%endif

%changelog
