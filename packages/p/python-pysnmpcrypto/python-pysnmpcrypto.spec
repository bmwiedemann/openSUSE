#
# spec file for package python-pysnmpcrypto
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-pysnmpcrypto
Version:        0.0.4
Release:        0
Summary:        Strong cryptography support for PySNMP (SNMP library for Python)
License:        BSD-2-Clause
URL:            https://github.com/etingof/pysnmpcrypto
Source:         https://files.pythonhosted.org/packages/source/p/pysnmpcrypto/pysnmpcrypto-%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
BuildArch:      noarch
%python_subpackages

%description
Strong cryptography support for PySNMP (SNMP library for Python)

%prep
%autosetup -p1 -n pysnmpcrypto-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.txt CHANGES.txt README.md
%license LICENSE.rst
%{python_sitelib}/pysnmpcrypto
%{python_sitelib}/pysnmpcrypto-%{version}.dist-info

%changelog
