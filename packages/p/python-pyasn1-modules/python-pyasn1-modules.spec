#
# spec file for package python-pyasn1-modules
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?sle15_python_module_pythons}
Name:           python-pyasn1-modules
Version:        0.3.0
Release:        0
Summary:        Collection of protocols modules written in ASN.1 language
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyasn1/pyasn1-modules
Source:         https://files.pythonhosted.org/packages/source/p/pyasn1-modules/pyasn1_modules-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyasn1 >= 0.4.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyasn1 >= 0.4.7
BuildArch:      noarch
%python_subpackages

%description
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP) but
then generalized to be suitable for a wide range of protocols based on ASN.1
specification.

%prep
%setup -q -n pyasn1_modules-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.txt README.md
%{python_sitelib}/pyasn1_modules
%{python_sitelib}/pyasn1_modules-%{version}.dist-info

%changelog
