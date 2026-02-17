#
# spec file for package python-signxml
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


Name:           python-signxml
Version:        4.3.0
Release:        0
Summary:        Python XML Signature and XAdES library
License:        Apache-2.0
URL:            https://github.com/XML-Security/signxml
Source:         https://files.pythonhosted.org/packages/source/s/signxml/signxml-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module certifi >= 2023.11.17}
BuildRequires:  %{python_module cryptography >= 43}
BuildRequires:  %{python_module lxml >= 5.2.1}
BuildRequires:  %{python_module testsuite}
# /SECTION
BuildRequires:  fdupes
Requires:       python-certifi >= 2023.11.17
Requires:       python-cryptography >= 43
Requires:       python-lxml >= 5.2.1
BuildArch:      noarch
%python_subpackages

%description
SignXML is an implementation of the W3C XML Signature standard in
Python. This standard (also known as "XMLDSig") is used to provide payload security in SAML 2.0,
EBICS, and `WS-Security, among other uses. The standard is defined in the `W3C Recommendation
XML Signature Syntax and Processing Version 1.1.

%prep
%autosetup -p1 -n signxml-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test/test.py

%files %{python_files}
%doc Changes.rst README.rst NOTICE
%license LICENSE
%{python_sitelib}/signxml
%{python_sitelib}/signxml-%{version}.dist-info

%changelog
