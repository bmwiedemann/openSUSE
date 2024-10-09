#
# spec file for package python-pysmi
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pysmi%{psuffix}
Version:        1.5.0
Release:        0
Summary:        SNMP SMI/MIB Parser
License:        BSD-2-Clause
URL:            https://github.com/lextudio/pysmi
Source:         https://files.pythonhosted.org/packages/source/p/pysmi/pysmi-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#lextudio/pysmi#5
Patch0:         support-new-pyasn1.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Jinja2 >= 3.1}
BuildRequires:  %{python_module ply >= 3.11}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pysmi = %{version}}
BuildRequires:  %{python_module pysnmp}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.26}
%endif
Requires:       python-Jinja2 >= 3.1
Requires:       python-ply >= 3.11
Requires:       python-requests >= 2.26
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
A pure-Python implementation of SNMP/SMI MIB parsing and conversion library.
Can produce PySNMP MIB modules.

%prep
%autosetup -p1 -n pysmi-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mibdump
%python_clone -a %{buildroot}%{_bindir}/mibcopy
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative mibdump

%post
%python_install_alternative mibdump

%postun
%python_uninstall_alternative mibdump

%files %{python_files}
%license LICENSE.rst
%doc README.md examples/*
%{python_sitelib}/pysmi
%{python_sitelib}/pysmi-%{version}.dist-info
%python_alternative %{_bindir}/mibdump
%python_alternative %{_bindir}/mibcopy
%endif

%changelog
