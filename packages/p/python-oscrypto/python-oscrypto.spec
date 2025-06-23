#
# spec file for package python-oscrypto
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-oscrypto%{psuffix}
Version:        1.3.0
Release:        0
Summary:        Python crypto using OS libraries
License:        MIT
URL:            https://github.com/wbond/oscrypto
Source:         https://github.com/wbond/oscrypto/archive/%{version}.tar.gz#/oscrypto-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python312.patch gh#wbond/oscrypto#77
Patch0:         python312.patch
BuildRequires:  %{python_module asn1crypto >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
# needed for TrustListTests to succeed
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
%endif
BuildArch:      noarch
Requires:       python-asn1crypto >= 1.0.0
%python_subpackages

%description
TLS (SSL) sockets, key generation, encryption, decryption, signing, verification
and KDFs using the OS crypto libraries. Does not require a compiler, and relies
on the OS for patching. Works on Windows, OS X and Linux/BSD.

%prep
%autosetup -p1 -n oscrypto-%{version}
# /docs has a different readme.md file - should not overwrite main readme.md
mv docs/readme.md docs/docs_readme.md

%build
%pyproject_wheel

%if %{with test}
%check
# TLSTests need network connectivity -> diabled with regular expression
%python_exec run.py tests ^\(\?\!test_tls\)
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc readme.md changelog.md docs/*
%{python_sitelib}/oscrypto
%{python_sitelib}/oscrypto-%{version}.dist-info
%endif

%changelog
