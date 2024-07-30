#
# spec file for package python-pysnmp
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


Name:           python-pysnmp
Version:        6.2.4
Release:        0
Summary:        A pure-Python SNMPv1/v2c/v3 library
License:        BSD-2-Clause
URL:            https://github.com/lextudio/pysnmp
Source:         https://files.pythonhosted.org/packages/source/p/pysnmp/pysnmp-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pysmi}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  net-snmp
BuildRequires:  python-rpm-macros
Requires:       python-pyasn1 >= 0.4.8
Requires:       python-pysmi
Requires:       python-pysnmpcrypto
BuildArch:      noarch
%python_subpackages

%description
This project is a SNMP v1/v2c/v3 engine written in the Python
programming language.

    * Complete SNMPv1/v2c and SNMPv3 engine support
    * Can act as Manager and/or Agent
    * Manager and Agent side MIB support
    * Asynchronous operations support
    * Pure-Python implementation
    * py2exe and .egg friendly
    * Twisted binding

%package -n python-pysnmp-doc
Summary:        PySNMP documentation
Provides:       %{python_module pysnmp-doc = %{version}}

%description -n python-pysnmp-doc
PySNMP documentation and examples.

%prep
%autosetup -p1 -n pysnmp-%{version}
# Remove uneeded files
find docs -name "\.*" -exec rm -Rf {} +

%build
%pyproject_wheel

%install
%pyproject_install
chmod -x docs/net-snmptrapd.conf docs/net-snmpd.conf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="test_addAsn1MibSource"

# Running tests with python -m to make it work with the import path
%{python_expand #
# Not running asyncio tests that requires network
$python -m pytest -v -m 'not asyncio' -k "not $donttest"
}

%files %{python_files}
%license LICENSE.rst
%doc README.md docs examples
%{python_sitelib}/pysnmp
%{python_sitelib}/pysnmp-%{version}.dist-info

%files -n python-pysnmp-doc
%license LICENSE.rst
%doc docs examples

%changelog
