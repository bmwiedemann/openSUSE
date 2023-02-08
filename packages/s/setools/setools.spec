#
# spec file for package setools
#
# Copyright (c) 2023 SUSE LLC
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


# As soon as python38 is introduced as flavor, we need this:
%{?!python3_primary_provider:%define python3_primary_provider %{lua: \
l,c = posix.readlink("/usr/bin/python3") \
flavor = l:gsub("%.", ""):sub(0,-1) \
print(rpm.expand("%{?" .. flavor .. "_prefix}%{!?" .. flavor .. "_prefix:python3}")) \
}}
# Skip every flavor except for the primary_provider
%define pythons %python3_primary_provider

Name:           setools
Version:        4.4.1
Release:        0
URL:            https://github.com/SELinuxProject/setools
Summary:        Policy analysis tools for SELinux
License:        GPL-2.0-only
Group:          System/Management
Source:         https://github.com/SELinuxProject/setools/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source2:        README.SUSE
# PATCH-FIX-UPSTREAM https://github.com/SELinuxProject/setools/pull/68
Patch1:         make_networkx_optional.patch
BuildRequires:  fdupes
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-setuptools
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

%package -n %{python3_primary_provider}-setools
Summary:        Python bindings for SELinux policy analysis
License:        LGPL-2.0-only
Group:          Development/Languages/Python
Requires:       python3 >= 3.4
Obsoletes:      python-setools < %{version}-%{release}
Provides:       python-setools = %{version}-%{release}
%if "%{python3_primary_provider}" != "python3"
Obsoletes:      python3-setools < %{version}-%{release}
Provides:       python3-setools = %{version}-%{release}
%endif

%description -n %{python3_primary_provider}-setools
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

%package gui
Summary:        Policy analysis graphical tools for SELinux
License:        GPL-2.0-only
Group:          System/Base
Requires:       python3-networkx
Requires:       python3-qt5
Requires:       python3-setools = %{version}

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
%fdupes -s %{buildroot}%{python3_sitearch}

%files -n %{python3_primary_provider}-setools
%defattr(-,root,root,-)
%{python3_sitearch}/setools
%{python3_sitearch}/setools-%{version}*-info
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/*

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

%files gui
%defattr(-,root,root,-)
%{python3_sitearch}/setoolsgui
%{_bindir}/apol
%{_mandir}/man1/apol.1.gz

%changelog
