#
# spec file for package python-jwcrypto
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


Name:           python-jwcrypto
Version:        1.5.1
Release:        0
Summary:        Python module package implementing JOSE Web standards
License:        LGPL-3.0-only
URL:            https://github.com/latchset/jwcrypto
Source:         https://files.pythonhosted.org/packages/source/j/jwcrypto/jwcrypto-%{version}.tar.gz
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module cryptography >= 3.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Deprecated
Requires:       python-cryptography >= 3.4
BuildArch:      noarch
%python_subpackages

%description
A Python implementation of the JOSE Working Group documents:
RFC 7515 - JSON Web Signature (JWS)
RFC 7516 - JSON Web Encryption (JWE)
RFC 7517 - JSON Web Key (JWK)
RFC 7518 - JSON Web Algorithms (JWA)
RFC 7519 - JSON Web Token (JWT)
RFC 7520 - Examples of Protecting Content Using JSON Object Signing and Encryption (JOSE)

%prep
%setup -q -n jwcrypto-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
rm -rv %{buildroot}%{_datadir}/doc/jwcrypto
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest jwcrypto

%files %{python_files}
%{python_sitelib}/jwcrypto
%{python_sitelib}/jwcrypto-%{version}.dist-info
%license LICENSE
%doc README.md

%changelog
