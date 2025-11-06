#
# spec file for package python-webauthn
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-webauthn
Version:        2.7.0
Release:        0
Summary:        Pythonic WebAuthn
License:        BSD-3-Clause
URL:            https://github.com/duo-labs/py_webauthn
Source:         https://github.com/duo-labs/py_webauthn/archive/refs/tags/v%{version}.tar.gz#/webauthn-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module asn1crypto >= 1.5.1}
BuildRequires:  %{python_module cbor2 >= 5.6.2}
BuildRequires:  %{python_module cryptography >= 44.0.2}
BuildRequires:  %{python_module pyOpenSSL >= 25.0.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-asn1crypto >= 1.5.1
Requires:       python-cbor2 >= 5.6.2
Requires:       python-cryptography >= 44.0.2
Requires:       python-pyOpenSSL >= 25.0.0
BuildArch:      noarch
%python_subpackages

%description
Pythonic WebAuthn

%prep
%autosetup -p1 -n py_webauthn-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/webauthn
%{python_sitelib}/webauthn-%{version}.dist-info

%changelog
