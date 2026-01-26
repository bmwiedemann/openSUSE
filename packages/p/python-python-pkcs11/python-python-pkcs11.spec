#
# spec file for package python-python-pkcs11
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-python-pkcs11
Version:        0.9.3
Release:        0
Summary:        PKCS#11 (Cryptoki) support for Python
License:        MIT
URL:            https://github.com/pyauth/python-pkcs11
Source:         https://files.pythonhosted.org/packages/source/p/python-pkcs11/python_pkcs11-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module oscrypto}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 18.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
BuildRequires:  softhsm
# SECTION test requirements
BuildRequires:  %{python_module asn1crypto}
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-asn1crypto
Requires:       python-cached-property
%python_subpackages

%description
PKCS#11 (Cryptoki) support for Python

%prep
%autosetup -p1 -n python_pkcs11-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
tmpdir=$(mktemp -d)
echo "directories.tokendir = $tmpdir" > /tmp/softhsm2.conf
export SOFTHSM2_CONF=/tmp/softhsm2.conf
export PKCS11_MODULE=%{_libdir}/softhsm/libsofthsm.so
export PKCS11_TOKEN_LABEL=TEST
export PKCS11_TOKEN_PIN=1234
export PKCS11_TOKEN_SO_PIN=5678
softhsm2-util --init-token --free --label $PKCS11_TOKEN_LABEL --pin $PKCS11_TOKEN_PIN --so-pin $PKCS11_TOKEN_SO_PIN
mv pkcs11 pkcs11-do-not-import
%pytest_arch -k 'not test_derive_key'
mv pkcs11-do-not-import pkcs11

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/pkcs11
%{python_sitearch}/python_pkcs11-%{version}.dist-info

%changelog
