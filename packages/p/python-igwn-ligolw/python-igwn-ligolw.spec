#
# spec file for package python-igwn-ligolw
#
# Copyright (c) 2025 SUSE LLC
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

%define modname igwn_ligolw
Name:           python-igwn-ligolw
Version:        2.1.0
Release:        0
Summary:        Python LIGO Light-Weight XML I/O Library
License:        GPL-3.0-or-later
URL:            https://igwn-ligolw.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/i/igwn-ligolw/%{modname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 74.1.0}
BuildRequires:  %{python_module setuptools_scm >= 8}
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module igwn-segments}
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module tqdm}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML
Requires:       python-igwn-segments
Requires:       python-numpy
Requires:       python-python-dateutil
Requires:       python-tqdm
Provides:       python-%{modname} = %{version}
Recommends:     python-lal
Recommends:     python-furo
%python_subpackages

%description
This module provides a python LIGO Light-Weight XML I/O Library

%package devel
Summary:        Headers and sources for developing with igwn_ligolw
Requires:       python-igwn-ligolw = %{version}

%description devel
This module provides a python LIGO Light-Weight XML I/O Library

This package provides the headers and sources for developing with igwn_ligolw.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/igwn_ligolw_add
%python_clone -a %{buildroot}%{_bindir}/igwn_ligolw_cut
%python_clone -a %{buildroot}%{_bindir}/igwn_ligolw_no_ilwdchar
%python_clone -a %{buildroot}%{_bindir}/igwn_ligolw_print
%python_clone -a %{buildroot}%{_bindir}/igwn_ligolw_run_sqlite
%python_clone -a %{buildroot}%{_bindir}/igwn_ligolw_segments
%python_clone -a %{buildroot}%{_bindir}/igwn_ligolw_sqlite
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%post
%python_install_alternative igwn_ligolw_add igwn_ligolw_cut igwn_ligolw_no_ilwdchar igwn_ligolw_print igwn_ligolw_run_sqlite igwn_ligolw_segments igwn_ligolw_sqlite

%postun
%python_uninstall_alternative igwn_ligolw_add

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/igwn_ligolw_add
%python_alternative %{_bindir}/igwn_ligolw_cut
%python_alternative %{_bindir}/igwn_ligolw_no_ilwdchar
%python_alternative %{_bindir}/igwn_ligolw_print
%python_alternative %{_bindir}/igwn_ligolw_run_sqlite
%python_alternative %{_bindir}/igwn_ligolw_segments
%python_alternative %{_bindir}/igwn_ligolw_sqlite
%dir %{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}/*.so
%{python_sitearch}/%{modname}/*.py
%{python_sitearch}/%{modname}/__pycache__/
%{python_sitearch}/%{modname}/utils/
%{python_sitearch}/%{modname}-%{version}.dist-info/

%files %{python_files devel}
%dir %{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}/*.h
%{python_sitearch}/%{modname}/*.c


%changelog
