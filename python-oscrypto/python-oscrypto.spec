#
# spec file for package python-oscrypto
#
# Copyright (c) 2019 cunix
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

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-oscrypto%{psuffix}
Version:        0.19.1
Release:        0
Summary:        Python crypto using OS libraries
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wbond/oscrypto
Source:         https://github.com/wbond/oscrypto/archive/%{version}.tar.gz#/oscrypto-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module asn1crypto >= 0.22.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
# needed for TrustListTests to succeed
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
%endif
BuildArch:      noarch
Requires:       python-asn1crypto >= 0.22.0
%python_subpackages

%description
TLS (SSL) sockets, key generation, encryption, decryption, signing, verification
and KDFs using the OS crypto libraries. Does not require a compiler, and relies
on the OS for patching. Works on Windows, OS X and Linux/BSD.

%prep
%setup -q -n oscrypto-%{version}
# /docs has a different readme.md file - should not overwrite main readme.md
mv readme.md README.md

%build
%python_build

%if %{with test}
%check
# TLSTests need network connectivity -> diabled with regular expression
%python_exec run.py tests ^\(\?\!test_tls\)
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md changelog.md docs/*
%{python_sitelib}/*
%endif

%changelog
