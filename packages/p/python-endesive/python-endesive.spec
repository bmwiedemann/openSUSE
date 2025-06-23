#
# spec file for package python-endesive
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


%{?sle15_python_module_pythons}
Name:           python-endesive
Version:        2.18.5
Release:        0
Summary:        Library for digital signing and verification of digital signatures
License:        MIT
URL:            https://github.com/m32/endesive
Source:         https://github.com/m32/endesive/archive/refs/tags/v%{version}.tar.gz#/endesive-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyKCS11}
BuildRequires:  %{python_module asn1crypto}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module certvalidator}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  openssh
BuildRequires:  openssl
BuildRequires:  softhsm
# /SECTION
BuildRequires:  fdupes
Requires:       python-Pillow
Requires:       python-PyKCS11
Requires:       python-asn1crypto
Requires:       python-attrs
Requires:       python-certvalidator
Requires:       python-cryptography
Requires:       python-lxml
Requires:       python-paramiko
Requires:       python-pytz
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Library for digital signing and verification of digital signatures in mail, PDF and XML documents.

%prep
%setup -q -n endesive-%{version}
# Set correct path to find the softhsm library, needed for test_create and test_load
sed -i 's|softhsm/libsofthsm2.so|pkcs11/libsofthsm2.so|g' tests/test_hsm.py
find . -name "*.py" -exec sed -i '/\/usr\/bin\/env.*python.*/d' {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Manually start ssh agent, needed to run test_ssh_sign and test_ssh_verify
eval $(ssh-agent)
export PYTHONPATH='tests'
# Deselect tests that require, respectively, font installation and network connection
donttest="test_pdf_signature_manual or test_pdf_timestamp"
# ... or cause the interpreter to segfault
donttest+=" or test_email_signed_attr or test_pdf or test_plain_ssl_noattr"
donttest+=" or test_plain_ssl_attr"
%pytest -k "not ($donttest)"
ssh-agent -k

%files %{python_files}
%doc README.rst changelog.md
%license LICENSE LICENSE.pdf-annotate LICENSE.pyfpdf LICENSE.pypdf2
%{python_sitelib}/endesive
%{python_sitelib}/endesive-%{version}.dist-info

%changelog
