#
# spec file for package python-requests
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
Name:           python-requests%{psuffix}
Version:        2.32.3
Release:        0
Summary:        Python HTTP Library
License:        Apache-2.0
URL:            https://docs.python-requests.org/
Source:         https://files.pythonhosted.org/packages/source/r/requests/requests-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       ca-certificates
Requires:       python
Requires:       python-certifi >= 2017.4.17
Requires:       python-charset-normalizer >= 2.0.0
Requires:       python-idna >= 2.5
Requires:       python-py
Requires:       python-urllib3 >= 1.21.1
BuildArch:      noarch
%if 0%{?_no_weakdeps}
Requires:       ca-certificates-mozilla
Requires:       python-PySocks >= 1.5.6
Requires:       python-cryptography >= 1.3.4
Requires:       python-pyOpenSSL >= 0.14
%else
Recommends:     ca-certificates-mozilla
Recommends:     python-PySocks >= 1.5.6
Recommends:     python-cryptography >= 1.3.4
Recommends:     python-pyOpenSSL >= 0.14
%endif
%if %{with test}
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module PySocks >= 1.5.6}
BuildRequires:  %{python_module charset-normalizer >= 2.0.0}
BuildRequires:  %{python_module idna >= 2.5}
BuildRequires:  %{python_module pytest-httpbin >= 0.0.7}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= %{version}}
BuildRequires:  %{python_module trustme}
%endif
%python_subpackages

%description
Requests is an HTTP library, written in Python, as an alternative
to Python's builtin urllib2 which requires work (even
method overrides) to perform basic tasks.

Features of Requests:
 - GET, HEAD, POST, PUT, DELETE Requests:
   + HTTP Header Request Attachment.
   + Data/Params Request Attachment.
   + Multipart File Uploads.
   + CookieJar Support.
   + Redirection History.
   + Redirection Recursion Urllib Fix.
   + Automatic Decompression of GZipped Content.
   + Unicode URL Support.
 - Authentication:
   + URL + HTTP Auth Registry.

%prep
%autosetup -p1 -n requests-%{version}

# remove 'never' default parameter from digest-auth check
# requires httpbin 0.6.0
sed -i "s#\(httpbin.*\), 'never'#\1#" tests/test_requests.py

%build
%python_build

%install
%if !%{with test}
%python_install
# check that urllib3 is not installed
test ! -e %{buildroot}%{python3_sitelib}/requests/packages/urllib3
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

# NOTE(aplanas) If we do not have the certificates, we some of the
# tests will fail, so for now we only run the tests in openSUSE
%if 0%{?suse_version} && %{with test}
%check
touch Pipfile
# exclude tests connecting to TARPIT
# exclude test_https_warnings as is flaky
%python_exec -m pytest -v tests -k "not (TestTimeout or connect or test_https_warnings or test_pyopenssl_redirect)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc HISTORY.md README.md
%{python_sitelib}/requests/
%{python_sitelib}/requests-*
%endif

%changelog
