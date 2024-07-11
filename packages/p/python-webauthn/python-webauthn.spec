#
# spec file for package python-webauthn
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
Name:           python-webauthn
Version:        2.2.0
Release:        0
Summary:        Pythonic WebAuthn
License:        BSD-3-Clause
URL:            https://github.com/duo-labs/py_webauthn
Source:         https://files.pythonhosted.org/packages/source/w/webauthn/webauthn-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module asn1crypto >= 1.4.0}
BuildRequires:  %{python_module cbor2 >= 5.4.6}
BuildRequires:  %{python_module cryptography >= 41.0.7}
BuildRequires:  %{python_module pyOpenSSL >= 23.3.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-asn1crypto >= 1.4.0
Requires:       python-cbor2 >= 5.4.6
Requires:       python-cryptography >= 41.0.7
Requires:       python-pyOpenSSL >= 23.3.0
BuildArch:      noarch
%python_subpackages

%description
Pythonic WebAuthn

%prep
%autosetup -p1 -n webauthn-%{version}

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
