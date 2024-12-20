#
# spec file for package python-asn1crypto
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
Name:           python-asn1crypto
Version:        1.5.1
Release:        0
Summary:        ASN.1 parser and serializer for Python
License:        MIT
URL:            https://github.com/wbond/asn1crypto
Source:         https://github.com/wbond/asn1crypto/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM support-python312.patch gh#wbond/asn1crypto@32b67e3caf25, gh#wbond/asn1crypto@8ec764d3914e
Patch1:         support-python312.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
ASN.1 parser and serializer with definitions for private keys,
public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7,
PKCS#8, PKCS#12, PKCS#5, X509 and TSP

%prep
%autosetup -p1 -n asn1crypto-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%{python_sitelib}/asn1crypto
%{python_sitelib}/asn1crypto-%{version}*-info

%changelog
