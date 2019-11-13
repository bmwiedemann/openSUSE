#
# spec file for package setools
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

# doesn't work for python 2
%define skip_python2 1

Name:           setools
Version:        4.2.2
Release:        0
Url:            https://github.com/SELinuxProject/setools
Summary:        Policy analysis tools for SELinux
License:        GPL-2.0-only
Group:          System/Management
Source:         https://github.com/SELinuxProject/setools/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM python3.8-compat.patch mcepl@suse.com
# allow build with Python 3.8
Patch0:         python3.8-compat.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  python-rpm-macros
BuildRequires:  swig
Requires:       setools-console = %{version}-%{release}
Requires:       setools-gui = %{version}-%{release}

%description
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This meta-package depends upon the main packages necessary to run
SETools.

%package console
Summary:        Policy analysis command-line tools for SELinux
License:        GPL-2.0-only
Group:          System/Base
Requires:       python3-setools = %{version}

%description console
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  seinfo          Provide information about policies
  sesearch        Tool to query policies
  sedta           Domain transition analysis tool
  seinfoflow      Information flow analysis tool
  sediff          Semantic policy difference tool

%package -n python3-setools
Summary:        Python bindings for SELinux policy analysis
License:        LGPL-2.0-only
Group:          Development/Languages/Python
Requires:       python
Obsoletes:      python-setools < %{version}
Provides:       python-setools = %{version}-%{release}

%description -n python3-setools
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

%package gui
Summary:        Policy analysis graphical tools for SELinux
License:        GPL-2.0-only
Group:          System/Base
Requires:       bwidget
Requires:       gtk2
Requires:       tcl
Requires:       tk

%description gui
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following graphical tools:

  apol          policy analysis tool

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%fdupes -s %{buildroot}%{python3_sitearch}

%files -n python3-setools
%defattr(-,root,root,-)
%dir %{python3_sitearch}/setools/
%{python3_sitearch}/setools/*
%{python3_sitearch}/setools*egg-info*

%files console
%defattr(-,root,root,-)
%{_bindir}/seinfo
%{_bindir}/sesearch
%{_bindir}/sedta
%{_bindir}/seinfoflow
%{_bindir}/sediff
%{_mandir}/man1/sedta.1.gz
%{_mandir}/man1/seinfoflow.1.gz
%{_mandir}/man1/sediff.1.gz
%{_mandir}/man1/seinfo.1.gz
%{_mandir}/man1/sesearch.1.gz

%files gui
%defattr(-,root,root,-)
%{python3_sitearch}/setoolsgui*
%{_bindir}/apol
%{_mandir}/man1/apol.1.gz

%changelog
