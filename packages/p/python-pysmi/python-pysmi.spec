#
# spec file for package python-pysmi
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
Name:           python-pysmi
Version:        0.3.4
Release:        0
Summary:        SNMP SMI/MIB Parser
License:        BSD-2-Clause
URL:            http://pysmi.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/p/pysmi/pysmi-%{version}.tar.gz
BuildRequires:  %{python_module ply}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ply
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A pure-Python implementation of SNMP/SMI MIB parsing and conversion library.
Can produce PySNMP MIB modules.

Documentation: http://pysmi.sf.net

%prep
%setup -q -n pysmi-%{version}

%build
%python_build

%install
%python_install
mv %{buildroot}%{_bindir}/mibdump.py %{buildroot}%{_bindir}/mibdump
mv %{buildroot}%{_bindir}/mibcopy.py %{buildroot}%{_bindir}/mibcopy
%python_clone -a %{buildroot}%{_bindir}/mibdump
%python_clone -a %{buildroot}%{_bindir}/mibcopy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative mibdump

%postun
%python_uninstall_alternative mibdump

#%%check
#nosetests # cannot be run without pysmnp which needs this package

%files %{python_files}
%license LICENSE.rst
%doc README.md CHANGES.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/mibdump
%python_alternative %{_bindir}/mibcopy

%changelog
