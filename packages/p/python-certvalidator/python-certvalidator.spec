#
# spec file for package python-certvalidator
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


%{?sle15_python_module_pythons}

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-certvalidator%{psuffix}
Version:        0.11.1
Release:        0
Summary:        X.509 certificates validation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wbond/certvalidator
Source:         https://github.com/wbond/certvalidator/archive/%{version}.tar.gz#/certvalidator-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module asn1crypto >= 0.18.1}
BuildRequires:  %{python_module oscrypto >= 0.16.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
%endif
BuildArch:      noarch
Requires:       python-asn1crypto >= 0.18.1
Requires:       python-oscrypto >= 0.16.1
%python_subpackages

%description
A Python library for validating X.509 certificates or paths. Supports various
options, including: validation at a specific moment in time, whitelisting and
revocation checks.

%prep
%autosetup -p1 -n certvalidator-%{version}
# /docs has a different readme.md file - should not overwrite main readme.md
mv readme.md README.md
# Deprecation warnings/errors for unittest.TestCase.assertRaisesRegexp, using 
# unittest.TestCase.assertRaisesRegex instead
sed -i 's/assertRaisesRegexp/assertRaisesRegex/g' tests/test_validate.py

%build
%pyproject_wheel

%if %{with test}
%check
# Disable tests that need network connection 
donttest="test_fetch_crl or test_fetch_ocsp"
# Disable tests with error "PathValidationError: The path could not be 
# validated because intermediate certificate 1 expired 2022-04-13 10:00:00Z"
donttest+=" or test_revocation_mode_hard or test_revocation_mode_soft"
# Failing tests related to issue https://github.com/wbond/certvalidator/issues/45
donttest+=" or test_basic_certificate_validator_tls or test_build_paths"
%pytest -k "not ($donttest)"
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md changelog.md docs/*
%{python_sitelib}/certvalidator
%{python_sitelib}/certvalidator-%{version}*-info
%endif

%changelog
