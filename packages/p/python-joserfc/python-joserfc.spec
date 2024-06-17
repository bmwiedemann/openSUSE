#
# spec file for package python-joserfc
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
Name:           python-joserfc
Version:        0.12.0
Release:        0
Summary:        The ultimate Python library for JOSE RFCs
License:        BSD-3-Clause
URL:            https://github.com/authlib/joserfc
Source:         https://files.pythonhosted.org/packages/source/j/joserfc/joserfc-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cryptography
Suggests:       python-pycryptodome
BuildArch:      noarch
%python_subpackages

%description
The ultimate Python library for JOSE RFCs, including JWS, JWE, JWK, JWA, JWT

%prep
%autosetup -p1 -n joserfc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/joserfc
%{python_sitelib}/joserfc-%{version}.dist-info

%changelog
