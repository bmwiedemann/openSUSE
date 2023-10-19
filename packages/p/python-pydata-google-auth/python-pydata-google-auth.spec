#
# spec file for package python-pydata-google-auth
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-pydata-google-auth
Version:        1.8.2
Release:        0
Summary:        PyData helpers for authenticating to Google APIs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pydata/pydata-google-auth
Source:         https://github.com/pydata/pydata-google-auth/archive/%{version}.tar.gz#/pydata-google-auth-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/pydata/pydata-google-auth/pull/73 Do not require six on Python 3
Patch0:         no-six.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 1.25.1
Requires:       python-google-auth-oauthlib >= 0.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module google-auth >= 1.25.0}
BuildRequires:  %{python_module google-auth-oauthlib >= 0.4.0}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PyData-Google-Auth is a package providing helpers for authenticating
to Google APIs.

%prep
%autosetup -p1 -n pydata-google-auth-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/pydata_google_auth
%{python_sitelib}/pydata_google_auth-%{version}*-info

%changelog
