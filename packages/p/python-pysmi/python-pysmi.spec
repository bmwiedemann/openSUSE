#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pysmi%{psuffix}
Version:        0.3.4
Release:        0
Summary:        SNMP SMI/MIB Parser
License:        BSD-2-Clause
URL:            http://pysmi.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/p/pysmi/pysmi-%{version}.tar.gz
BuildRequires:  %{python_module ply}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
%if %{with test}
BuildRequires:  %{python_module pysnmp}
%endif
Requires:       python-ply
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
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
%if !%{with test}
%python_install
mv %{buildroot}%{_bindir}/mibdump.py %{buildroot}%{_bindir}/mibdump
mv %{buildroot}%{_bindir}/mibcopy.py %{buildroot}%{_bindir}/mibcopy
%python_clone -a %{buildroot}%{_bindir}/mibdump
%python_clone -a %{buildroot}%{_bindir}/mibcopy
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pyunittest -v tests
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
%doc README.md CHANGES.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/mibdump
%python_alternative %{_bindir}/mibcopy
%endif

%changelog
