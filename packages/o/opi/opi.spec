#
# spec file for package opi
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


%define use_python python3
%define pythons %{use_python}

Name:           opi
Version:        5.6.0
Release:        0
Summary:        OBS Package Installer (CLI)
License:        GPL-3.0-only
Group:          System/Packages
URL:            https://github.com/openSUSE/opi
Source0:        https://github.com/openSUSE/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

BuildRequires:  help2man
BuildRequires:  python3
BuildRequires:  python3-curses
BuildRequires:  python3-lxml
BuildRequires:  python3-requests
BuildRequires:  python3-rpm
BuildRequires:  python3-setuptools
BuildRequires:  python3-termcolor
Requires:       sudo
Requires:       zypper
# rpm --import used curl but doesn't require it explicitly
Requires:       curl
Requires:       python3-curses
Requires:       python3-lxml
Requires:       python3-requests
Requires:       python3-rpm
Requires:       python3-termcolor
Requires:       zypper
# for rpm building and snap extracting
Requires:       rpm-build
Requires:       squashfs

%description
OBS Package Installer (CLI)
Search and install almost all packages available for openSUSE and SLE:
- openSUSE Build Service
- Packman
- Popular packages for 3rd party vendors

%prep
%setup -q

%build
help2man -s8 -N ./bin/opi > opi.8
%pyproject_wheel

%install
%pyproject_install
install -m 644 -D -v org.openSUSE.opi.appdata.xml %{buildroot}%{_datadir}/metainfo/org.openSUSE.opi.appdata.xml
install -m 644 -D -v opi.8 %{buildroot}%{_datadir}/man/man8/opi.8
install -m 644 -D -v opi.default.cfg %{buildroot}%{_sysconfdir}/opi.cfg
%python3_fix_shebang
%fdupes %{buildroot}%{python3_sitelib}

%check

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.openSUSE.opi.appdata.xml
%{_datadir}/man/man8/opi.8%{?ext_man}
%{python3_sitelib}/*
%config %{_sysconfdir}/opi.cfg

%changelog
