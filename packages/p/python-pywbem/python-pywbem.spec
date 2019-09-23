#
# spec file for package python-pywbem
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global         pkgname pywbem
Name:           python-pywbem
Version:        0.11.0
Release:        0
Summary:        Python module for making CIM operation calls using the WBEM protocol
License:        LGPL-2.1
Group:          System/Management
URL:            http://pywbem.github.io/
Source0:        pywbem-%{version}.tar.gz
BuildRequires:  %{python_module M2Crypto}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-PyYAML
Requires:       python-ply
Requires:       python-xml
Requires:       python-six
Requires:       python-M2Crypto
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Provides:       pywbem = %{version}
%endif
%python_subpackages

%description
PyWBEM is a Python module for making CIM operation calls using the WBEM
protocol to query and update managed objects.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}
# don't clash with sblim-wbemcli
mv %{buildroot}%{_bindir}/wbemcli %{buildroot}%{_bindir}/pywbemcli
rm %{buildroot}%{_bindir}/*.bat
%python_clone -a %{buildroot}%{_bindir}/pywbemcli
%python_clone -a %{buildroot}%{_bindir}/wbemcli.py
%python_clone -a %{buildroot}%{_bindir}/mof_compiler

%post
%python_install_alternative pywbemcli
%python_install_alternative wbemcli.py
%python_install_alternative mof_compiler

%postun
%python_uninstall_alternative pywbemcli
%python_uninstall_alternative wbemcli.py
%python_uninstall_alternative mof_compiler

%files %{python_files}
%doc README.rst pywbem/LICENSE.txt
%python_alternative %{_bindir}/pywbemcli
%python_alternative %{_bindir}/wbemcli.py
%python_alternative %{_bindir}/mof_compiler
%{python_sitelib}/*

%changelog
