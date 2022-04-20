#
# spec file for package python-snimpy
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2016-2021, Martin Hauke <mardnh@gmx.de>
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
%global skip_python2 1
Name:           python-snimpy
Version:        1.0.0
Release:        0
Summary:        Interactive SNMP tool
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/vincentbernat/snimpy
Source:         https://files.pythonhosted.org/packages/source/s/snimpy/snimpy-%{version}.tar.gz
Patch0:         python-snimpy-disable-IPv6-tests.diff
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner}
BuildRequires:  fdupes
BuildRequires:  libsmi-devel
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pysnmp >= 4}
BuildRequires:  %{python_module setuptools}
# /SECTION
Requires:       python-cffi >= 1.0.0
Requires:       python-pycryptodomex
Requires:       python-pysnmp >= 4
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Snimpy is a Python-based tool providing a simple interface to build
SNMP query. You can either use Snimpy interactively through its console
(derived from Python own console or from IPython_ if available) or write
Snimpy scripts which are just Python scripts with some global variables
available.

Snimpy is aimed at being the more Pythonic possible. You should forget
that you are doing SNMP requests. Snimpy will rely on MIB to hide SNMP
details. Here are some "features":

 * MIB parser based on libsmi  (through CFFI)
 * SNMP requests are handled by PySNMP (SNMPv1, SNMPv2 and SNMPv3
   support)
 * scalars are just attributes of your session object
 * columns are like a Python dictionary and made available as an
   attribute
 * getting an attribute is like issuing a GET method
 * setting an attribute is like issuing a SET method
 * iterating over a table is like using GETNEXT
 * when something goes wrong, you get an exception

%prep
%setup -q -n snimpy-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/snimpy
%python_clone -a %{buildroot}%{_mandir}/man1/snimpy.1

%check
# https://github.com/vincentbernat/snimpy/issues/98
sed -i 's:import mock:from unittest import mock:' tests/test_{basictypes,main}.py
%python_exec -m unittest discover tests -v

%post
%python_install_alternative snimpy snimpy.1

%postun
%python_uninstall_alternative snimpy snimpy.1

%files %{python_files}
%license docs/license.rst
%doc AUTHORS.rst README.rst
%python_alternative %{_bindir}/snimpy
%python_alternative %{_mandir}/man1/snimpy.1%{ext_man}
%{python_sitearch}/snimpy*

%changelog
