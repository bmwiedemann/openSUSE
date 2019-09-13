#
# spec file for package python-pysnmp
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
Name:           python-pysnmp
Version:        4.4.11
Release:        0
Summary:        A pure-Python SNMPv1/v2c/v3 library
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/etingof/pysnmp
Source:         https://github.com/etingof/pysnmp/archive/v%{version}.tar.gz#/pysnmp-%{version}.tar.gz
BuildRequires:  %{python_module pyasn1 >= 0.2.3}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module pysmi}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyasn1 >= 0.2.3
Requires:       python-pycryptodome
Requires:       python-pysmi
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
Group:          Documentation/HTML
Provides:       %{python_module pysnmp-doc = %{version}}

%description -n python-pysnmp-doc
PySNMP documentation and examples.

%prep
%setup -q -n pysnmp-%{version}
# Remove uneeded files
find docs -name "\.*" -exec rm -Rf {} +

%build
%python_build

%install
%python_install
chmod -x docs/net-snmptrapd.conf docs/net-snmpd.conf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

### Disable checks since those require network access to demo.snmplabs.com
#%%check
#%%python_expand PYTHONPATH=%%{buildroot}%%{$python_sitelib} ./runtests.sh

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.txt README.md THANKS.txt TODO.txt docs examples
%{python_sitelib}/pysnmp/
%{python_sitelib}/pysnmp-%{version}-py%{py_ver}.egg-info

%files -n python-pysnmp-doc
%license LICENSE.rst
%doc docs examples

%changelog
