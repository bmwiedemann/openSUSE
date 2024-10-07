#
# spec file for package python-pycognito
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
Name:           python-pycognito%{psuffix}
Version:        2024.5.1
Release:        0
Summary:        Python class to integrate Boto3's Cognito client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pvizeli/pycognito
Source:         https://files.pythonhosted.org/packages/source/p/pycognito/pycognito-%{version}.tar.gz
Source1:        https://github.com/NabuCasa/pycognito/raw/refs/tags/%{version}/tests.py
Source99:       python-pycognito.rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 2.8.0
Requires:       python-boto3 >= 1.10.49
# cryptography requirement comes from pyjwt[crypto]
Requires:       python-cryptography >= 3.4.0
Requires:       python-envs >= 1.3
Requires:       python-requests >= 2.22.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module freezegun >= 1.5.1}
BuildRequires:  %{python_module joserfc}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module pycognito = %{version}}
BuildRequires:  %{python_module pytest >= 8.2.1}
BuildRequires:  %{python_module requests-mock >= 1.12.1}
%endif
%python_subpackages

%description
Python class to integrate Boto3's Cognito client so it is easy to login users. With SRP support.

%prep
%autosetup -p1 -n pycognito-%{version}
cp %{SOURCE1} ./

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
donttest="test_srp_requests_http_auth"
%pytest -k "not ($donttest)" tests.py
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pycognito
%{python_sitelib}/pycognito-%{version}.dist-info
%endif

%changelog
