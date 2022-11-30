#
# spec file for package python-google-api-python-client
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-google-api-python-client
Version:        2.66.0
Release:        0
Summary:        Google APIs Python Client
License:        Apache-2.0
URL:            https://github.com/google/google-api-python-client
Source:         https://files.pythonhosted.org/packages/source/g/google-api-python-client/google-api-python-client-%{version}.tar.gz
# PATCH-FIX-OPENSUSE opensuse-remove-oauth2client-tests.patch -- upstream wants to support and test deprecated oauth2client indefinitely, but
# the distro has to remove it at some point
Patch0:         opensuse-remove-oauth2client-tests.patch
BuildRequires:  %{python_module google-api-core >= 1.31.5}
BuildRequires:  %{python_module google-auth >= 1.19.0}
BuildRequires:  %{python_module google-auth-httplib2 >= 0.1.0}
BuildRequires:  %{python_module httplib2 >= 0.15.0}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module uritemplate  >= 3.0.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.31.5
Requires:       python-google-auth >= 1.19.0
Requires:       python-google-auth-httplib2 >= 0.1.0
Requires:       python-httplib2 >= 0.15.0
Requires:       python-uritemplate >= 3.0.1
# Package renamed in SLE 12, do not remove Provides, Obsolete directives
# until after SLE 12 EOL
Provides:       google-api-python-client = %{version}
Obsoletes:      google-api-python-client < %{version}
BuildArch:      noarch
%python_subpackages

%description
Google APIs Client Library for Python

%prep
%autosetup -p1 -n google-api-python-client-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# DiscoveryErrors::test_credentials_and_credentials_file_mutually_exclusive fails with "socket.gaierror: [Errno -3] Temporary failure in name resolution"
donttest="test_credentials_and_credentials_file_mutually_exclusive"
# don't test deprecated oaut2client usage
donttest="$donttest or TestAuthWithOAuth2Client or test_oauth2client_crendentials"
# test_http.py uses mocked Credentials class and API from deprecated oauth2client
%pytest --ignore=samples --ignore tests/test_http.py -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/apiclient
%{python_sitelib}/googleapiclient
%{python_sitelib}/google_api_python_client-%{version}*-info

%changelog
