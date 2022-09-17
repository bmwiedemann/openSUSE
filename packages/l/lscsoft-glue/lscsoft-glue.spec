#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
# Tests known to fail on 32 bit due to fp precision
ExcludeArch:    %{ix86}
%else
%bcond_with test
%define psuffix %{nil}
%endif

%define pname lscsoft-glue
# NEP 29: numpy, matplotlib do not have a python36 flavor package in TW
%define skip_python36 1
# Support dropped for python2 by upstream
%define skip_python2 1

%define ligocommands ligolw_combine_segments ligolw_diff ligolw_dq_active ligolw_dq_active_cats ligolw_inspiral2mon ligolw_print_tables

%define modname glue
Name:           lscsoft-glue%{psuffix}
Version:        3.0.1
Release:        0
Summary:        Grid LSC User Environment
License:        GPL-2.0-only
URL:            http://software.ligo.org/lscsoft
Source:         https://files.pythonhosted.org/packages/source/l/lscsoft-glue/%{pname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{pname}-data = %{version}
Requires:       python-ligo-segments
Requires:       python-numpy
Requires:       python-pyRXP
Provides:       python-glue = %{version}-%{release}
Obsoletes:      python-glue < %{version}-%{release}
%define oldpython python
Provides:       %{oldpython}-glue = %{version}-%{release}
Obsoletes:      %{oldpython}-glue < %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module ligo-segments}
BuildRequires:  %{python_module lscsoft-glue = %{version}}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pyRXP}
BuildRequires:  %{python_module pytest}
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Glue is a collection of utilities for running data analysis pipelines
for online and offline analysis as well as accessing various grid
utilities.  It also provides the infrastructure for the segment
database.

%package -n %{pname}-data
Summary:        Collection of data files for use by %{name}

%description -n %{pname}-data
Glue is a collection of utilities for running data analysis pipelines
for online and offline analysis as well as accessing various grid
utilities.  It also provides the infrastructure for the segment
database.

This package provides a common set of data files for %{name}.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%if ! %{with test}
%python_build
%endif

%install
%if ! %{with test}
%python_install

# SECTION Remove non-library config/php files
rm -fr %{buildroot}%{_prefix}%{_sysconfdir}
rm -fr %{buildroot}%{_prefix}%{_localstatedir}
# /SECTION

%{lua: for c in string.gmatch(rpm.expand("%ligocommands"), "%S+") do
  print(rpm.expand("%python_clone -a %{buildroot}%{_bindir}/" .. c .. "\n"))
end}

%python_expand %fdupes -s %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# test_ldbd.py requires network; disable
%pytest_arch -k 'not test_ldbd'
%endif

%if ! %{with test}
%post
%python_install_alternative %ligocommands

%postun
# arguments after the master item are ignored
%python_uninstall_alternative %ligocommands

%files -n %{pname}-data
%{_datadir}/%{name}/

%files %{python_files}
%doc README.md
%license LICENSE
%{lua: for c in string.gmatch(rpm.expand("%ligocommands"), "%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. c .. "\n"))
end}
%{python_sitearch}/glue
%{python_sitearch}/lscsoft_glue-%{version}*-info
%endif

%changelog
