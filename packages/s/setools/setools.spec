#
# spec file for package setools
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define software_name setools

%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define name_suffix %{nil}
%else
%define name_suffix -%{flavor}
%endif

%{?sle15_python_module_pythons}
%if 0%{?suse_version} < 1600
# set python_for_executables from python macros to python311
# to build python scripts in bin dirs only for python311
%define python_for_executables python311
%endif

%if "%{flavor}" == "test"
# The test flavor does not package any files, it only builds the software and
# runs the tests. To simplify test execution, the software is actually
# installed in the buildroot first. After the tests have passed, the buildroot
# is deleted. As debuginfo generation is done based on the contents of the
# buildroot after the install section, and before the check section, the final
# debuginfo step will expect to find the now deleted files in the buildroot.
# Disable debuginfo generation in the test flavor to avoid these issues.
# Since the test flavor does not produce any RPMs, this is not a problem.
%define debug_package %{nil}
%if 0%{?suse_version} <= 1600
# Test dependencies such as python-PyQt6, python-NetworkX, python-pytest-qt
# are not found in other distributions.
# Do not build test flavor for distributions which cannot run tests.
ExclusiveArch:  do_not_build
%endif
%endif

Name:           setools%{name_suffix}
Version:        4.6.0
Release:        0
URL:            https://github.com/SELinuxProject/setools
Summary:        Policy analysis tools for SELinux
License:        GPL-2.0-only
Group:          System/Management
Source:         https://github.com/SELinuxProject/setools/releases/download/%{version}/%{software_name}-%{version}.tar.bz2
Source2:        https://github.com/SELinuxProject/setools/releases/download/%{version}/%{software_name}-%{version}.tar.bz2.sha256.asc
Source3:        setools.keyring
Source4:        README.SUSE
BuildRequires:  %{python_module Cython >= 0.29.14}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel >= 3.2
BuildRequires:  python-rpm-macros
%if "%{flavor}" == "test"
BuildRequires:  %{python_module PyQt6}
BuildRequires:  %{python_module networkx >= 2.6}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tox}
BuildRequires:  checkpolicy
%endif
%if "%{flavor}" != "test"
Requires:       setools-console = %{version}-%{release}
Requires:       setools-gui = %{version}-%{release}
# needed since setools is not a python-main package, see
# https://github.com/openSUSE/python-rpm-macros
%define python_subpackage_only 1
%python_subpackages
%endif

%description
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This meta-package depends upon the main packages necessary to run
SETools.

%if "%{flavor}" != "test"
%package console
Summary:        Policy analysis command-line tools for SELinux
License:        GPL-2.0-only
Group:          System/Base
Requires:       %{python_for_executables}-setools = %{version}

%description console
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  seinfo          Provide information about policies
  sesearch        Tool to query policies
  sedta           Domain transition analysis tool
  seinfoflow      Information flow analysis tool
  sediff          Semantic policy difference tool

%package -n python-setools
Summary:        Python bindings for SELinux policy analysis
License:        LGPL-2.0-only
Group:          Development/Languages/Python
Requires:       %{python_for_executables} >= 3.10
Requires:       %{python_for_executables}-setuptools
# Only suggest python-networkx due to its large amount of dependencies
# (see README.SUSE)
Suggests:       %{python_for_executables}-networkx
Obsoletes:      python-setools < %{version}-%{release}
Provides:       python-setools = %{version}-%{release}
%if "%{python_flavor}" != "python3"
Obsoletes:      python3-setools < %{version}-%{release}
%endif

%description -n python-setools
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

%package gui
Summary:        Policy analysis graphical tools for SELinux
License:        GPL-2.0-only
Group:          System/Base
Requires:       %{python_for_executables}-PyQt6
Requires:       %{python_for_executables}-pygraphviz
Requires:       %{python_for_executables}-setools = %{version}

%description gui
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following graphical tools:

  apol          policy analysis tool
%endif

%prep
%setup -q -n %{software_name}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%if "%{flavor}" != "test"
install -m 644 -D %{SOURCE2} %{buildroot}%{_docdir}/%{software_name}/README.SUSE
%python_expand %fdupes -s %{buildroot}%{$python_sitearch}
%endif

%check
%if "%{flavor}" == "test"
# Remove the module directories to prevent Python loading the modules from CWD.
# This way, the modules are actually loaded from the buildroot, which is
# inserted on the PATH by the pytest macros
rm -rf setools setoolsgui
%pytest_arch -v
# The test flavor should not package any files
rm -rf %{buildroot}
%endif

%if "%{flavor}" != "test"
%files %{python_files setools}
%defattr(-,root,root,-)
%{python_sitearch}/setools
%{python_sitearch}/setoolsgui
%{python_sitearch}/setools-%{version}*-info

%files console
%defattr(-,root,root,-)
%{_bindir}/seinfo
%{_bindir}/sesearch
%{_bindir}/sedta
%{_bindir}/seinfoflow
%{_bindir}/sediff
%{_bindir}/sechecker
%{_mandir}/man1/sechecker.1.gz
%{_mandir}/man1/sedta.1.gz
%{_mandir}/man1/seinfoflow.1.gz
%{_mandir}/man1/sediff.1.gz
%{_mandir}/man1/seinfo.1.gz
%{_mandir}/man1/sesearch.1.gz
%{_mandir}/ru/man1/apol.1.gz
%{_mandir}/ru/man1/sediff.1.gz
%{_mandir}/ru/man1/sedta.1.gz
%{_mandir}/ru/man1/seinfo.1.gz
%{_mandir}/ru/man1/seinfoflow.1.gz
%{_mandir}/ru/man1/sesearch.1.gz
%dir %{_docdir}/%{software_name}/
%{_docdir}/%{software_name}/*

%files gui
%defattr(-,root,root,-)
%{_bindir}/apol
%{_mandir}/man1/apol.1.gz
%endif

%changelog
