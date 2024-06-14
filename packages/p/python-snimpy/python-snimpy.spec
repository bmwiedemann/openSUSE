#
# spec file for package python-snimpy
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-snimpy
Version:        1.0.3
Release:        0
Summary:        Interactive SNMP tool
License:        ISC
URL:            https://github.com/vincentbernat/snimpy
Source:         https://files.pythonhosted.org/packages/source/s/snimpy/snimpy-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libsmi-devel
BuildRequires:  python-rpm-macros
Requires:       python-cffi >= 1.0.0
Requires:       python-pysnmp >= 5
Requires:       python-setuptools
Requires:       (python-pyasyncore if python-base >= 3.12)
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION test requirements
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module pyasyncore if %python-base >= 3.12}
BuildRequires:  %{python_module pysnmp >= 5}
BuildRequires:  %{python_module pytest}
# /SECTION
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
%autosetup -p1 -n snimpy-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/snimpy
%python_clone -a %{buildroot}%{_mandir}/man1/snimpy.1

%check
%pytest_arch

%post
%python_install_alternative snimpy snimpy.1

%postun
%python_uninstall_alternative snimpy snimpy.1

%files %{python_files}
%license docs/license.rst
%doc AUTHORS.rst README.rst
%python_alternative %{_bindir}/snimpy
%python_alternative %{_mandir}/man1/snimpy.1%{ext_man}
%{python_sitearch}/snimpy
%{python_sitearch}/snimpy-%{version}.dist-info

%changelog
