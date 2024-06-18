#
# spec file for package python-urllib3
#
# Copyright (c) 2024 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-urllib3%{psuffix}
Version:        2.1.0
Release:        0
Summary:        HTTP library with thread-safe connection pooling, file post, and more
License:        MIT
URL:            https://urllib3.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/u/urllib3/urllib3-%{version}.tar.gz
# PATCH-FIX-OPENSUSE openssl-3.2.patch gh#urllib3/urllib3#3271
Patch1:         openssl-3.2.patch
# PATCH-FIX-UPSTREAM https://github.com/urllib3/urllib3/commit/accff72ecc2f6cf5a76d9570198a93ac7c90270e Strip Proxy-Authorization header on redirects
Patch2:         CVE-2024-37891.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#!BuildIgnore:  python-requests
Requires:       ca-certificates-mozilla
Requires:       python-certifi
Requires:       python-cryptography >= 1.9
Requires:       python-idna >= 3.4
Requires:       python-pyOpenSSL >= 23.2.0
Recommends:     python-Brotli >= 1.0.9
Recommends:     python-PySocks >= 1.7.1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Brotli >= 1.0.9}
BuildRequires:  %{python_module PySocks >= 1.7.1}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cryptography >= 1.9}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module idna >= 3.4}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest >= 7.4.0}
BuildRequires:  %{python_module pytest-timeout >= 2.1.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module tornado >= 6.2}
BuildRequires:  %{python_module trustme >= 0.9.0}
BuildRequires:  %{python_module urllib3 >= %{version}}
BuildRequires:  timezone
%else
Conflicts:      python-urllib3 < 2
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

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}
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
# Try to access external evil.com
skiplist+=" or test_deprecated_no_scheme"
%pytest %{?jobs:-n %jobs} -k "not (${skiplist})" --ignore test/with_dummyserver/test_socketlevel.py
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.md
%{python_sitelib}/urllib3
%{python_sitelib}/urllib3-%{version}*-info
%endif

%changelog
