#
# spec file for package setools
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


%{?sle15_python_module_pythons}
%if 0%{?suse_version} < 1600
# set python_for_executables from python macros to python311
# to build python scripts in bin dirs only for python311
%define python_for_executables python311
%endif

Name:           setools
Version:        4.5.1
Release:        0
URL:            https://github.com/SELinuxProject/setools
Summary:        Policy analysis tools for SELinux
License:        GPL-2.0-only
Group:          System/Management
Source:         https://github.com/SELinuxProject/setools/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source2:        README.SUSE
BuildRequires:  %{python_module Cython >= 0.29.14}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  python-rpm-macros
Requires:       setools-console = %{version}-%{release}
Requires:       setools-gui = %{version}-%{release}
# needed since setools is not a python-main package, see
# https://github.com/openSUSE/python-rpm-macros
%define python_subpackage_only 1
%python_subpackages

%description
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This meta-package depends upon the main packages necessary to run
SETools.

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

%prep
%setup -q -n %{name}
%autopatch -p1

%build
%python_build

%install
%python_install
install -m 644 -D %{SOURCE2} %{buildroot}%{_docdir}/%{name}/README.SUSE
%fdupes -s %{buildroot}%{python_sitearch}

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
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/*

%files gui
%defattr(-,root,root,-)
%{_bindir}/apol
%{_mandir}/man1/apol.1.gz

%changelog
