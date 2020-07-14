#
# spec file for package python-pydata-google-auth
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
%bcond_without python2
Name:           python-pydata-google-auth
Version:        1.1.0
Release:        0
Summary:        PyData helpers for authenticating to Google APIs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pydata/pydata-google-auth
Source:         https://github.com/pydata/pydata-google-auth/archive/%{version}.tar.gz#/pydata-google-auth-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module google-auth-oauthlib}
BuildRequires:  %{python_module google-auth}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python-mock
%endif
# /SECTION
Requires:       python-google-auth
Requires:       python-google-auth-oauthlib
BuildArch:      noarch

%python_subpackages

%description
PyData-Google-Auth is a package providing helpers for authenticating
to Google APIs.

%prep
%setup -q -n pydata-google-auth-%{version}

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
%{python_sitelib}/*

%changelog
