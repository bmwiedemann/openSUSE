#
# spec file for package python-asn1crypto
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-asn1crypto
Version:        1.0.0
Release:        0
Summary:        ASN.1 parser and serializer for Python
License:        MIT
URL:            https://github.com/wbond/asn1crypto
Source:         https://github.com/wbond/asn1crypto/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
ASN.1 parser and serializer with definitions for private keys, public keys,
certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X509 and TSP

%prep
%setup -q -n asn1crypto-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
